'''
Author: TianMingXTU 1600410115@qq.com
Date: 2024-11-28 15:00:04
LastEditors: TianMingXTU 1600410115@qq.com
LastEditTime: 2024-11-28 15:00:21
FilePath: \GitPull\CreateProject\xml_handler.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import xml.etree.ElementTree as ET

def xml_to_dict(element: ET.Element) -> dict:
    """Convert an XML element to a dictionary."""
    if len(element) == 0:
        return element.text or ""
    return {child.tag: xml_to_dict(child) for child in element}

def dict_to_xml(structure: dict, root_name: str = "root") -> str:
    """Convert a dictionary to an XML string."""
    root = ET.Element(root_name)
    _dict_to_xml_helper(structure, root)
    return ET.tostring(root, encoding="unicode")

def _dict_to_xml_helper(structure: dict, parent: ET.Element):
    """Helper function to recursively build XML from a dictionary."""
    for key, value in structure.items():
        child = ET.SubElement(parent, key)
        if isinstance(value, dict):
            _dict_to_xml_helper(value, child)
        else:
            child.text = value
