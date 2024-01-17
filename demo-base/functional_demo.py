import unittest
import functools
import operator
from collections import namedtuple


class FunctionalDemo(unittest.TestCase):
    def test_lambda(self):
        """lambda只能是纯表达式,不能赋值,不能使用while和try等语句"""
        simple_lambda = lambda a, b: a + b
        print(simple_lambda(1, 2))

    def test_map(self):
        """使用map,这个可以使用推导替代"""
        for i in map(lambda x: x * 2, [1, 2, 3]):
            print(i)

    def test_reduce(self):
        """使用reduce"""
        # 初始值默认为list的第一个元素,也可以通过initial指定
        print(functools.reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_partial(self):
        """partial可以为lambda给定默认参数,然后生成新的lambda"""
        three_param = lambda a, b, c: a + b + c
        # 默认参数1,2
        partial = functools.partial(three_param, 1, 2)
        print(partial(3))
        # 默认参数2
        print(functools.partial(operator.mul, 2)(3))

    def test_operator(self):
        """
        使用operator来减少一些常用的lambda表达式
        operator提供了一些简单的运算, 比如add|mul|pow
        operator.itemgetter(k): lambda x: x[k], 可以用在元组列表的排序
        operator.attrgetter(attr) : lambda x:x.attr, 可以用在类列表的排序
        """
        # 使用add
        print("reduce add:", functools.reduce(operator.add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

        # operator.itemgetter, 相当于tuple/list的第二个元素
        print(operator.itemgetter(1)((1, 2, 3)))

        # operator.attrgetter, 相当于obj.attr
        print(operator.attrgetter("attr")(AttrClass("value")))


class AttrClass:
    def __init__(self, attr):
        self._attr = attr

    @property
    def attr(self):
        return self._attr
