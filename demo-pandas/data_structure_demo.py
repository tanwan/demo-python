import unittest
import pandas as pd


class SeriesDemo(unittest.TestCase):
    """
    Series是一维数据结构, 类似于表中的一列
    每个Series都有一个索引, 默认使用整数当索引
    """

    def test_create(self):
        """
        创建Series
        index: 指定索引, 指定索引后, data的长度不能大于索引数
        """
        data = [1, 2, 3]
        ser = pd.Series(data)
        print(ser)
        ser = pd.Series(data, index=["A", "B", "C"])
        print(ser)

    def test_get(self):
        """
        获取值
        Series[index]: 使用索引访问数据
        Series.iloc[n]: 使用位置索引访问数据
        """
        ser = pd.Series([1, 2, 3], index=["A", "B", "C"])
        self.assertEqual(1, ser["A"])
        self.assertEqual(1, ser.iloc[0])

    def test_modify(self):
        """修改数据"""
        ser = pd.Series([1, 2, 3], index=["A", "B", "C"])
        ser["A"] = 10
        self.assertEqual(10, ser.iloc[0])
        ser.iloc[1] = 20
        self.assertEqual(20, ser["B"])
        # 删除数据, 不影响原有的数据
        new_ser = ser.drop(["C"])
        print(new_ser)

    def test_operation(self):
        """
        计算
        s.sum(): 总和
        s.mean(): 平均值
        s.max()/min(): 最大值/最小值
        s.std(): 标准差
        """
        ser = pd.Series([1, 2, 3])
        self.assertEqual(6, ser.sum())
        self.assertEqual(2, ser.mean())
        self.assertEqual(3, ser.max())
        self.assertEqual(1, ser.std())


class DataFrameDemo(unittest.TestCase):
    """DataFrame是二维表格型数据, 可以当成是数据库表,具有行和列, 是Series的容器"""

    def test_create(self):
        """
        创建DataFrame
        index: 行索引, 默认使用整数当索引, 指定后, data的行数需要跟index一致
        columns: 列索引, 默认使用整数当索引, 指定后, 列数不能大于columns
        行索引和列索引用于访问数据
        df.columns: 列索引
        df.index: 行索引
        """
        # 二维数组创建(按行), 每一行数据中的元素都是一列,缺少的话,就为NaN,比如第3行第1列是3,第二列就是NaN
        data = [["A", 1], ["B", 2], [3]]
        df = pd.DataFrame(data, columns=["Col1", "Col2"], index=["Row1", "Row2", "Row3"])
        print(df)

        # 字典创建(按列), 每一列的长度都要相同
        data = {"Col1": ["A", "B", "C"], "Col2": [1, 2, 3]}
        df = pd.DataFrame(data)
        print(df)

        # 一维数组和字典创建(按行),每个字典是一行, 每个key是一行,缺少的话,就是NaN,比如第1行第3列为NaN,第3行第2列为NaN
        data = [{"Col1": "A", "Col2": 1}, {"Col1": "B", "Col2": 2}, {"Col1": "C", "Col3": 3}]
        df = pd.DataFrame(data)
        print(df)

    def test_get(self):
        """
        访问数据, 使用设置的行列索引, 如果没有设置,则使用位置索引, 0为第1个, 1为第2个
        DataFrame.loc[rowIndex]: 访问行, 返回pandas.core.series.Series, 可以遍历
        DataFrame[columnsIndex]: 访问列, 返回pandas.core.series.Series, 可以遍历
        DataFrame.loc[rowIndexs]: 访问多行, rowIndexs为list, 返回pandas.core.frame.DataFrame
        DataFrame[columnsIndexs]: 访问多列, columnsIndexs为list, 返回pandas.core.frame.DataFrame
        Series[index]: 使用索引访问数据
        Series.iloc[n]: 使用位置索引访问数据
        """
        data = [["A", 1], ["B", 2], ["C", 3]]
        df = pd.DataFrame(data, columns=["Col1", "Col2"], index=["Row1", "Row2", "Row3"])

        # 访问行
        row1 = df.loc["Row1"]
        self.assertEqual("A", row1["Col1"])
        self.assertEqual("A", row1.iloc[0])

        # 访问列
        col1 = df["Col1"]
        self.assertEqual("A", col1["Row1"])
        self.assertEqual("A", col1.iloc[0])

    def test_modify(self):
        """修改数据"""
        data = [["A", 1], ["B", 2], ["C", 3]]
        df = pd.DataFrame(data)
        # 修改和新增行
        df.loc[0] = ["AA", 11]
        self.assertEqual("AA", df.loc[0][0])

        # 修改和新增列
        df[1] = [10, 11, 12]
        self.assertEqual(10, df[1][0])

        # drop删除行,不影响原有的DataFrame
        new_df = df.drop(0)
        print(new_df)

        # drop删除列,不影响原有的DataFrame, axis: 0表示行,1表示列
        new_df = df.drop(0, axis=1)
        print(new_df)
