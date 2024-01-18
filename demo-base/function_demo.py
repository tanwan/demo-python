import unittest
import functools


class FunctionDemo(unittest.TestCase):
    def test_function_declare(self):
        """
        测试函数定义
        函数中的第一个三引号的注释就是这个函数的doc, 可以通过function_name.__doc__获取
        指定参数名传参
        默认参数
        *args: 接收所有的非关键字入参的参数(入参不指定参数名), 是tuple
        **kw: 接收所有关键字参数(入参指定参数名), 是dict
        """

        # 无参函数
        def func_no_arg():
            print("func_no_arg")

        func_no_arg()

        # 带参函数
        def func_with_arg(arg1, arg2):
            print("func_with_arg: ", arg1, arg2)

        func_with_arg("arg1 value", "arg2 value")
        # 可以通过指定参数名传参
        func_with_arg(arg2="arg2 value", arg1="arg1 value")

        # 默认参数
        def func_with_default_arg(arg1, default_arg="default value"):
            print("func_with_default_arg: ", arg1, default_arg)

        func_with_default_arg("arg value")
        func_with_default_arg("arg value", "default value override")

        # args(tuple)接收所有非关键字参数(入参不指定参数名),kw(dict)接收所有关键字参数(入参指定参数名)
        def func_args_keyword(*args, **kw):
            print(f"func_args_keyword", args, kw)

        func_args_keyword("arg1 value", "arg2 value", 3, k1="k1 value", k2=2)

    def test_global_var(self):
        """
        测试global
        global的变量: 跟全局的变量是同一个
        非global的变量: python会在此作用域下,使用global的值创建一个同名的局部变量,此变量跟全局变量是两个变量
        """
        self.assertEqual("no_use_global_var", func_global()[0])
        self.assertEqual("global_var", func_global()[1])

        # 修改非global的变量和global的变量, no_use_global_var跟全局的no_use_global_var是两个变量, global_var是同一个变量
        no_use_global_var = "no_use_global_var override"
        global global_var
        global_var = "global_var override"

        # 全局变量的值会被修改, 非全局变量的值不会被修改
        self.assertEqual("no_use_global_var", func_global()[0])
        self.assertEqual("global_var override", func_global()[1])

    def test_function_annotation(self):
        """测试方法注解"""

        # 函数注解,只是对函数的入参和返回作出提示信息,对python解释器没有意义
        def func_annnotation(a: str, b: "int>0" = 10) -> str:
            print("func_annnotation", a, b)
            return "func_annnotation"

        func_annnotation(1, -1)

    def test_unpacking(self):
        """list和tuple可以拆包当做函数的参数"""

        tpe = (1, 2)
        lst = list(tpe)

        def unpacking(a, b):
            print(f"unpacking", a, b)

        unpacking(*tpe)
        unpacking(*lst)

        def unpacking_args(*arg):
            print(f"unpacking_args", arg)

        unpacking_args(*tpe)
        unpacking_args(*lst)

    def test_non_local(self):
        """
        nonlocal
        用在嵌套函数修改外层函数的变量
        """
        non_local_var = "non_local_var"

        def inner_fun():
            # 此变量即不是局部变量,也不是全局变量, 需要在外层函数有定义, 用来修改外层函数的变量
            nonlocal non_local_var
            non_local_var = "non_local_var override"

        inner_fun()
        self.assertEqual("non_local_var override", non_local_var)

    def test_dispatch(self):
        """分派"""

        # python不支持多态,使用这个可以相当于实现多态
        @functools.singledispatch
        def func_obj(obj):
            print("func:", obj)

        # func的入参数据为str类型,将调用此函数
        @func_obj.register(str)
        def func_str(obj):
            print("func_str:", obj)

        func_obj("str")


no_use_global_var = "no_use_global_var"
global_var = "global_var"


def func_global():
    return (no_use_global_var, global_var)
