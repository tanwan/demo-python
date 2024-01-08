import unittest
import json
from types import SimpleNamespace
from pathlib import Path

file_dir = Path(__file__).parent / ".file"
json_file = file_dir / "json.json"
tmp_dir = file_dir / "tmp"


class JsonDemo(unittest.TestCase):
    def test_read_json(self):
        """反序列化,json只能反序列化简单的数据类型,比如list,dict,string,int等"""
        with open(json_file) as f:
            # 使用json load读取json文件
            json_dict = json.load(f)
            print(f"json load, dict type:{type(json_dict)}, dict:{json_dict}")

        json_str = json_file.read_text()
        # 使用json.loads读取json字符串
        json_dict = json.loads(json_str)
        print(f"json loads dict type:{type(json_dict)}, dict:{json_dict}")

    def test_write_json(self):
        """序列化,json只能序列化简单的数据类型,比如list,dict,string,int等"""
        map = {"name": "outer", "inner": {"k1": "v1", "k2": "v2"}}
        # 把dict转为json,indent添加缩进,格式化比较好看
        print(f"json dumps: {json.dumps(map, indent=4)}")

        with open(tmp_dir / "json.json", "w") as f:
            json.dump(map, f, indent=4)

    def test_read_obj_json(self):
        """反序列化复杂对象"""
        json_str = json_file.read_text()
        map = json.loads(json_str)
        outer = Outer(**map)
        print(f"{outer}")

    def test_write_obj_json(self):
        """序列化复杂对象"""
        inner = Inner("v1", "v2")
        outer = Outer("outer", inner.__dict__)
        # Inner的属性都是基本数据类型,所以使用__dict__也可以直接序列化
        print(f"json dumps inner obj {json.dumps(inner.__dict__,indent=4)}")
        # Outer的属性没有都是基本数据类型,所以无法直接序列化,这边要多指定一个default参数,当遇到无法序列化的对象会调用它
        print(f"json dumps outer obj {json.dumps(outer,default=lambda o: o.__dict__,indent=4)}")


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
