import unittest


class MagicMethodDemo(unittest.TestCase):
    def test_magic_method(self):
        """
        魔术方法
        ==: __eq__
        len: __len__
        [index]: __getitem__
        str: __str__
        +: __add__
        +=: __iadd__
        *: __mul__
        bool: __bool__
        iter: __iter__
        """
        obj = SimpleMagicMethod()
        other = SimpleMagicMethod()
        obj.test_values.append(1)
        other.test_values.append(10)

        self.assertFalse(obj == other)

        print("len:", len(obj))
        print("getitem:", obj[0])
        print("str:", obj)
        print("add:", obj + other)
        obj += other
        print("iadd:", obj)
        print("mul:", obj * 2)
        print("bool:", bool(obj))

        for i in obj:
            print(i)

    def test_equal(self):
        """
        判断相等
        ==判断相等
        is判断是否是同一个对象
        """

        a = SimpleMagicMethod()
        b = SimpleMagicMethod()
        # ==判断相等,调用__eq__方法
        self.assertTrue(a == b)
        # is判断是否是同一个对象
        self.assertFalse(a is b)


class SimpleMagicMethod:
    def __init__(self):
        self.test_values = []
        self.iter_start = -1

    """
    魔术方法是为了被python解释器调用
    使用__开头和__结尾
    """

    def __eq__(self, __o):
        """用来支持==判断相等的"""
        print("__eq__ exec")
        return self.test_values == __o.test_values

    def __len__(self):
        """用来支持len方法"""
        print("__len__ exec")
        return len(self.test_values)

    def __getitem__(self, index):
        """用来支持数组的大部分方法"""
        print("__getitem__ exec")
        return self.test_values[index]

    def __iter__(self):
        """用来支持迭代器"""
        print("__iter__ exec")
        return self

    def __next__(self):
        print("__next__ exec")
        self.iter_start += 1
        if len(self.test_values) > self.iter_start:
            return self.__getitem__(self.iter_start)
        raise StopIteration

    def __str__(self):
        """用来支持str"""
        print("__str__ exec")
        return f"SimpleMagicMethod:{self.test_values}"

    def __add__(self, other):
        """支持+"""
        print("__add__ exec")
        self.test_values += other.test_values
        return self

    def __iadd__(self, other):
        """支持+=,如果没有使用__iadd__,则会使用__add__"""
        print("__iadd__ exec")
        self.test_values += other.test_values
        return self

    def __mul__(self, other):
        """支持*"""
        print("__mul__ exec")
        self.test_values = [i * other for i in self.test_values]
        return self

    def __bool__(self):
        """支持判断"""
        print("__bool__ exec")
        return bool(self.test_values)
