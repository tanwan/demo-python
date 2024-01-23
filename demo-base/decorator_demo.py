import functools
import unittest
import os
import socket


class DecoratorTest(unittest.TestCase):
    def test_decorator(self):
        """装饰器, 原理就是使用高阶函数来实现aop的功能, 入参为函数, 出参也是函数"""
        # without_wraps_func的方法名被修改了
        self.assertEqual("internal_decorator", without_wraps_func.__name__)
        self.assertEqual("with_wraps_func", with_wraps_func.__name__)
        without_wraps_func("var1", "var2")
        with_wraps_func("var1", "var2")

    def test_decorator_with_param(self):
        """装饰器可以带参数"""
        with_param_func("var1", "var2")

    def test_multi_decorator(self):
        """多个装饰器"""
        with_multi_decorator_func("var1", "var2")


need_print = None


def print_for_decorator(msg):
    # 由于python.testing.unittestArgs测试文件的匹配规则使用的是*.py, 所以所有的py文件都会被unittest执行一遍
    # 而装饰器的本质其实就是一个入参为函数的函数, 所以当它被装饰到目标函数上时, 他就被执行了
    # 这就会导致在执行其它测试时, 这个测试文件的装饰器的print也会被执行
    # 所以这边定义这个方法, 只有在执行此文件的测试时,才会进行print
    global need_print
    if need_print == None:
        # 参数ms-python的unittestadapter/execution.py来获取执行的测试方法
        port_str = os.environ.get("RUN_TEST_IDS_PORT")
        if not port_str:
            return
        run_test_ids_port = int(port_str)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", run_test_ids_port))
        data = client_socket.recv(1024 * 1024)
        need_print = "decorator_demo" in str(data)
    if need_print:
        print(msg)


def decorator_without_wraps(func):
    """不带参数的装饰器的入参就是要装饰的函数"""
    print_for_decorator("decorator_without_wraps exec")

    # 这边没有@functools.wraps,所以使用decorator_without_wraps注解的函数的函数名和属性会被修改为internal_decorator
    def internal_decorator(*args, **kw):
        print("decorator_without_wraps internal_decorator exec before")
        # 真正执行的函数
        func(*args, **kw)
        print("decorator_without_wraps internal_decorator exec after")

    return internal_decorator


# 一遇到注解,就会直接先执行装饰器的方法,这边会直接执行decorator_without_wraps(without_wraps_func)
@decorator_without_wraps
def without_wraps_func(a, b):
    """相当于执行decorator_without_wraps(without_wraps_func)(a,b)"""
    print("real func without_wraps_func exec:", a, b)


def decorator_with_wraps(func):
    print_for_decorator("decorator_with_wraps exec")

    # @functools.wraps用来保留原来函数的函数名和属性
    @functools.wraps(func)
    def internal_decorator(*args, **kw):
        print("decorator_with_wraps internal_decorator exec before")
        # 真正执行的函数
        func(*args, **kw)
        print("decorator_with_wraps internal_decorator exec after")

    return internal_decorator


# 一遇到注解,就会直接先执行装饰器的方法,这边会直接执行decorator_with_wraps(with_wraps_func)
@decorator_with_wraps
def with_wraps_func(a, b):
    """相当于执行decorator_with_wraps(with_wraps_func)(a,b)"""
    print("real func with_wraps_func exec:", a, b)


def decorator_with_param(**kw):
    """
    带参数的装饰器的入参就是装饰器的参数, 这边使用了**kw,也可以直接使用参数名
    然后要定义一个入参为要装饰的函数的方法
    """
    print_for_decorator("decorator_with_param exec")

    # 这一层函数用来包装真正的函数
    def internal_decorator_func(func):
        print_for_decorator("decorator_with_param internal_decorator_attr exec")
        param1 = kw["param1"]
        param2 = kw["param2"]

        @functools.wraps(func)
        def internal_decorator(*args, **kw):
            print("decorator_with_param internal_decorator exec before:", param1, param2)
            # 真正执行的函数
            func(*args, **kw)
            print("decorator_with_param internal_decorator exec after")

        return internal_decorator

    return internal_decorator_func


# 一遇到注解,就会直接先执行装饰器的方法,这边会直接执行decorator_with_param(param1="param1 value", param2="param2 value")(with_param_func)
@decorator_with_param(param1="param1 value", param2="param2 value")
def with_param_func(a, b):
    """
    相当于decorator_with_param(param1="param1 value", param2="param2 value")(with_param_func)(a,b)
    """
    print("real func with_param_func exec:", a, b)


# 一遇到注解,就会直接先执行装饰器的方法,这边会直接执行decorator_with_wraps(decorator_with_param(param1="param1 value", param2="param2 value")(with_multi_decorator_func))
@decorator_with_wraps
@decorator_with_param(param1="param1 value", param2="param2 value")
def with_multi_decorator_func(a, b):
    """
    存在多个装饰器时, 上面的装饰器就是在外层, 下面的装饰器在里层
    decorator_with_wraps(decorator_with_param(param1="param1 value", param2="param2 value")(with_multi_decorator_func))
    所以在进行函数包装的时候, 是先执行里层的装饰器, 将返回的函数再传给外层的装饰器进行处理
    包装后的函数在执行的时候, 就会先执行外层装饰器返回的函数, 再执行里层装饰器返回的函数
    """
    print("real func with_multi_decorator_func exec:", a, b)
