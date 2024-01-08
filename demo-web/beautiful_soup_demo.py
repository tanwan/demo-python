from bs4 import BeautifulSoup
import unittest
import re
from pathlib import Path


class BeautifulSoupDemo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """setUpClass: beforeClass,需要使用@classmethod,setUp:beforeEach"""
        with open(Path(__file__).parent / ".file/simple.html") as file:
            # html.parser:python内置的解析器,lxml:解析速度快,需要install lxml
            self.soup = BeautifulSoup(file.read(), features="lxml")

    def test_prettify(self):
        """格式化"""
        print(self.soup.prettify())

    def test_string_attr(self):
        """文档的值和属性"""
        soup = self.soup
        # 使用点取属性获取文档中第一个a标签
        tag_a = soup.a
        # tag.string: 节点的值
        # tag.name:节点的名称
        print(f"tag_a:{tag_a}, string:{tag_a.string}, name:{tag_a.name}")
        # tag[attribute_name]:节点的属性
        # tag.attrs:节点所有的属性,就是个dict
        print(f"single attribute:{tag_a['href']},all attributes:{tag_a.attrs}")
        # input也使用属性获取值
        print(f"input:{soup.select('#input-text')[0]['value']}")
        # 可以连续使用点取属性(获得的都是首次出现的节点)
        tag_title = soup.head.title
        print(f"tag_title:{tag_title.string}")

    def test_css_selector(self):
        soup = self.soup
        """css选择器"""
        # 使用css选择器查找
        tag_title = soup.select("title")
        print(f"tag_title:{tag_title}")

        tag_body_a = soup.select("body a")
        for a in tag_body_a:
            # tag[attribute_name]: 获取属性的值, string:获取标签的值
            print(f"a href:${a['href']},a text:${a.string}")

        # 按css类名查找
        tag_div_class1 = soup.select(".div-class1")
        print(f"tag_class:{tag_div_class1}")

    def test_tag_relationship(self):
        """tag的关系"""
        soup = self.soup
        tag_title = soup.head.title
        # tag.parent: 获取父节点
        tag_title_parent = tag_title.parent
        print(f"tag_title's parent:{tag_title_parent.name}")
        # tag.parents:递归节点的父节点
        for parent in tag_title.parents:
            print(f"parents:{parent.name}")

        tag_a = soup.a
        # tag.next_sibling:下一个兄弟节点,a的下一个兄弟节点的逗号和换行,再下一个兄弟节点才是第二个a
        # tag.previous_sibling:上一个兄弟节点
        tag_a_next_sibling = tag_a.next_sibling.next_sibling
        print(f"tag_a_next_sibling:{tag_a_next_sibling}")

        # tag.contents: 节点的直接子节点列表
        print(f"body contents:{soup.body.div.contents}")
        # tag.children: 节点的直接子节点生成器
        for child in soup.body.children:
            print(f"children:{child.name}")

    def test_find_all(self):
        """查找"""
        soup = self.soup
        # find_all:查找所有节点,默认按节点名称查找
        # 也可以指定kw来指定按其它的查找,class_(因为class是关键字):按class查找,string:按字符串查找
        # find: 跟find_all不一样的是,find只返回一个结果
        all_tag_a = soup.find_all("a")
        print(f"all tag a:{all_tag_a}")
        # 可以使用正则
        all_tag_button = soup.find_all(re.compile("butto.*"))
        print(f"all tag button:{all_tag_button}")
        # 可以传入列表
        all_tag_list = soup.find_all(["a", "p"])
        print(f"all tag list:{all_tag_list}")
        # 可以传入函数
        all_tag_func = soup.find_all(find_all_fun)
        print(f"all tag func:{all_tag_func}")


def find_all_fun(tag):
    return tag.has_attr("class") and not tag.has_attr("id")
