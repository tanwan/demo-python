import unittest
from pathlib import Path
import xml.etree.ElementTree as ET
import os

curdir = Path(__file__).parent
original_workdir = os.getcwd()

class XMLDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        print(f"work directory: {os.getcwd()}")
        
    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_parse_xml(self):
        """读取xml文件"""
        tree = ET.parse("xml.xml")
        root = tree.getroot()
        for e in root.iter():
            # 元素名称会保留namespace
            print(f"tag:{e.tag}, text:{e.text}, attrs:{e.attrib}")
        # find:找到第一个匹配的元素,findall:找到所有匹配的元素,这边都需要使用namespace
        dog1 = root.find("{ns}animals").findtext("{ns}dog")
        print(f"dog1 text:{dog1}")

    def test_parse_xml_without_namespace(self):
        """读取xml文件"""
        tree = ET.parse("xml.xml")
        root = tree.getroot()
        for e in root.iter():
            # 去除namespace
            e.tag = e.tag.rpartition('}')[2]
        for e in root.iter():
            print(f"tag:{e.tag}, text:{e.text}, attrs:{e.attrib}")
        # find:找到第一个匹配的元素,findall:找到所有匹配的元素,这边都需要使用namespace
        cat1 = root.findall("animals")[1].findtext("cat")
        print(f"cat1 text:{cat1}")

