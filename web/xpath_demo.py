import unittest
from pathlib import PurePath
from lxml import etree


class RequestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(PurePath(__file__).parent / "file/simple.html") as file:
            cls.dom = etree.HTML(file.read())

    def test_base(self):
        """xpath 基础用法"""
        dom = self.dom
        # xpath也可以直接从Chrome的开发者工具的Elements直接快速复制
        # /: 选择根元素
        html = dom.xpath("/html")
        print(f"/html: {html}")

        # node: 从当前节点(默认为根节点)的子节点选择节点
        body = dom.xpath("body")[0]
        print(f"body: {body}")

        # //: 从当前节点(默认根节点)的子孙节点选择节点
        all_div = dom.xpath("//div")
        print(f"//div: {all_div}")
        all_div_p = dom.xpath("/html/body/div//p")
        print(f"/html/body/div//p: {all_div_p}")

        # @: 用来获取属性
        all_a_class = dom.xpath("//a/@href")
        print(f"//a/@href: {all_a_class}")

        # 可以从选择出来的节点再使用xpath进行选择
        body_div = body.xpath("div")
        print(f"body xpath: {body_div}")


    def test_value_attr(self):
        """值和属性"""
        dom = self.dom
        div2 = dom.xpath("body/div[2]")[0]
        # text: 获取元素的内容
        # attrib: 获取元素的属性
        print(f"text:{div2.text}, attrib:{div2.attrib}")

        # *用来表示任意
        # 直接获取出input的值
        text_input = dom.xpath("//*[@id='input-text']/@value")[0]
        print(f"input value: {text_input}")

    def test_predicates(self):
        """谓语"""
        dom = self.dom
        # [index]: 选择指定下标的节点(以1为基准)
        first_a = dom.xpath("//a[1]")
        print(f"//a[1]: {first_a}")

        # last(): 获取节点的长度
        last_a = dom.xpath("//a[last()]")
        print(f"//a[last()]: {last_a}")

        # position: 获取当前元素的下标(以1为基准)
        first_two_a = dom.xpath("//a[position()<3]")
        print(f"//a[position()<3]: {first_two_a}")

        # node[@attr]: 选择具有attr属性的节点
        all_a = dom.xpath("//a[@href]")
        print(f"//a[@href]: {all_a}")
        # node[@attr=value]: 选择attr属性等于value的节点
        equal_attr_a = dom.xpath("//a[@href='#']")
        print(f"//a[@href='#']: {equal_attr_a}")
