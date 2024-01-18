import unittest
import functools
import random
import hashlib


class ListDemo(unittest.TestCase):
    def test_add(self):
        """添加"""
        lst = [1]
        # 在末尾添加
        lst.append(2)
        print("append:", lst)
        # 在指定位置插入
        lst.insert(0, 3)
        print("insert:", lst)
        # extend: 添加多个
        lst.extend([2, 3, 4])
        print("extend:", lst)
        # + 拼接list
        joined_list = lst + [5, 6, 7]
        print("join:", joined_list)

    def test_update(self):
        """修改"""
        lst = [1]
        lst[0] = 0
        print("update:", lst)

    def test_delete(self):
        """删除"""
        lst = [1, 2, 3, 3, 3, 3, 4]

        # del: 按索引删除元素
        del lst[0]
        print("by index:", lst)

        # pop: 按索引删除元素并返回它的值, 默认删除最后一个元素
        value = lst.pop(0)
        print(f"pop, value: {value}, list:{lst}")

        # remove: 按值删除元素,只会删除一个元素, 传入的值必须在list存在
        lst.remove(3)
        print("remove:", lst)

        # 使用列表推导式按值删除元素
        lst = [e for e in lst if e != 3]
        print("comprehension remove", lst)

        # clear: 清空list
        lst.clear()
        print("clear:", lst)

    def test_get(self):
        """获取元素"""
        lst = ["a", "b", "c", "d"]
        # 遍历只能拿到元素
        for e in lst:
            print("i:", e)

        # 使用enumerate可以获取索引和元素
        for i, e in enumerate(lst):
            print(f"i:{i},e:{e}")

    def test_slice(self):
        """
        切片 list[start:stop:step] list[start]到list[stop-1]每间隔step个取值
        start可以省略,默认为0
        stop可以省略,默认为len(list)
        step可以省略,默认为1,如果为负值,则表示反向
        反向的时候,start默认为len(list)-1,stop默认为-1(但是不要传-1),list[start]到list[stop+1]每间隔step个取值
        """
        lst = [1, 2, 3, 4, 5, 6]
        # 从list[1]到list[3]
        print("lst[1:4]:", lst[1:4])
        # 从list[2]到list[5],每间隔2个取值
        print("lst[2::2]:", lst[2::2])
        # 从lst[4]到lst[1]反向每间隔2个取值
        print("lst[4:0:-2]:", lst[4:0:-2])
        # [:] 可以用来复制list,相当于list.copy
        copy_list = lst[:]
        copy_list.append(7)
        print(f"lst:{lst},copy list:{copy_list}")

    def test_sort(self):
        """
        排序
        key: 提取用来排序的关键字,默认为None
             使用lambda时, 就是以lambda的结果来进行排序的,lambda格式为: lambda x: pass, x为列表中的元素
             使用functools.cmp_to_key(lambda a, b:pass),可以自定义排序算法, a/b为列表中的元素
        reverse: 是否倒序, 默认False, 也可以简单的使用lst[::-1]
        """
        unsort_list = ["c", "e", "d", "f", "a", "b"]

        # sorted: 对list排序, 生成新的list, 不影响原有的list
        sorted_list = sorted(unsort_list, reverse=True)
        print("sorted():", sorted_list)

        # key: 提取用来排序的关键字, 这边就是使用元素的md5值进行排序
        sorted_list = sorted(unsort_list, key=lambda x: hashlib.md5(x.encode()).hexdigest())
        print("sorted(key=):", sorted_list)

        # functools.cmp_to_key: 用来自定义排序
        sorted_list = sorted(unsort_list, key=functools.cmp_to_key(lambda a, b: 1 if a < b else 0 if a == b else -1))
        print("functools.cmp_to_key:", sorted_list)

        # sort跟sorted的区别就是sort是直接在list排序的, 同样也能使用key和reverse
        unsort_list.sort()
        print("lst.sort():", unsort_list)

    def test_comprehensions(self):
        """
        列表推导使用[]
        一维: [f(x) for x in seq if condition], if condition可以省略
        二维: [f(x) for row in seq for x in row if condition]
        双列表: [f(i,j) for i in seq1 for j in seq2 if condition], 先遍历seq1,再遍历seq2
        f(x)可以使用条件表达式 x if condition else y
        """
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        lst2 = ["a", "b", "c", "d", "e"]
        lst3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        result = [x * 4 for x in lst if x % 2 == 0]
        print(result)

        # f(x)使用条件表达式
        result = [x * 4 if x <= 4 else -1 for x in lst if x % 2 == 0]
        print(result)

        # 二维数组
        result = [x * 4 for row in lst3 for x in row if x % 2 == 0]
        print(result)

        # 双列表
        result = [(i, j) for i in lst for j in lst2 if i % 2 == 0]
        print(result)

    def test_list_func(self):
        """
        作用于list的一些函数和list的方向
        sum: 求和
        min: 最小的元素
        max: 最大的元素
        any: 只要有一个元素不是None,0,""就返回True,否则返回False
        all: 所有元素不是None,0,""就返回True,否则返回False
        zip(lst1, lst2): 将从个list列表的元素组成tuple,长度由元素最少的list决定,[(lst1[0], lst2[0]), (lst1[1], lst2[1])]
        zip(*zip_list): zip(lst1, lst2)的反向操作, 将[(lst1[0], lst2[0]), (lst1[1], lst2[1])]转为lst1, lst2
        list.count: 计算指定元素的个数
        """
        lst = [1, 2, 3, 4, 5]
        print(f"sum:{sum(lst)},min:{min(lst)},max:{max(lst)}")

        # any
        self.assertFalse(any(["", 0]))
        self.assertTrue(any(["", 0, 1]))

        # all
        self.assertFalse(all(["", 0, 1]))
        self.assertTrue(all(["1", 2, 1]))

        lst2 = ["a", "b", "c", "d"]
        lst3 = ["e", "f", "g", "h"]
        # zip
        zip_list = zip(lst, lst2, lst3)
        print("zip:", [i for i in zip_list])

        zip_list = [(1, "a"), (2, "b"), (3, "c")]
        lst, lst2 = zip(*zip_list)
        print(f"unzip: lst:{lst},lst2:{lst2}")

        # count
        print("cnt:", lst.count(1))

    def test_random(self):
        """随机获取list的元素"""
        lst = [1, 2, 3, 4, 5]
        # choice随机返回list中的一个元素
        print("choice:", random.choice(lst))
        # 对list进行随机排序
        random.shuffle(lst)
        print("shuffle", lst)

    def test_generator(self):
        """生成器使用()"""
        lst = [1, 2, 3, 4, 5]
        generator = (x * 2 for x in lst)
        print(type(generator))
        # 生成器只有在使用元素的时候才会生成,节省内存
        for i in generator:
            print(i)
        # 如果生成器表达式是一个函数唯一的参数,则可以省略()
        func_one_arg(x * 2 for x in lst)
        # 有多个参数,则不能省略()
        func_two_arg((x * 2 for x in lst), "arg2")

    def test_unpacking(self):
        """list拆包"""
        lst = ["a", "b", "c", "d", "e"]
        # _占位符用来忽略不关注的值, 加*的参数表示获取元组剩余的元素
        a, *rest, d, _ = lst
        self.assertEqual("a", a)
        self.assertEqual("d", d)
        print("*c: ", rest)


def func_one_arg(arg):
    for i in arg:
        print(i)


def func_two_arg(arg1, arg2):
    for i in arg1:
        print(f"{arg2},{i}")
