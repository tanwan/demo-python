import functools
import unittest


class DecoratorTest(unittest.TestCase):
    def test_decorator(self):
        print(simple_without_wraps_func.__name__)
        print(simple_with_wraps_func.__name__)
        # simple_without_wraps_func的方法名被修改了
        self.assertEqual(simple_without_wraps_func.__name__, "internal_decorator")
        self.assertEqual(simple_with_wraps_func.__name__, "simple_with_wraps_func")
        simple_without_wraps_func("var1", "var2")
        simple_with_wraps_func("var1", "var2")

    def test_decorator_with_attr(self):
        simple_with_attr_func("var1", "var2")

    def test_multi_decorator(self):
        simple_with_multi_decorator_func("var1", "var2")


def decorator_without_wraps(func):
    print("decorator_without_wraps exec")
    # 这边没有@functools.wraps,所以使用decorator_without_wraps注解的函数的函数名和属性会被修改
    def internal_decorator(*args, **kw):
        print("decorator_without_wraps internal_decorator exec before")
        # 真正执行的函数
        func(*args, **kw)
        print("decorator_without_wraps internal_decorator exec after")

    return internal_decorator


def decorator_with_wraps(func):
    print("decorator_with_wraps exec")
    # @functools.wraps用来保留原来函数的函数名和属性
    @functools.wraps(func)
    def internal_decorator(*args, **kw):
        print("decorator_with_wraps internal_decorator exec before")
        # 真正执行的函数
        func(*args, **kw)
        print("decorator_with_wraps internal_decorator exec after")

    return internal_decorator


def decorator_with_attr(**kw):
    """这边使用了**kw,也可以直接使用参数名"""
    print("decorator_with_attr exec")
    # 这一层函数用来获取注解的属性
    def internal_decorator_attr(func):
        print("decorator_with_attr internal_decorator_attr exec")
        attr1 = kw["attr1"]
        attr2 = kw["attr2"]

        # 这一层函数用来获取函数的参数
        @functools.wraps(func)
        def internal_decorator(*args, **kw):
            print(f"decorator_with_attr internal_decorator exec before: attr1:{attr1},attr2:{attr2}")
            # 真正执行的函数
            func(*args, **kw)
            print("decorator_with_attr internal_decorator exec after")

        return internal_decorator

    return internal_decorator_attr


# 一遇到注解,就会直接先执行注解,这边会直接执行decorator_without_wraps(simple_without_wraps_func)
@decorator_without_wraps
def simple_without_wraps_func(a, b):
    """相当于执行decorator_without_wraps(simple_without_wraps_func)(a,b)"""
    print(f"simple_without_wraps_func exec,a:{a},b:{b}")


# 一遇到注解,就会直接先执行注解,这边会直接执行decorator_with_wraps(simple_with_wraps_func)
@decorator_with_wraps
def simple_with_wraps_func(a, b):
    """相当于执行decorator_with_wraps(simple_with_wraps_func)(a,b)"""
    print(f"simple_with_wraps_func exec,a:{a},b:{b}")


# 一遇到注解,就会直接先执行注解,这边会直接执行decorator_with_attr(attr1="attr1 value", attr2="attr2 value")(simple_with_attr_func)
@decorator_with_attr(attr1="attr1 value", attr2="attr2 value")
def simple_with_attr_func(a, b):
    """
    相当于decorator_with_attr(attr1="attr1 value", attr2="attr2 value")(simple_with_attr_func)(a,b)
    """
    print(f"simple_with_attr_func exec,a:{a},b:{b}")


# 一遇到注解,就会直接先执行注解,这边会直接执行decorator_with_wraps(decorator_with_attr(attr1="attr1 value", attr2="attr2 value")(simple_with_multi_decorator_func))
@decorator_with_wraps
@decorator_with_attr(attr1="attr1 value", attr2="attr2 value")
def simple_with_multi_decorator_func(a, b):
    """
    存在多个装饰器时,处理注解的时候是从下往上处理的,相当于decorator_with_wraps(decorator_with_attr(attr1="attr1 value", attr2="attr2 value")(simple_with_multi_decorator_func))
    也就是先运行decorator_with_attr再运行相当于decorator_with_wraps,而在执行函数的时候,则是从上往下执行的,先执行decorator_with_wraps返回的函数,再执行decorator_with_attr返回的函数
    这边就相当于decorator_with_wraps(decorator_with_attr(attr1="attr1 value", attr2="attr2 value")(simple_with_multi_decorator_func))(a,b)
    """
    print(f"simple_with_multi_decorator_func exec,a:{a},b:{b}")
