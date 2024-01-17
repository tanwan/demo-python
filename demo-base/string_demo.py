import unittest
import textwrap


class StringDemo(unittest.TestCase):
    def test_check(self):
        """
        判断
        not, (not) in, startswith, endswith
        count
        find
        isalpha,isalnum
        """
        str = "hello world"
        # not, in, startswith, endswith
        print(f"not:{not ''},in:{'hello' in str},startswith:{str.startswith('hello')}, endswith:{str.endswith('world')}")
        # 出现的次数
        print("count:", str.count("he"))
        # 查询index
        print("index:", str.find("o"))
        # isalpha, isalnum
        print(f"isalpha:{str.isalpha()},isalnum:{str.isalnum()}")

    def test_format(self):
        """
        字符串格式化
        format: {}作为占位符, 可以指定index, 比如{0}表示第1个参数
        f"": 会把字符串中的{}格式化为它的值
        {}: 是可以指定格式的, 比如{i:03d}: 格式化为3位数字,不够补0
        """
        print("format, {},{}".format("a", "b"))
        # 0表示第一个参数,1表示第二个参数
        print("format use index, {1},{0},{1}".format("a", "b"))
        a = "value a"
        b = "value b"
        # 会把字符串中的{}格式化为它的值
        print(f"format use variable, {a},{b}")
        # {}中还可以指定格式 03d表示3位数字,不够补0
        i = 1
        print(f"{i:03d}")
        print("{0:03d}".format(i))

    def test_multiline_string(self):
        """
        多行字符串
        textwrap.dedent: 去除多行字符串的缩进
        """
        str = """
        1234
        5678
        """
        # 没有去除缩进
        print("no dedent:", str)
        # 去除多行字符串的缩进
        print("dedent :", textwrap.dedent(str))

    def test_convert(self):
        """
        字符串转换
        upper|lower|capitalize
        strip|lstrip|rstrip: 去除左右|左|右的字符,默认去除空白字符
        ord(char) <-> chr(ascii): ASCII <-> char ASCII跟字符的转换
        str.encode <-> bytes.decode: str <-> bytes 字符串和字节数组的转换
        """
        # upper:大写,lower:小写,capitalize:首字母大写
        str = "hello World"
        print(f"upper:{str.upper()},lower:{str.lower()},capitalize:{str.capitalize()}")
        # 使用strip去除前后的字符
        print(f"strip:{' hello world '.strip()}, lstrip(a):{'aahello worldaa'.lstrip('a')}")

        # ord字符转ASCII, chrASILL转字符
        print(f"ord:{ord('a')},chr:{chr(97)}")

        # 字符串跟字节数组互转
        bytes = str.encode("utf-8")
        print(f"str to bytes:{bytes}")
        print(f"bytes to str:{bytes.decode('utf-8')}")

    def test_slice(self):
        """字符串的切片"""
        str = "hello world"
        print("slice:", str[:6])
        print("reverse:", str[::-1])
        print("char at:", str[3])
