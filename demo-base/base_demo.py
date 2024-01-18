import unittest

# python执行到import的时候,就会打开import的文件,然后将函数/类复制到这个程序中
# import可以添加别名, import module as alias
# 可以使用from module_name import *,这样在使用的时候就不需要使用模块名的前缀了
# 也可以导入特定的方法/类 from module_name import func, 这样就可以使用func()了, 还可以添加别名from module_name import func as f, 就可以使用f()


class BaseDemo(unittest.TestCase):
    def test_exception(self):
        """测试异常"""

        def func_exception(raise_exp):
            try:
                if raise_exp:
                    raise Exception
            except BaseException:
                # BaseException所有异常的父类
                print("catch exception")
            else:
                # else表示没有异常才会执行
                print("run success")

        func_exception(True)
        func_exception(False)

    def test_type(self):
        """
        isinstance: 判断是否是指定的类型
        type: 获取变量的类型
        """
        # isinstance判断是否属于指定类型
        print("isinstance:", isinstance(1, int))
        print("type is int ", type(1) is int)


class WithDemo(unittest.TestCase):
    """
    with用来管理上下文, 用来简化try except finally
    如果某个类定义了__enter__、__exit__方法, 那么这个类就是上下文管理器对象, 这个类就可以使用with
    1. 执行with的expression得到上下文管理器对象
    2. 调用返回值的__enter__方法
    3. __enter__的返回值赋值给as的target
    4. 执行with块
    5. 执行上下文管理器对象的__exit__方法
    """

    def test_with_success(self):
        with SimpleWith("without exception") as target:
            print("do without exception", target)

    def test_with_exception(self):
        with SimpleWith("with exception") as target:
            print("do with exceptioin", target)
            raise Exception

    def test_with_exist_false(self):
        # 如果__exit__返回False,则还会再抛出异常
        try:
            with SimpleWith("with exception exit False", False) as target:
                print("do with exceptioin exit False")
                raise Exception
        except BaseException:
            print("handle exception")


class SimpleWith(object):
    """
    上下文管理器对象
    必须有__enter__,__exit__方法
    简化try except finally
    """

    def __init__(self, param, raise_expection=True):
        self._param = param
        self._raise_expection = raise_expection
        print("with __init__,param:", param)

    def __enter__(self):
        print("with __enter__")
        # 返回值作为with as 的taget
        return self._param

    def __exit__(self, exc_type, exc_value, exc_trackback):
        """
        __exit__一定会执行
        exc_type|exc_value|exc_trackback: 在with体有异常这些才有值, 没有值就代表with体的代码执行成功
        """
        print(f"with __exit__,exc_type:{exc_type}, exc_value:{exc_value},exc_trackback:{exc_trackback}")
        if exc_trackback is None:
            print("exec success")
        else:
            print("exec expection")
        # 返回True,则直接忽略异常, 返回False重新抛出异常
        return self._raise_expection
