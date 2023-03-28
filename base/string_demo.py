import unittest
import textwrap
import re


class StringDemo(unittest.TestCase):
    def test_check(self):
        """判断"""
        str = "hello World"
        # not, in, startswith
        print(f"not:{not ''},in:{'hello' in str},startswith:{str.startswith('hello')}")
        # 出现的次数
        print(f"count:{str.count('he')}")

    def test_format(self):
        """字符串格式化"""
        print("format, {},{}".format("a", "b"))
        # 0表示第一个参数,1表示第二个参数
        print("format use index, {1},{0},{1}".format("a", "b"))
        a = "value a"
        b = "value b"
        # 使用f可以使用字面量格式化字符串
        print(f"format use variable, {a},{b}")
        # {}中还可以指定格式 03d表示3位数字,不够补0
        i = 1
        print(f"{i:03d}")
        print("{0:03d}".format(i))

        str = """
        1234
        5678
        """
        # 没有去除缩进
        print(f"no dedent:{str}")
        # 去除多行字符串的缩进
        print(f"dedent{textwrap.dedent(str)}")

    def test_convert(self):
        """字符串转换"""
        # upper:大写,lower:小写,capitalize:首字母大写
        str = "hello World"
        print(f"upper:{str.upper()},lower:{str.lower()},capitalize:{str.capitalize()}")
        # 使用strip去除前后的字符
        print(f"strip:{' hello world '.strip()}, strip(a):{'aahello worldaa'.strip('a')}")

        # ord字符转ASCII, chrASILL转字符
        print(f"ord:{ord('a')},chr:{chr(97)}")

        # 字符串跟字节数组互转
        bytes = str.encode("utf-8")
        print(f"str to bytes:{bytes}")
        print(f"bytes to str:{bytes.decode('utf-8')}")

    def test_slice(self):
        """字符串也可以使用slice"""
        str = "hello world"
        print(f"slice:{str[:6]}")
        print(f"reverse:{str[::-1]}")

        print(f"char at:{str[3]}")

    def test_regex_match(self):
        """
        正则表达式
        compile: 生成一个Pattern对象
        match: 判断给定字符串需要符合正则表达式,成功返回匹配对象,否则返回None
        search: 搜索一个符合正则表达式的子字符串,成功返回第一个匹配的对象,否则返回None
        findall: 搜索所有符合正则表达式的子字符串,成功返回匹配的捕获组列表,否则返回空列表
        finditer: 搜索所有符合正则表达式的子字符串,成功返回匹配的对象的iteror
        """
        str = "This is the text used to test the regex"
        # r表示字符串是个正则表达式,re.M:多行匹配,re.I:忽略大小写
        match_obj = re.match(r"(.*) text (.*?) .*", str, re.M | re.I)
        if match_obj:
            print(f"matchObj.span():{match_obj.span()}")
            print(f"matchObj.group():{match_obj.group()}")
            print(f"matchObj.group(1):{match_obj.group(1)}")
            print(f"matchObj.group(2):{match_obj.group(2)}")
        # 使用compile生成一个Pattern对象,re.match|search|findall|finditer其实也是先生成Pattern对象
        pattern = re.compile(r"te([x|s]t)")
        # match要求字符串要匹配正则
        match_obj = pattern.match(str, re.M | re.I)
        print(f"match:{match_obj}")
        # 在字符串中搜索一个符合正则的子字符串
        search_obj = pattern.search(str, re.M | re.I)
        print(f"search:{search_obj.group()},group(1):{search_obj.group(1)}")
        # 在字符串中搜索所有符合正则的子字符串
        # 如果正则没有捕获组,则结果返回匹配的子字符串,如果正则有捕获组,则结果只有捕获组
        findall_obj = pattern.findall(str, re.M | re.I)
        print(f"findall:{findall_obj}")
        # 在字符串中搜索所有符合正则的子字符串
        for finditer_obj in pattern.finditer(str, re.M | re.I):
            print(f"finditer:{finditer_obj.group()},group(1):{finditer_obj.group(1)}")

    def test_regex_replace(self):
        """使用sub进行正则替换"""
        str = "This is the text used to test the regex#用于正则替换"
        new_str = re.sub(r"#.*$", "^_^", str)
        print(f"replace:{new_str}")
        # repl可以是一个函数, 入参为匹配的对象
        new_str = re.sub(r"#.*$", replace_func, str)
        print(f"replace:{new_str}")


def replace_func(matched):
    print(f"matched:{matched}")
    return "^_^"
