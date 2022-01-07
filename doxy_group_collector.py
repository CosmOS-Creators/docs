from pathlib import Path
from typing import List
import xml.etree.ElementTree as ET
import breathe

generated_files = list()

COMPOUND_DEF_XPATH = "./compounddef"
INNER_GROUP_XPATH = "./innergroup"
COMPOUND_NAME = "compoundname"
COMPOUND_TITLE = "title"
REF_ID = "refid"

RST_HEADER_TEMPLATE = """
{page_title}
=============================
"""

RST_TOCTREE_TEMPLATE = """
.. toctree::
    :caption: {toctree_caption}:
    :maxdepth: 1

{toctree_list}
"""

RST_DOXY_GROUP_TEMPLATE = """
.. doxygengroup:: {group_name}
    :project: {doxygen_project}

"""

RST_DOXY_GROUP_INNER_TEMPLATE = """
.. doxygengroup:: {group_name}
    :inner:

"""

HEADING_LEVELS = ['=', '-', '`', '"', ':', '~', '*', '^']

class doxy_group():
    def __init__(self, input_path: Path, refid: str, nesting_level: int = 0):
        self.__input_path = input_path
        self.__refid = refid
        self.__file = self.__input_path.joinpath(f'{self.__refid}.xml')
        self.__level = nesting_level

        self.__name: str = None
        self.__title: str = None
        self.__compound_def: ET.Element = None
        self.__parsed_xml: ET.Element = None
        self.__inner_groups: List[doxy_group] = None

    def __repr__(self) -> str:
        return f'doxy_group({self.name})'

    @property
    def refid(self):
        return self.__refid

    @property
    def name(self):
        if(self.__name is None):
            self.__name = self.__get_compound_name()
        return self.__name

    @property
    def title(self):
        if(self.__title is None):
            self.__title = self.__get_compound_title()
        return self.__title

    @property
    def inner_groups(self):
        if(self.__inner_groups is None):
            self.__inner_groups = self.__get_inner_groups()
        return self.__inner_groups

    @property
    def nesting_level(self):
        return self.__level

    @property
    def _compound_def(self):
        if(self.__compound_def is None):
            self.__compound_def = self.__get_compound_def()
        return self.__compound_def

    @property
    def _parsed_xml(self):
        if(self.__parsed_xml is None):
            self.__parsed_xml = self.__parse_xml()
        return self.__parsed_xml

    def __parse_xml(self):
        return ET.parse(self.__file).getroot()

    def __get_compound_name(self):
        return self._compound_def.find(COMPOUND_NAME).text

    def __get_compound_title(self):
        return self._compound_def.find(COMPOUND_TITLE).text

    def __get_compound_def(self):
        compound_defs = self._parsed_xml.findall(COMPOUND_DEF_XPATH)
        if(len(compound_defs) != 1):
            raise Exception(f'Expected 1 compounddef in {self.__file} but found {len(compound_defs)}')
        return compound_defs[0]

    def __get_inner_groups(self):
        inner_groups = list()
        for inner_group in self._compound_def.findall(INNER_GROUP_XPATH):
            if(REF_ID in inner_group.attrib):
                inner_groups.append(doxy_group(self.__input_path, inner_group.attrib[REF_ID], self.__level + 1))
        return inner_groups

def rst_heading(heading: str, level: int = 0):
    if(level < len(HEADING_LEVELS)):
        return f'{heading}\n{len(heading) * HEADING_LEVELS[level]}\n'
    else:
        raise Exception(f'Heading level "{level}" requested, which exceeded the maximum allowed of {len(HEADING_LEVELS)}')

def generate_flat_rst_file_group(doxygen_group: doxy_group, doxygen_project: str, level: int = 0):
    file_content = rst_heading(doxygen_group.title, level)
    file_content += RST_DOXY_GROUP_TEMPLATE.format(group_name=doxygen_group.name, doxygen_project = doxygen_project)
    for inner_group in doxygen_group.inner_groups:
        file_content += generate_flat_rst_file_group(inner_group, doxygen_project, level + 1)
    return file_content

def generate_rst_file_group(doxygen_group: doxy_group, output_directory: Path, doxygen_project: str, recursive: bool = True, max_nesting_level: int = 2):
    flat_file_content = ""
    file_content = rst_heading(doxygen_group.title)
    if(len(doxygen_group.inner_groups) > 0):
        file_list = list()
        if(doxygen_group.nesting_level < max_nesting_level):
            for group in doxygen_group.inner_groups:
                if(recursive):
                    file_list.append(f'    {group.name}')
                    generate_rst_file_group(group, output_directory, doxygen_project, recursive, max_nesting_level)
            file_content += RST_TOCTREE_TEMPLATE.format(toctree_caption=doxygen_group.title, toctree_list='\n'.join(file_list))
        else:
            flat_file_content = generate_flat_rst_file_group(doxygen_group, doxygen_project)
    if(len(flat_file_content) > 0):
        file_content = flat_file_content
    else:
        file_content += RST_DOXY_GROUP_TEMPLATE.format(group_name = doxygen_group.name, doxygen_project = doxygen_project)
    filename = f'{doxygen_group.name}.rst'
    output_file = output_directory.joinpath(filename)
    if(output_file.exists()):
        if(output_file.read_text() != file_content):
            output_file.write_text(file_content)
    else:
        output_file.write_text(file_content)
    if(filename in generated_files):
        print("WARNING: File was already generated and might have been overwritten: " + filename)
    else:
        generated_files.append(filename)

def generate_root_rst_file(list_of_modules: List[doxy_group], output_directory: Path, file_title: str, file_name: str):
    file_content = rst_heading(file_title)
    file_list = [f'    {module.name}' for module in list_of_modules]
    file_content += RST_TOCTREE_TEMPLATE.format(toctree_caption=file_title, toctree_list='\n'.join(file_list))
    filename = f'{file_name}.rst'
    output_directory.joinpath(filename).write_text(file_content)

def parse_modules(input_path: Path, glob: str):
    modules = list()
    for file in input_path.glob(glob):
        refid = file.stem
        modules.append(doxy_group(input_path, refid))
    return modules

def convert_doxygen_to_rst(doxy_xml_input_path: str, output_rst_folder: str, root_title: str, root_file_name: str, doxygen_root_xml_file_glob: str, doxygen_project: str, recursive = True, max_nesting_level: int = 2) -> None:
    print("generating doxygen rst files...", end='')
    doxy_xml_input_path = Path(doxy_xml_input_path)
    output_rst_folder = Path(output_rst_folder)
    # for file in output_rst_folder.glob("*"):
    #     file.unlink()
    modules = parse_modules(doxy_xml_input_path, doxygen_root_xml_file_glob)
    if(output_rst_folder.exists() is False):
        output_rst_folder.mkdir(parents=True)
    generate_root_rst_file(modules, output_rst_folder, root_title, root_file_name)
    for module in modules:
        generate_rst_file_group(module, output_rst_folder, doxygen_project, recursive, max_nesting_level)
    print("DONE")
