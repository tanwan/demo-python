import unittest
import bisect
import array
import collections


class OtherCollectionsDemo(unittest.TestCase):
    def test_range(self):
        """range"""
        # 1,2,3,4
        for i in range(1, 5):
            print("range step=1,i:", i)
        # 1,3
        for i in range(1, 5, 2):
            print("range step=2,i", i)
        # 使用list()转换为list
        print("to list:", list(range(1, 5)))

    def test_bisect(self):
        """插入后保持lst是有序的"""
        lst = []
        bisect.insort(lst, "d")
        bisect.insort(lst, "c")
        bisect.insort(lst, "f")
        print(lst)

    def test_array(self):
        """
        array,代替纯数字的list,可以提高效率
        只能存放同一种类型,因为他们存放的是值而不是引用,它是连续的内存空间
        """
        # i表示整形,d表示double
        lst = array.array("i")
        lst.append(3)
        lst.append(4)
        lst.append(2)
        print(lst)

    def test_deque(self):
        """双端队列,队列满了会丢弃队首的数据"""
        q = collections.deque(maxlen=3)
        q.append(1)
        q.append(2)
        q.append(3)
        q.append(4)
        print(q)
