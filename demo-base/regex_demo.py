import unittest
import re


class RegexDemo(unittest.TestCase):
    def test_pattern(self):
        """
        Pattern对象
        re.compile可以创建出Pattern, re.match|search|findall|finditer也是生成Pattern对象
        用pattern对象和直接使用re的方法是等价的
        """
        # 使用compile生成一个Pattern对象
        pattern_str = r"te([x|s]t)"
        text = "test"
        pattern = re.compile(pattern_str)
        # 跟re.match(pattern_str, text)是等价的
        print(pattern.match(text))
        print(re.match(pattern_str, text))

    def test_match(self):
        """
        match: 判断字符串是否匹配正则表达式, 匹配返回的match object, 否则返回None
        跟search的区别: match用来判断字符串是否匹配正则, search用来在字符串中搜索匹配的子字符串
        """
        text = """This is the text used to test 
        the regex"""
        # r表示字符串为正则表达式
        # re.S:使.表示任意字符包括换行符,否则需要使用[\s\S], re.I:忽略大小写
        match_obj = re.match(r"(.*) Text (.*?) .* the", text, re.S | re.I)
        re.search
        if match_obj:
            # span获取符合正则的起始和结束位置
            print("matchObj.span():", match_obj.span())
            # 第0个捕获组, 也就是匹配的字符串
            print("matchObj.group():", match_obj.group())
            # 第一个捕获组和第二个捕获组
            print("matchObj.group(1):", match_obj.group(1), "matchObj.group(2):", match_obj.group(2))

    def test_findall(self):
        """
        findall: 从字符串中搜索出匹配正则表达式的所有子字符串, 返回list, 没有匹配的话, 返回空list
        list的元素取决于正则表达式捕获组的数量
        1. 没有捕获组: 匹配的字符串
        2. 一个捕获组: 捕获组的字符串
        3. 多个捕获组: 捕获组的字符串组成的元组
        """
        text = "This is the text used to test the regex"
        # ['text', 'test']
        print("non capturing group", re.findall(r"te[x|s]t", text))
        # ['xt', 'st']
        print("one capturing group", re.findall(r"te([x|s]t)", text))
        # [('te', 'xt'), ('te', 'st')]
        print("two capturing group", re.findall(r"(te)([x|s]t)", text))

    def test_finditer(self):
        """
        finditer: 从字符串中搜索出匹配正则表达式的所有子字符串, 返回match object的iterator
        """
        text = "This is the text used to test the regex"
        for match_obj in re.finditer(r"te([x|s]t)", text, re.M | re.I):
            print("match objec:", match_obj)

    def test_search(self):
        """
        search: 从字符串中搜索出匹配正则表达式的第一个字符串,返回它的match object,否则返回None
        跟finditer的区别: search只返回第一个match object, finditer返回所有的match object
        跟match的区别: search用来在字符串中搜索匹配的子字符串, match用来判断字符串是否匹配正则
        """
        text = "This is the text used to test the regex"
        match_obj = re.search(r"te([x|s]t)", text)
        # 字符串不匹配此正则, 但是它的子字符串有匹配的
        self.assertIsNone(re.match(r"te([x|s]t)", text))
        print("match_obj:", match_obj)

    def test_replace(self):
        """
        正则替换
        re.sub: 要替换的内容可以是字符串, 也可以是一个函数(方法的入参是匹配的对象,返回值是要替换的字符串)
        """
        text = "This is the text used to test the regex#用于正则替换"
        new_text = re.sub(r"#.*$", "^_^", text)
        print("replace:", new_text)

        # 替换的内容为函数
        new_text = re.sub(r"#.*$", replace_func, text)
        print("replace:", new_text)


def replace_func(matched):
    # 入参matched是正则匹配的对象
    print("matched:", matched)
    # 返回值是用来替换的字符串
    return "^_^"
