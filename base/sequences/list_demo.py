import unittest
import functools
import random


class ListDemo(unittest.TestCase):
    def test_base(self):
        """list的基本使用"""
        lst = [1]
        # 在末尾添加
        lst.append(2)
        # 在指定位置插入
        lst.insert(0, 3)
        print("add list:", lst)
        # extend: 添加多个
        lst.extend([2, 3, 4])
        print("extend:", lst)
        # 修改
        lst[0] = 0
        print(f"modify list:{lst}")
        # 删除
        del lst[0]
        print(f"delete list by index:{lst}")
        lst = [1, 2, 3]
        # 使用pop,返回最后一个元素的值,并删除最后一个元素,pop可以指定index,list.pop(0)就是删除第一个元素
        print(f"delete list by pop, pop: {lst.pop(0)}, list:{lst}")
        lst = [1, 2, 2, 3]
        # 使用remove,只删除第一个指定的值
        lst.remove(2)
        print(f"delete by remove,list:{lst}")
        # clear: 清空list
        lst.clear()
        print("clear:", lst)

        lst = ["a", "b", "c", "d"]
        # 遍历只能拿到元素
        for e in lst:
            print(f"i:{e}")
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
        print(f"list slice,list:{lst[1:4]}")
        # 从list[2]到list[5],每间隔2个取值
        print(f"list slice,step:2 list:{lst[2::2]}")
        # 从lst[4]到lst[1]反向每间隔2个取值
        print(f"list slice,step:-2 list:{lst[4:0:-2]}")
        # [:] 可以用来复制list,相当于list.copy
        copy_list = lst[:]
        copy_list.append(7)
        print(f"lst:{lst},copy list:{copy_list}")

    def test_sort(self):
        """排序"""
        orign_list = ["c", "e", "d", "f", "a", "b"]
        lst = orign_list[:]
        # 直接在lst排序,可以指定key和reverse
        lst.sort()
        print(f"lst sort,lst:{lst}")
        lst = orign_list[:]
        # 使用sorted,跟list.sort的区别就是,sorted不改变原有list的顺序
        print(f"lst sorted,lst:{lst},sorted:{sorted(lst)}")

        # 指定key来进行排序
        lst = orign_list[:]
        lst.sort(key=functools.cmp_to_key(lambda a, b: 1 if a < b else 0 if a == b else -1))
        print(f"lst sort whith key,lst:{lst}")

        # 倒序
        lst.sort(reverse=True)
        print(f"lst sort reverse,lst:{lst}")

        # 反转list
        lst = orign_list[:]
        print(f"lst reversed use reversed ,list:{[i for i in reversed(lst)]},use slice,list:{lst[::-1]}")

    def test_comprehensions(self):
        """列表推导使用[]"""
        lst = [1, 2, 3, 4, 5]
        lst2 = ["a", "b", "c", "d", "e"]
        lst3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print([x * 2 for x in lst])
        # 只有if: [f(x) for x in seq if condition]
        print([x for x in lst if x % 2 == 0])
        # 有if和else的: [f(x) if condition else g(x) for x in seq]
        print([x if x % 2 == 0 else -1 for x in lst])
        # 遍历二维数组:[i for row in seq for i in row if condition]
        print([i for row in lst3 for i in row if i % 2 == 0])
        # 遍历两列表,先遍历seq1,再遍历seq2: [f(i,j) for i in seq1 for j in seq2 if condition]
        print([(i, j) for i in lst for j in lst2 if i % 2 == 0])

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

    def test_list_func(self):
        """作用于list的一些函数"""
        lst = [1, 2, 3, 4, 5]
        print(f"sum:{sum(lst)},min:{min(lst)},max:{max(lst)}")

        # 只要有一个不为None,0,""(" "不算)的就返回True,否则返回False
        print(f"any False:{any(['', 0])},True:{any(['', 0, 1])}")
        # 所有元素都不为None,0,""(" "不算)的就返回True,否则返回False
        print(f"all False:{all(['', 0, 1])},True:{all(['1', 2, 1])}")

        lst2 = ["a", "b", "c", "d"]
        lst3 = ["e", "f", "g", "h"]
        # zip将list列表的元素组成tuple,长度由元素最少的list决定
        print(f"zip:{[i for i in zip(lst, lst2, lst3)]}")

        zip_list = [(1, "a"), (2, "b"), (3, "c")]
        # zip(*zip)就是zip的反向操作
        lst, lst2 = zip(*zip_list)
        print(f"unzip: lst:{lst},lst2:{lst2}")

    def test_operation(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5]
        # join
        print("join:", lst1 + lst2)

        # count
        print("count", lst1.count(1))

    def test_random(self):
        lst = [1, 2, 3, 4, 5]
        # choice随机返回list中的一个元素
        print(f"choice:{random.choice(lst)}")
        # 对list进行随机排序
        random.shuffle(lst)
        print(f"shuffle:{lst}")


def func_one_arg(arg):
    for i in arg:
        print(i)


def func_two_arg(arg1, arg2):
    for i in arg1:
        print(f"{arg2},{i}")
