import unittest
import collections
import types


class DictDemo(unittest.TestCase):
    def test_add(self):
        """添加"""
        # 空字典使用{}或者dict()
        map = {}
        # 新增
        map["k3"] = "v3"

        # setdefault不存在才会新增
        map.setdefault("k3", "v3 override")
        map.setdefault("k4", "v4")

        print("map:", map)

    def test_remove(self):
        """删除"""
        map = {"k1": "v1", "k2": "v2"}

        # del: key必须存在才能删除,否则会报错
        del map["k1"]

        # pop: 删除并返回key对应的值
        value1 = map.pop("k2")
        # pop还支持传默认值, 当要pop的key不存在, 则返回默认值
        value2 = map.pop("k2", None)
        self.assertEqual("v2", value1)
        self.assertIsNone(value2)

        print("map:", map)

    def test_get(self):
        """
        获取元素
        dict[key]: 不存在会抛异常
        dict.get(key): 不存在返回None或者默认值
        in: 判断key是否在dict中
        """
        map = {"k1": "v1", "k2": "v2"}
        # dict[key]
        self.assertEqual("v1", map["k1"])

        # dict.get(key)
        self.assertEqual("v2", map.get("k2"))
        # 返回None
        self.assertIsNone(map.get("k3"))
        # 返回默认值
        self.assertEqual("default", map.get("k3", "default"))

        # in
        self.assertTrue("k1" in map)

    def test_iterate(self):
        """
        迭代
        dict.items: 获取key和value
        dict.keys: 获取key
        dict.values: 获取value, value没有去重
        """
        map = {"k1": "v1", "k2": "v2", "k3": "v2"}

        # items
        for k, v in map.items():
            print(f"items,k:{k},v:{v}")
        # keys
        for k in map.keys():
            print("keys, key:", k)

        # values
        for v in map.values():
            print(f"values, value:", v)

        # keys和values返回的并不是list, 可以使用list进行转换
        print("to list", list(map.values()))

    def test_comprehensions(self):
        """
        字典推导使用{}
        通用格式为:  {f(x):g(x) for x in seq}
        """
        lst = [(1, "a"), (2, "b"), (3, "c")]
        map = {x[0]: x[1] for x in lst}
        print(map)

    def test_default_dict(self):
        """
        有默认值的dict
        使用collections.defaultdict, 它需要一个构造器, 这个构造器是一个lambda
        # int: 默认值为int()也就是0
        # str: 默认值为str()也就是''
        # 自定义lambda: 默认值为lambda()
        """
        # 使用int当构造器
        self.assertEqual(0, collections.defaultdict(int)["noExist"])

        # 使用lambda当构造器
        default_lambda_dict = collections.defaultdict(lambda: "default value")
        self.assertEqual("default value", default_lambda_dict["noExist"])

        # 可以有初始化值
        default_with_init_item_dict = collections.defaultdict(int, key1=1, key2=2)
        self.assertEqual(1, default_with_init_item_dict["key1"])

    def test_order_dict(self):
        """
        保持插入顺序的dict
        使用collections.OrderedDict()
        """
        order_dict = collections.OrderedDict()
        order_dict["k2"] = "v2"
        order_dict["k1"] = "v1"
        order_dict["k3"] = "v3"
        print("order_dict:", order_dict)

    def test_read_only_dict(self):
        """
        只读的dict
        types.MappingProxyType可以将dict转为只读的
        """
        read_only_dict = types.MappingProxyType({"a": 1, "b": 2})
        try:
            # 这个是只读的
            read_only_dict["1"] = 2
        except BaseException:
            print("exception, read_only_dict:", read_only_dict)
