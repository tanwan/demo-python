import unittest
from pathlib import Path
from lxml import etree


class XpathDemo(unittest.TestCase):
    # xpath也可以直接从Chrome的开发者工具的Elements直接快速复制

    @classmethod
    def setUpClass(cls):
        with open(Path(__file__).parent / ".file/simple.html") as file:
            cls.dom = etree.HTML(file.read())

    def test_select_element(self):
        """
        xpath选择元素
        /: 选择根元素
        node: 从当前节点(默认为根节点)的子节点选择节点
        //: 从当前节点(默认根节点)的子孙节点选择节点
        *: 表示任意
        """
        # /: 选择根元素
        print("/html:", self.dom.xpath("/html"))

        # node: 从当前节点(默认为根节点)的子节点选择节点
        print("body:", self.dom.xpath("body")[0])

        # //: 从当前节点(默认根节点)的子孙节点选择节点
        print("//div:", self.dom.xpath("//div"))
        print("/html/body/div//p:", self.dom.xpath("/html/body/div//p"))

        # *用来表示任意
        print("use *:", self.dom.xpath("//*[@id='input-text']"))

        # 可以从选择出来的节点再使用xpath进行选择
        print("body xpath:", self.dom.xpath("body")[0].xpath("div"))

    def test_value_attr(self):
        """
        值和属性
        text: 获取元素的内容
        attrib: 获取元素的属性, 返回dict
        @attr: 获取属性, 返回list
        """
        div2 = self.dom.xpath("body/div[2]")[0]
        # text: 获取元素的内容
        # attrib: 获取元素的属性
        # @attr: 获取元素指定的属性
        print(div2.text, div2.attrib, self.dom.xpath("body/div[2]/@class"))

    def test_predicates(self):
        """
        谓语
        [index]: 选择指定下标的节点(以1为基准)
        last(): 获取节点的长度
        position: 获取当前元素的下标(以1为基准)
        node[@attr]: 选择具有attr属性的节点
        node[@attr=value]: 选择attr属性等于value的节点
        """
        # [index]: 选择指定下标的节点(以1为基准)
        print("//a[1]:", self.dom.xpath("//a[1]"))

        # last(): 获取节点的长度
        print("//a[last()]:", self.dom.xpath("//a[last()]"))

        # position: 获取当前元素的下标(以1为基准)
        print("//a[position()<3]:", self.dom.xpath("//a[position()<3]"))

        # node[@attr]: 选择具有attr属性的节点
        print("//a[@href]:", self.dom.xpath("//a[@href]"))

        # node[@attr=value]: 选择attr属性等于value的节点
        print("//a[@href='#']:", self.dom.xpath("//a[@href='#']"))
