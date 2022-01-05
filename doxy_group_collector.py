from pathlib import Path
from typing import List
import xml.etree.ElementTree as ET

generated_files = list()

MODULE_GLOB = "group__*__module.xml"

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

{toctree_list}
"""

RST_DOXY_GROUP_TEMPLATE = """
.. doxygengroup:: {group_name}


"""

class doxy_group():
    def __init__(self, input_path: Path, refid: str):
        self.__input_path = input_path
        self.__refid = refid
        self.__file = self.__input_path.joinpath(f'{self.__refid}.xml')

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
                inner_groups.append(doxy_group(self.__input_path, inner_group.attrib[REF_ID]))
        return inner_groups

def parse_modules(input_path: Path, glob: str):
    modules = list()
    for file in input_path.glob(glob):
        refid = file.stem
        modules.append(doxy_group(input_path, refid))
    return modules

def generate_rst_file_group(doxygen_group: doxy_group, output_directory: Path, recursive: bool = True):
    file_content = RST_HEADER_TEMPLATE.format(page_title=doxygen_group.title)
    if(len(doxygen_group.inner_groups) > 0):
        file_list = list()
        for group in doxygen_group.inner_groups:
            file_list.append(f'    {group.name}')
            if(recursive):
                generate_rst_file_group(group, output_directory, recursive)
        file_content += RST_TOCTREE_TEMPLATE.format(toctree_caption=doxygen_group.title, toctree_list='\n'.join(file_list))
    file_content += RST_DOXY_GROUP_TEMPLATE.format(group_name=doxygen_group.name)
    if(output_directory.exists() is False):
        output_directory.mkdir(parents=True)
    filename = f'{doxygen_group.name}.rst'
    output_directory.joinpath(filename).write_text(file_content)
    if(filename in generated_files):
        print("WARNING: File was already generated and might have been overwritten: " + filename)
    else:
        generated_files.append(filename)

def generate_root_rst_file(list_of_modules: List[doxy_group], output_directory: Path, file_title: str, file_name: str):
    file_content = RST_HEADER_TEMPLATE.format(page_title=file_title)
    file_list = [f'    {module.name}' for module in list_of_modules]
    file_content += RST_TOCTREE_TEMPLATE.format(toctree_caption=file_title, toctree_list='\n'.join(file_list))
    filename = f'{file_name}.rst'
    output_directory.joinpath(filename).write_text(file_content)

def generate_rst_files(doxy_xml_input_path: str, output_rst_folder: str, root_title: str, root_file_name: str, recursive = True) -> None:
    print("generating doxygen rst files...", end='')
    doxy_xml_input_path = Path(doxy_xml_input_path)
    output_rst_folder = Path(output_rst_folder)
    for file in output_rst_folder.glob("*"):
        file.unlink()
    modules = parse_modules(doxy_xml_input_path, MODULE_GLOB)
    generate_root_rst_file(modules, output_rst_folder, root_title, root_file_name)
    for module in modules:
        generate_rst_file_group(module, output_rst_folder, recursive)
    print("DONE")

if __name__ == "__main__":
    generate_rst_files(
        r"C:\Files\Projects\Developement\CosmOS\reference_project_stmIDE\Cosmos\docs\doxyout\xml",
    r"C:\Files\Projects\Developement\CosmOS\reference_project_stmIDE\Cosmos\docs\doxygen_rst",
    "Modules",
    "modules")
