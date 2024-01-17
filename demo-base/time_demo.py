import time
import datetime
import unittest


class TimeDemo(unittest.TestCase):
    def test_datetime(self):
        """
        datetime/date/time
        datetime.now: 当前日期时间
        datetime.datetime/date/time (year,month,day,hour,minite,second,microsecond): 指定日期时间生成datetime
        """
        d = datetime.datetime.now()
        # 可以获取到相应的年月日时分秒毫秒
        print(d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond)
        # 指定日期时间, 时分秒可以省略,支持时区
        print(datetime.datetime(2024, 1, 2, 3, 4, 5))

    def test_struct_time(self):
        """struct_time"""
        # 将秒级时间戳转为struct_time, 默认参数为当时时间戳
        st = time.localtime(time.time())
        print(st.tm_year, st.tm_mon, st.tm_yday, st.tm_mday, st.tm_wday, st.tm_hour, st.tm_min, st.tm_sec)

    def test_convert_between_str(self):
        """
        时间跟字符串的转换
        strftime: 将datetime/struct_time转为字符串
        strptime: 将字符串转为datetime/struct_time
        """
        # Y: 4位年份(带世纪), y: 2位年份(不带世纪)
        pattern = "%Y-%m-%d %H:%M:%S"
        # datetime转字符串
        print(datetime.datetime.now().strftime(pattern))
        # struct_time转字符串
        print(time.strftime(pattern, time.localtime(time.time())))

        str = "2024-01-01 00:11:22"
        # 字符串转datetime
        print(datetime.datetime.strptime(str, pattern))
        # 字符串转struct_time
        print(time.strptime(str, pattern))

    def test_compute(self):
        """
        时间计算
        datetime +/- timedelta(days, hours, minutes, seconds, weeks): 时间的加减
        replace: 时间字段的替换
        """
        d = datetime.datetime(2024, 1, 1)
        # 使用datetime +/- timedelta
        print(d - datetime.timedelta(days=3, hours=2))

        # 使用replace可以替换datetime
        print(d.replace(month=2))

    def test_convert(self):
        """
        时间类型之间的转换
        时间戳 <-> datetime: datetime.fromtimestamp <-> datetime.fromtimestamp
        时间戳 <-> struct_time: time.localtime <->
        """
        # 时间戳 -> datetime, 支持时区
        print(datetime.datetime.fromtimestamp(time.time()))
        # datetime -> 时间戳
        print(datetime.datetime.now().timestamp())

        # 时间戳 -> struct_time
        print(time.localtime(time.time()))
        # struct_time > 时间戳
        print(time.mktime(time.localtime()))
