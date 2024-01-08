import time
import unittest


class TimeDemo(unittest.TestCase):
    def test_convert(self):
        """时间转换"""

        pattern = "%Y-%m-%d %H:%M:%S"
        # time.time:秒级时间戳
        # time.localtime:时间戳转换为time.struct_time
        # time.strftime:time.struct_time转字符串
        time_str = time.strftime(pattern, time.localtime(time.time()))
        print(time_str)
        # time.strptime:字符串转time.struct_time
        # time.mktime:time.struct_time转时间戳
        print(time.mktime(time.strptime(time_str, pattern)))
