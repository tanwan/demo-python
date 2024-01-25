from bs4 import BeautifulSoup
import unittest
import re
from pathlib import Path


class BeautifulSoupDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(Path(__file__).parent / ".file/simple.html") as file:
            # html.parser:python内置的解析器,lxml:解析速度快,需要install lxml
            cls.soup = BeautifulSoup(file.read(), features="lxml")

    def test_prettify(self):
        """格式化"""
        print(self.soup.prettify())

    def test_string_attr(self):
        """
        文档的值和属性
        soup.<tag>: 获取文档中首个tag标签
        tag.<tag>: 获取tag下首个tag标签
        tag.string: 节点的值
        tag.name: 节点的名称
        attrs: 节点的所有属性(dict)
        tag[attr]: 节点的属性
        """
        # 使用点取属性获取文档中第一个a标签
        tag_a = self.soup.a
        # tag也可以继续使用.获取下面的标签
        print(self.soup.head.title.string)

        # tag.string: 节点的值
        # tag.name:节点的名称
        print(tag_a, tag_a.name, tag_a.string)

        # tag[attr]:节点的属性
        # tag.attrs:节点所有的属性,就是个dict
        print(tag_a["href"], tag_a.attrs)

    def test_css_selector(self):
        """css选择器, 返回的是list"""
        # 使用css选择器查找
        tag_title = self.soup.select("title")
        self.assertTrue(isinstance(tag_title, list))
        print(tag_title)

        # 按css tag查找
        tag_body_a = self.soup.select("body a")
        print(tag_body_a)

        # 按css类名查找
        tag_div_class1 = self.soup.select(".div-class1")
        print(tag_div_class1)

    def test_tag_relationship(self):
        """
        tag的关系
        tag.parent: 父节点
        tag.parents: 节点的所有祖先节点, 返回生成器
        tag.next_sibling: 下一个兄弟节点
        find_next_sibling(tag): 下一个兄弟tag节点
        tag.previous_sibling:上一个兄弟节点
        tag.children: 节点的直接子节点, 返回生成器
        tag.contents: 节点的直接子节点列表
        """
        tag_title = self.soup.head.title
        # tag.parent: 获取父节点
        tag_title_parent = tag_title.parent
        print(tag_title_parent.name)

        # tag.parents: 节点的所有祖先节点, 返回生成器
        print([p.name for p in tag_title.parents])

        # tag.next_sibling:下一个兄弟节点,a的下一个兄弟节点是换行,再下一个兄弟节点才是第二个a
        # 可以使用tag.find_next_sibling指定tag标签
        # tag.previous_sibling:上一个兄弟节点
        print(self.soup.a.next_sibling.next_sibling)
        print(self.soup.a.find_next_sibling("a"))

        # tag.children: 节点的直接子节点生成器
        print([child.name for child in self.soup.body.div.children])

        # tag.contents: 节点的直接子节点列表
        print(self.soup.body.div.contents)

    def test_find_all(self):
        """
        查找
        find: 只返回一个元素
        find_all: 查找所有节点,返回list
        默认按节点名称查找,也可以指定kw来指定按其它的查找,class_(因为class是关键字):按class查找,string:按字符串查找
        """
        print(self.soup.find_all("a"))

        # 使用class
        print(self.soup.find_all(class_="div-class1"))

        # 可以使用正则
        print(self.soup.find_all(re.compile("butto.*")))

        # 可以传入列表
        print(self.soup.find_all(["a", "p"]))

        def find_all_fun(tag):
            return tag.has_attr("class") and not tag.has_attr("id")

        # 可以传入函数
        print(self.soup.find_all(find_all_fun))
