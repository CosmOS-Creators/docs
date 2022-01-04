from pathlib import Path
from typing import List
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


MODULE_GLOB = "group__*__module.xml"

COMPOUND_DEF_XPATH = "./compounddef"
INNER_GROUP_XPATH = "./innergroup"
COMPOUND_NAME = "compoundname"
REF_ID = "refid"

class doxy_group():
    def __init__(self, input_path: Path, refid: str):
        self.__input_path = input_path
        self.__refid = refid
        self.__file = self.__input_path.joinpath(f'{self.__refid}.xml')

        self.__name: str = None
        self.__compound_def: ET.Element = None
        self.__parsed_xml: ET.Element = None
        self.__inner_groups: List[str] = None

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

def generate_rst_file(doxy_xml_input_path: str, output_rst_file: str) -> None:
    doxy_xml_input_path = Path(doxy_xml_input_path)
    output_rst_file = Path(output_rst_file)

    modules = parse_modules(doxy_xml_input_path, MODULE_GLOB)
    for module in modules:
        print(f'{module.name}: {module.inner_groups}')
        # get_next_level(doxy_xml_input_path, modules[module][0])



if __name__ == "__main__":
    generate_rst_file(r"C:\Files\Projects\Developement\CosmOS\reference_project_stmIDE\Cosmos\docs\doxyout\xml", "")
