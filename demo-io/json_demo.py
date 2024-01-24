import unittest
import json
from types import SimpleNamespace
from pathlib import Path

file_dir = Path(__file__).parent / ".file"
json_file = file_dir / "json.json"
tmp_dir = file_dir / "tmp"


class JsonDemo(unittest.TestCase):
    def test_read_json(self):
        """
        反序列化
        json只能反序列化简单的数据类型,比如list,dict,string,int等
        json.load: 从文件读取
        json.loads: 从字符串读取
        """
        # 从json文件读取json为dict
        with open(json_file) as f:
            json_dict = json.load(f)
            self.assertTrue(isinstance(json_dict, dict))
            print("dict:", json_dict)

        # 从json字符串读取json为dict
        json_dict = json.loads(json_file.read_text())
        self.assertTrue(isinstance(json_dict, dict))
        print("dict:", json_dict)

    def test_write_json(self):
        """
        序列化
        json只能序列化简单的数据类型,比如list,dict,string,int等
        json.dump: 转为json字符串
        json.dumps: 转为json文件
        """
        map = {"name": "outer", "inner": {"k1": "v1", "k2": "v2"}}

        # 把dict转为json字符串,indent添加缩进,格式化比较好看
        print("json dumps: ", json.dumps(map, indent=4))

        # 把dict转为json文件
        with open(tmp_dir / "json.json", "w") as f:
            json.dump(map, f, indent=4)

    def test_read_obj_json(self):
        """反序列化复杂对象"""
        # 先序列化为dict
        map = json.loads(json_file.read_text())
        # 通过dict创建复杂对象
        outer = Outer(**map)
        print(outer)

    def test_write_obj_json(self):
        """序列化复杂对象"""
        inner = Inner("v1", "v2")
        outer = Outer("outer", inner.__dict__)
        # Inner的属性都是基本数据类型,所以使用__dict__也可以直接序列化
        print("json dumps inner obj:", json.dumps(inner.__dict__, indent=4))

        # Outer的属性没有都是基本数据类型,所以无法直接序列化,这边要多指定一个default参数,当遇到无法序列化的对象会调用它
        print("json dumps outer obj:", json.dumps(outer, default=lambda o: o.__dict__, indent=4))


# 需要序列化的类的属性就不要用下划线开头了
class Outer(object):
    def __init__(self, name, inner):
        self.name = name
        # 在这边创建Inner出来
        self.inner = Inner(**inner)

    def __str__(self):
        return f"Outer(name={self.name},inner={self.inner})"


class Inner(object):
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2

    def __str__(self):
        return f"k1={self.k1},k2={self.k2}"
