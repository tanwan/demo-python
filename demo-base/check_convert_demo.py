import unittest
import math
import decimal


class CheckConvertDemo(unittest.TestCase):
    """校验和转换"""

    def test_check_float(self):
        """校验是否是float"""

        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        self.assertTrue(isfloat("-1.23"))
        self.assertTrue(isfloat("1"))
        self.assertFalse(isfloat("1xx"))

    def test_convert_thousands_format(self):
        """千分位格式的转换"""
        # 转为千分位格式
        print("{:,.2f}".format(12345.00, format_spec=","))
        # 千分位转浮点
        print(float("12,345.00".replace(",", "")))
