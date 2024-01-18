import unittest
import copy


# 表示继承了TestCase,使用super()可以调用到父类
class ClassDemo(unittest.TestCase):
    def test_prop(self):
        """测试属性"""
        simple_class = SimpleClass("prop1 value")
        print(simple_class.prop1)
        print(simple_class.prop2)
        # 为prop2贼值
        simple_class.prop2 = "prop2 value override"
        print(simple_class.prop2)
        # 可以动态添加属性
        simple_class._prop3 = "prop3 value"
        print(simple_class._prop3)

    def test_method(selft):
        """测试方法"""
        # 调用方法
        simple_class = SimpleClass("prop1 value")
        simple_class.method1()
        # 静态方法 类和实例都可以直接调用
        SimpleClass.static_method()
        simple_class.static_method()
        # 类方法 类和实例都可以直接调用
        SimpleClass.class_method()
        simple_class.class_method()
        # 无法调用私有方法
        # simple_class.__private_method()
        # 直接把实例当前方法调用,将会调用__call__方法
        simple_class()

    def test_inherit(self):
        """测试继承"""
        child = Child("prop value")
        child.parent_prop()

    def test_copy(self):
        """
        浅复制: copy.copy
        深复制: copy.deepcopy
        """
        lst = [SimpleClass("")]
        # 浅复制
        shallow_copy = copy.copy(lst)
        shallow_copy[0]._prop2 = "simple_copy value"
        self.assertEqual("simple_copy value", lst[0].prop2)

        # 深复制
        lst = [SimpleClass("")]
        deep_copy = copy.deepcopy(lst)
        deep_copy[0]._prop2 = "deep_copy value"
        self.assertEqual("prop2 value", lst[0].prop2)


class SimpleClass:
    # python的对象其实都是动态添加属性的,__slots__可以限定此类可以添加的属性,如果不定义,则可以任意添加属性
    __slots__ = ("_prop1", "_prop2", "_prop3")

    # 方法的第一个参数都必需是self,表示该类的实例,相当于this

    def __init__(self, prop1):
        """相当于类的构造函数,只能有一个__init__方法,创建实例的入参跟这个方法的参数要对应"""
        # 在__init__方法中为此类添加属性,推荐使用单下划线开头
        self._prop1 = prop1
        # 相当于默认值
        self._prop2 = "prop2 value"

    # 使用@property可以让类实例直接将prop1当成属性而不是方法, 相当于getter
    @property
    def prop1(self):
        return self._prop1

    @property
    def prop2(self):
        return self._prop2

    # 使用@propName.setter可以让类实例直接给prop2贼值, 相当于setter
    @prop2.setter
    def prop2(self, prop2):
        self._prop2 = prop2

    def method1(self):
        print("method1 exec")

    # @staticmethod表示该方法是个静态方法
    @staticmethod
    def static_method():
        print("static_method")

    # 必须要有个cls入参
    @classmethod
    def class_method(cls):
        print(f"class_method,cls:{cls}")

    # 使用__开头的表示私有方法,只能在内部使用
    def __private_method(self):
        print("private_method")

    # 直接将类实例当成方法调用,将会执行此方法
    def __call__(self, *args, **kwds):
        print("__call__")


class Parent:
    def __init__(self, parent_prop):
        self._parent_prop = parent_prop

    @property
    def parent_prop(self):
        return self._parent_prop


class Child(Parent):
    def __init__(self, prop):
        # 使用super()可以调用到父类
        super().__init__(prop)

    def parent_prop(self):
        print(f"parent_prop:{super().parent_prop}")
