import unittest
import pinyin


class PinYinDemo(unittest.TestCase):
    def test_to_pinyin(self):
        """拼音"""
        # 默认带声调, 没有分隔
        print(pinyin.get("你好"))
        # strip不带声调, delimiter指定分隔
        print(pinyin.get("你好", format="strip", delimiter=" "))
        # 声调使用数字
        print(pinyin.get("你好", format="numerical", delimiter=" "))
        # 首字母拼音
        print(pinyin.get_initial("你好", delimiter=" "))
