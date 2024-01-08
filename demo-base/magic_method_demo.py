import unittest


class MagicMethodDemo(unittest.TestCase):
    def test_magic_method(self):
        """魔术方法"""
        simple_magic_method = SimpleMagicMethod()
        other = SimpleMagicMethod()
        simple_magic_method.value.append(1)
        other.value.append(10)
        print(f"len: {len(simple_magic_method)}")
        print(f"getitem: {simple_magic_method[0]}")
        print(f"str: {simple_magic_method}")
        print(f"add: {simple_magic_method + other}")
        simple_magic_method += other
        print(f"iadd: {simple_magic_method}")
        print(f"mul: {simple_magic_method*2}")
        print(f"bool: {bool(simple_magic_method)}")

        for i in simple_magic_method:
            print(i)


class SimpleMagicMethod:
    def __init__(self):
        self.value = []
        self.start = -1

    """
    魔术方法是为了被python解释器调用
    使用__开头和__结尾
    """

    def __len__(self):
        """用来支持len方法"""
        print("__len__ exec")
        return len(self.value)

    def __getitem__(self, index):
        """用来支持数组的大部分方法"""
        print("__getitem__ exec")
        return self.value[index]

    def __iter__(self):
        """用来支持迭代器"""
        print("__iter__ exec")
        return self

    def __next__(self):
        print("__next__ exec")
        self.start += 1
        if len(self.value) > self.start:
            return self.__getitem__(self.start)
        raise StopIteration

    def __str__(self):
        """用来支持str"""
        print("__str__ exec")
        return f"SimpleMagicMethod:{self.value}"

    def __add__(self, other):
        """支持+"""
        print("__add__ exec")
        self.value += other.value
        return self

    def __iadd__(self, other):
        """支持+=,如果没有使用__iadd__,则会使用__add__"""
        print("__iadd__ exec")
        self.value += other.value
        return self

    def __mul__(self, other):
        """支持*"""
        print("__mul__ exec")
        self.value = [i * other for i in self.value]
        return self

    def __bool__(self):
        """支持判断"""
        print("__bool__ exec")
        return bool(self.value)
