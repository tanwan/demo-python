import copy
import unittest
import functools
import logging
from pathlib import Path

# python执行到import的时候,就会打开import的文件,然后将函数/类复制到这个程序中
# 当使用unitest模板的函数/类时, 使用unittest. 如果给模块添加了别名import unitest as test,则使用test.即可
# 可以使用from module_name import *,这样在使用的时候就不需要使用模块名的前缀了
# 也可以导入特定的方法/类 from module_name import func, 这样就可以使用func()了, 还可以添加别名from module_name import func as f, 就可以使用f()

curdir = Path(__file__).parent


class FunctionDemo(unittest.TestCase):
    def test_function(self):
        """测试函数"""
        # 函数中的第一个"""注释就是这个函数的doc
        print(func_no_arg.__doc__)
        func_no_arg()
        func_with_arg("arg1 value", "arg2 value")
        # 可以通过指定参数名传参
        func_with_arg(arg2="arg2 value", arg1="arg1 value")
        # 默认参数可以不传
        func_with_default_arg("arg value")
        # 默认参数传参可以覆盖默认值
        func_with_default_arg("arg value", "default value override")
        # 传任意参数,不能传关键字入参(入参指定参数名)
        func_with_any_arg("arg1 value", "arg2 value", 3)
        # 传入非关键字入参(入参不指定参数名)和关键字入参(入参指定参数名)
        func_args_keyword("arg1 value", "arg2 value", 3, k1="k1 value", k2=2)

    def test_function_annotation(self):
        """测试方法注解"""
        func_annnotation(1, -1)

    def test_dispatch(self):
        """分派"""
        func_obj("str")


class BaseDemo(unittest.TestCase):
    def test_global_var(self):
        """测试global"""
        func_global()
        # 非global的变量,python会在此作用域下,使用global的值创建一个同名的局部变量,此变量跟全局变量是两个变量
        no_use_global_var = "no_use_global_var override"
        # global的变量,就是跟全局的变量是同一个
        global global_var
        global_var = "global_var override"
        func_global()

    def test_non_local(self):
        """测试non_local"""
        non_local_var = "non_local_var"

        def inner_fun():
            # 表示此变量不是局部变量,也不是全局变量,用来修改外层函数的变量
            nonlocal non_local_var
            non_local_var = "non_local_var override"

        inner_fun()
        print(f"non_local_var:{non_local_var}")

    def test_exception(self):
        """测试异常"""
        func_exception(True)
        func_exception(False)

    def test_equal(self):
        class EqualClass:
            def __init__(self, value):
                self.value = value

            def __eq__(self, __o):
                print("__eq__")
                return self.value == __o.value

        a = EqualClass("value")
        b = EqualClass("value")
        # ==判断相等,调用__eq__方法
        self.assertTrue(a == b)
        # is判断是否是同一个对象
        self.assertFalse(a is b)

    def test_type(self):
        # isinstance判断是否属于指定类型
        print(f"isinstance:{isinstance(1,int)}")
        print(f"type is int {type(1) is int}")

    def test_with(self):
        """
        1. expression被执行得到返回值
        2. 调用返回值的__enter__方法
        3. __enter__的返回值赋值给target
        4. 执行with块
        5. 调用expression返回值的__exit__方法
        """
        with SimpleWith("without exception") as sw:
            print("do within without exception")
        with SimpleWith("with exception") as sw:
            print("do within with exceptioin")
            raise Exception
        # 如果__exit__返回False,则还会再抛出异常
        try:
            with SimpleWith("with exception exit False", False) as sw:
                print("do within with exceptioin exit False")
                raise Exception
        except BaseException:
            print("handle exception")

    def test_copy(self):
        """深复制和浅复制"""
        lst = [SimpleCopy("value")]
        # 浅复制
        shallow_copy = copy.copy(lst)
        shallow_copy[0].value = "simple_copy value"
        print(f"shallow copy:{lst[0].value}")

        # 深复制
        lst = [SimpleCopy("value")]
        deep_copy = copy.deepcopy(lst)
        deep_copy[0].value = "deep_copy value"
        print(f"deep copy:{lst[0].value}")

    def test_approximate(self):
        """近似"""
        # round(num[,n]):四舍五入,n表示小数位
        print(f"round:{round(1.336,2)}")
        # 格式化保留两位小数
        print("{:.2f}".format(321.33645))


class LoggerDemo(unittest.TestCase):
    def test_logging(self):
        """日志"""
        tmp_dir = curdir / ".file/tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        formatter = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(
            filename=curdir / ".file/tmp/log.log", level=logging.DEBUG, format=formatter
        )
        logger = logging.getLogger()
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(formatter))
        # 如果配置的是写入到文件的,默认不会输出到控制台,因此需要添加一个StreamHandler,把日志输入到控制台
        logger.addHandler(ch)
        logger.debug("test_logging message")


def func_no_arg():
    """不带参数"""
    print("func_no_arg")


def func_with_arg(arg1, arg2):
    """带参数"""
    print(f"func_with_arg, arg1:{arg1},arg2:{arg2}")


def func_with_default_arg(arg1, default_arg="default value"):
    """带默认参数"""
    print(f"func_with_default_arg, arg1:{arg1},default_arg:{default_arg}")


def func_with_any_arg(*args):
    """*args可以传任意参数,args是个tuple"""
    print(f"func_with_any_arg, args type:{type(args)}, args:{args}")


def func_args_keyword(*args, **kw):
    """带args和kw,args接受非关键字参数(入参不指定参数名),kw接收关键字参数(入参指定参数名),args是tuple,kw是dict"""
    print(f"func_args_keyword, args type:{type(args)},args:{args},kw type:{type(kw)},kw:{kw}")


def func_annnotation(a: str, b: "int>0" = 10) -> str:
    """函数注解,只是对函数的入参和返回作出提示信息,对python解释器没有意义"""
    print(f"func_annnotation, a:{a},b:{b}")
    return "func_annnotation"


no_use_global_var = "no_use_global_var"
global_var = "global_var"


def func_global():
    print(f"no_use_global_var:{no_use_global_var},global_var:{global_var}")


def func_exception(raise_exp):
    try:
        if raise_exp:
            raise Exception
    except BaseException:
        # BaseException所有异常的父类
        print("catch exception")
    else:
        print("run success")


class SimpleWith(object):
    """
    必须有__enter__,__exit__方法
    简化try except finally
    """

    def __init__(self, param, raise_expection=True):
        self._param = param
        self._raise_expection = raise_expection
        print(f"with __init__,param:{param}")

    def __enter__(self):
        print("with __enter__")
        return self._param

    def __exit__(self, exc_type, exc_value, exc_trackback):
        """
        __exit__一定会执行
        """
        print(f"with __exit__,exc_type:{exc_type}, exc_value:{exc_value},exc_trackback:{exc_trackback}")
        if exc_trackback is None:
            print("exec success")
        else:
            print("exec expection")
        # 返回True,则直接忽略异常
        # 返回False重新抛出异常
        return self._raise_expection


class SimpleCopy:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


# python不支持多态,使用这个可以相当于实现多态
@functools.singledispatch
def func_obj(obj):
    print(f"func:{obj}")


# func的入参数据为str类型,将调用此函数
@func_obj.register(str)
def func_str(obj):
    print(f"func_str:{obj}")
