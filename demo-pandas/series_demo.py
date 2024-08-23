import unittest
import pandas as pd


class SeriesDemo(unittest.TestCase):
    """
    Series是一维数据结构, 类似于表中的一列
    每个Series都有一个索引, 没有指定的话就使用下标当索引, 默认索引使用int类型
    """

    def test_create(self):
        """
        创建Series
        index: 指定索引, 指定索引后, data大小需要跟索引大小一致
        """
        data = [1, 2, 3]
        s = pd.Series(data)
        print(s)
        # 指定索引
        s = pd.Series(data, index=["A", "B", "C"])
        print(s)
        # 使用字典创建
        s = pd.Series({"A": 1, "B": 2, "C": 3})
        print(s)

    def test_get(self):
        """
        获取值
        Series[index]: 使用索引访问数据, 默认索引使用int类型
        Series.iloc[n]: 使用下标访问数据
        Series是可以遍历的
        """
        s = pd.Series([1, 2, 3], index=["A", "B", "C"])
        self.assertEqual(1, s["A"])
        self.assertEqual(1, s.iloc[0])
        for i in s:
            print(i)

    def test_modify(self):
        """
        修改数据: 使用[index], iloc[n]获取值, 然后进行赋值就可以修改数据
        添加数据: 使用[newIndex]赋值就可以在末尾新增数据
                 使用concat可以在中间插入数据
        删除数据: drop, 使用索引删除数据(不影响原有的数据),可以是单个索引,也可以是多个索引(list)
                 如果要使用下标删除数据的话,可以使用Series.index[n]获取到索引
                 del [index]: 在原有数据中删除
        """
        s = pd.Series([1, 2, 3], index=["A", "B", "C"])
        # 修改数据
        s["A"] = 10
        self.assertEqual(10, s.iloc[0])
        s.iloc[1] = 20
        self.assertEqual(20, s["B"])

        # 添加数据
        # 索引不存在赋值就可以在末尾添加数据
        s["D"] = 40
        self.assertEqual(40, s.iloc[3])
        # 在中间插入数据
        new_s = pd.concat([s[:"B"], pd.Series([5]), s["C":]])
        self.assertEqual(5, new_s.iloc[2])

        # 删除数据
        new_s = s.drop("C")
        print(new_s)
        # 使用s.index[n]获取出索引
        new_s = s.drop(s.index[2])
        print(new_s)

        del s["A"]
        print(s)

    def test_attributes(self):
        """
        属性
        size: 元素个数
        index: 索引(可遍历), 指定索引返回pandas.core.indexes.base.Index, 没有指定返回pandas.core.indexes.range.RangeIndex
            index[n]: 利用下标获取索引
            index[[n1,n2]]: 利用下标获取多个索引
        values: 值的数组(numpy.ndarray)
        """
        s = pd.Series([1, 2, 3], index=["A", "B", "C"])
        self.assertEqual(3, s.size)
        print(s.index)
        print(s.index[0])
        print(s.index[[0, 1]])
        print(s.values)

    def test_math_methods(self):
        """
        数学计算方法
        s.sum(): 总和
        s.mean(): 平均值
        s.max()/min(): 最大值/最小值
        s.std(): 标准差
        """
        s = pd.Series([1, 2, 3])
        self.assertEqual(6, s.sum())
        self.assertEqual(2, s.mean())
        self.assertEqual(3, s.max())
        self.assertEqual(1, s.std())

    def test_slice(self):
        """切片,可以使用索引,也可以使用下标"""
        s = pd.Series([1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])
        # 使用指定的索引
        print(s["B":"D"])
        print(s[:"D"])
        # 使用下标
        print(s[1:3])
        print(s[:3])

    def test_convert(self):
        """
        类型转换
        Series.str
        apply
        """
        s = pd.Series(["12,345.00", "15,345.00"])
        # 使用Series.str
        new_s = s.str.replace(",", "").astype(float)
        print(new_s)
        # 使用apply
        new_s = s.apply(lambda s: s.replace(",", "")).astype(float)
        print(new_s)
