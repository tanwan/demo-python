import unittest
import collections
import types

lst = [(1, "a"), (2, "b"), (3, "c")]


class DictDemo(unittest.TestCase):
    def test_base(self):
        """字典基本使用"""
        empty_map = {}
        empty_map2 = dict()
        print(f"empty_map:{type(empty_map)},empty_map:{type(empty_map2)}")
        map = {"k1": "v1", "k2": "v2"}
        # 使用dict[key]取值,不存在会抛异常,使用dict.get(key),不存在会返回None,也可以指定默认值
        print(f"k1:{map['k1']},k2:{map.get('k2')},k3:{map.get('k3')},k4:{map.get('k4', 'default value')}")
        # 新增
        map["k3"] = "v3"
        # setdefault不存在才会新增
        map.setdefault("k3", "v3 override")
        map.setdefault("k4", "v4")
        print(f"k3:{map['k3']},k4:{map['k4']}")
        # 删除
        # 使用del, key必须存在才能删除,否则会报错
        del map["k4"]
        print(f"k4:{map.get('k4')}")
        # 使用pop, 会返回key对应的值, 可以多传一个默认值参数, 如果key不存在,则会返回这个默认值
        map.pop("k4", None)
        print(f"k4:{map.get('k4')}")

        # 遍历, 使用items可以拿到key和value
        for k, v in map.items():
            print(f"items,k:{k},v:{v}")
        # 遍历, 使用keys拿到key
        for k in map.keys():
            print(f"keys, key:{k}")
        # 遍历, 使用values拿到value,value没有去重,如果要去重,则需要使用set(map.values())
        for v in map.values():
            print(f"values, value:{v}")

    def test_comprehensions(self):
        """字典推导使用{}"""
        # 推导出dict: {f(k):g(v) for k,v in seq}
        print({k: v for k, v in lst})

    def test_default_dict(self):
        """有默认值的dict"""
        # 需要有一个构造器,这边是int,如果key不存在,则返回0
        default_int_dict = collections.defaultdict(int)
        # key不存在,返回default,这边的构造器是lambda
        default_lambda_dict = collections.defaultdict(lambda: "default")
        print(f"default_int_dict,a:{default_int_dict['a']}")
        print(f"default_lambda_dict,a:{default_lambda_dict['a']}")
        # 可以有初始化值
        default_with_int_item_dict = collections.defaultdict(int, a=1, b=2)
        print(f"default_with_int_item_dict,a:{default_with_int_item_dict['a']},c:{default_with_int_item_dict['c']}")

    def test_order_dict(self):
        """保持插入顺序的dict"""
        order_dict = collections.OrderedDict()
        order_dict["k2"] = "v2"
        order_dict["k1"] = "v1"
        order_dict["k3"] = "v3"
        print(f"order_dict:{order_dict}")

    def test_read_only_dict(self):
        """只读的dict"""
        map = {"a": 1, "b": 2}
        # 使用types.MappingProxyType把dict转为只读的
        read_only_dict = types.MappingProxyType(map)
        try:
            # 这个是只读的
            read_only_dict["1"] = 2
        except BaseException:
            print(f"exception, read_only_dict:{read_only_dict}")
        # 原来的dict是可写的
        map["a"] = 2
        print(f"read_only_dict:{read_only_dict}")
