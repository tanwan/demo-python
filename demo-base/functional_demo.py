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

    def test_operator(self):
        """使用operator来减少一些常用的lambda表达式"""
        # 使用add
        reduce_result = functools.reduce(operator.add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(f"reduce add:{reduce_result}")

        # 使用mul
        # partial相当于是给func给了默认参数,mul本来需要2个参数,被partial包装后的函数,只需要1个参数
        map_list = [i for i in map(functools.partial(operator.mul, 2), [1, 2, 3])]
        print(f"map mul:{map_list}")

        # operator.itemgetter返回一个函数
        # itemgetter(1)相当于lambda x:x[1]
        # itemgetter(1,2)相当于lambda x:(x[1],x[2])
        lst = [(1, "b"), (2, "a")]
        lst.sort(key=operator.itemgetter(1))
        print(f"use itemgetter sort:{lst}")

        # operator.attrgetter返回一个函数
        # attrgetter("k1")相当于lambda x:x["k1"]
        # attrgetter("k1","k2")相当于lambda x:(x["k1"],x["k2"])
        Simple = namedtuple("Simple", ["k1", "k2"])
        lst = [Simple(1, "b"), Simple(2, "a")]
        lst.sort(key = operator.attrgetter("k2"))
        print(f"use attrgetter sort:{lst}")
