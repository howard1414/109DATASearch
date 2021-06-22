import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
from xml.dom import minidom

STATIC = "./static"
XML_VERSION_STRING = '<?xml version="1.0" ?>\n'
dir_list = os.listdir(STATIC)
for d in dir_list:
    root = ET.Element("annotation")
    SubElement(root, "folder").text = STATIC+'label'
    SubElement(root, "filename").text = f"{d}.jpg"
    SubElement(root, "path").text = f"{STATIC}/label/{d}.jpg"
    SubElement(SubElement(root, "source"), "database").text = "Yu-Gi-Oh"

    # Size
    size = SubElement(root, "size")
    SubElement(size, "width").text = "421"
    SubElement(size, "height").text = "614"
    SubElement(size, "depth").text = "3"

    SubElement(root, "segmented").text = "0"

    # Object
    obj = SubElement(root, "object")
    SubElement(obj, "name").text = d
    SubElement(obj, "pose").text = "Unspecified"
    SubElement(obj, "truncated").text = "0"
    SubElement(obj, "difficult").text = "0"

    # bndbox
    bndbox = SubElement(obj, "bndbox")
    SubElement(bndbox, "xmin").text = "44"
    SubElement(bndbox, "ymin").text = "110"
    SubElement(bndbox, "xmax").text = "377"
    SubElement(bndbox, "ymax").text = "433"

    tree = ElementTree(root)
    formatted = minidom.parseString(ET.tostring(root)).toprettyxml()
    formatted = formatted.replace(XML_VERSION_STRING, "")
    with open(f"{STATIC}/label/{d}.xml", "w", encoding="utf-8") as f:
        f.write(formatted)
    print(dir_list.index(d)+1,'/',len(dir_list))