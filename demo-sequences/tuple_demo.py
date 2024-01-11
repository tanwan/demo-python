import unittest
from collections import namedtuple


# tuple是不可变列表
class TupleDemo(unittest.TestCase):
    def test_base(self):
        """tuple基本使用"""
        # 使用()定义tuple
        tpe = ("a", "b", "c", "d")

        # in: 判断是否在元组中
        self.assertTrue("a" in tpe)

        # 使用[]获取值
        self.assertEqual("a", tpe[0])

        # 可以遍历
        for i in tpe:
            print(i)

    def test_convert(self):
        """转换"""
        tpe = ("a", "b", "c", "d")
        # 转成list
        lst = list(tpe)
        print("to list:", lst)
        # 从list转成tuple
        tpe = tuple(lst)
        print("to tuple:", tpe)

    def test_unpacking(self):
        """元组拆包"""
        tpe = ("a", "b", "c", "d", "e")
        # _占位符用来忽略不关注的值, 加*的参数表示获取元组剩余的元素
        a, *rest, d, _ = tpe
        self.assertEqual("a", a)
        self.assertEqual("d", d)
        print("*c: ", rest)

        # 元组列表在遍历或者推导式中, 也可以进行拆包
        for a, *_ in [tpe]:
            print("a:", a)

        # 元组加*会拆包成函数的参数
        func_tuple(*tpe)

    def test_named_tuple(self):
        """命名的tuple"""
        # 返回一个有x,y,x属性的类型
        Point = namedtuple("Point", ["x", "y", "z"])
        # 入参需要给所有属性赋值
        p = Point("a", "b", "c")
        # 属性只能访问,不能修改
        self.assertEqual("a", p.x)
        self.assertEqual("b", p.y)
        self.assertEqual("c", p.z)

    def test_slice(self):
        """元组切片"""
        tpe = ("a", "b", "c", "d")
        print("slice:", tpe[1:3])


def func_tuple(a, b, c, d, e):
    print(f"a:{a},b:{b},c:{c},d:{d},e:{e}")
