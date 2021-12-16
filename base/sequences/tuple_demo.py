import unittest
from collections import namedtuple

# tuple是不可变列表
class TupleDemo(unittest.TestCase):
    def test_base(self):
        """tuple定义和遍历"""
        # 使用()定义tuple
        tpe = ("a", "b", "c", "d")
        # 使用[]获取值
        print(f"0:{tpe[0]},1:{tpe[1]}")
        # 可以遍历
        for i in tpe:
            print(i)

    def test_unpacking(self):
        """元组拆包"""
        tpe = ("a", "b", "c")
        a, b, c = tpe
        print(f"a:{a},b:{b},c:{c}")
        # _占位符用来忽略不关注的值
        d, _, e = tpe
        print(f"d:{d},e:{e}")
        # 参数前加*可以获取元组剩余的元素
        *f, g = tpe
        print(f"f:{f},g:{g}")
        # 元组加*会拆包成函数的参数
        func_tuple(*tpe)

    def test_named_tuple(self):
        """命名的tuple"""
        # 返回一个有属性的类型
        Point = namedtuple("Point", ["x", "y", "z"])
        # 入参一定要给全所有属性
        p = Point("a", "b", "c")
        # 属性只能访问,不能修改
        print(f"point:{p},p.x:{p.x},p.y:{p.y},p.z:{p.z}")


def func_tuple(a, b, c):
    print(f"a:{a},b:{b},c:{c}")
