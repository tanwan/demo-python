import unittest


class SetDemo(unittest.TestCase):
    def test_add(self):
        """添加"""
        # 空集合不能用{},因为它表示dict
        empty_set = set()

        # add
        empty_set.add(3)
        print("add:", empty_set)

        # update: 添加多个元素使用update
        empty_set.update([1, 2, 3])
        print("update:", empty_set)

    def test_delete(self):
        """删除"""
        set1 = {1, 2, 3}
        set1.remove(2)
        print("remove:", set1)

    def test_set_operation(self):
        """
        集合操作
        |,&,-进行并集交集差集时, set1和set2都要求是set类型
        union,intersection,difference不要求seq2是set类型
        并集:set1 | set2 或者 set1.union(seq2)
        交集:set1 & set2 或者 set1.intersection(seq2)
        差集:set1 - set2 或者 set1.difference(seq2)
        """
        set1 = {1, 2}
        set2 = {2, 3, 5}
        lst = [2, 3, 5]

        # 并集,使用|
        print("union use |:", set1 | set2)
        # 并集,使用union
        print("union use union:", set1.union(lst))

        # 交集,使用&
        print("intersection use &:", set1 & set2)
        # 交集,使用intersection
        print("intersection use intersection:", set1.intersection(lst))

        # 差集,使用-
        print("difference use -:", set1 - set2)
        # 差集,使用intersection
        print(f"difference use difference:", set1.difference(lst))

    def test_comprehensions(self):
        """
        集合推导使用{}
        通用格式: {f(x) for i in seq}
        """
        lst = [(1, "a"), (1, "b"), (2, "c")]
        to_set = {i[0] for i in lst}
        print(to_set)
