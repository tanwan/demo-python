import unittest

lst = [(1, "a"), (2, "b"), (3, "c")]


class SetDemo(unittest.TestCase):
    def test_base(self):
        """集合基本使用"""
        set1 = {1, 2, 3}
        set2 = {2, 3, 5}
        lst = [2, 3, 5]
        # 空集合不能用{},它表示dict
        empty_set = set()
        # 并集,使用|的话,都需要是set
        print(f"union use |:{set1 | set2}")
        # 并集,使用union参数不需要是set
        print(f"union use union:{set1.union(lst)}")

        # 交集,使用&的话,都需要是set
        print(f"intersection use &:{set1 & set2}")
        # 交集,使用intersection参数不需要是set
        print(f"intersection use intersection:{set1.intersection(lst)}")

        # 差集,使用-的话,都需要是set
        print(f"difference use -:{set1 - set2}")
        # 差集,使用intersection参数不需要是set
        print(f"difference use difference:{set1.difference(lst)}")

    def test_comprehensions(self):
        """集合推导使用{}"""
        # 推导出set: {f(x) for i in seq}
        print({i[0] for i in lst})
