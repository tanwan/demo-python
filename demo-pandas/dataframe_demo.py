import unittest
import pandas as pd


class DataFrameDemo(unittest.TestCase):
    """
    DataFrame是Series的容器, 相当于是二维表格型数据, 可以当成是数据库表,具有行和列
    每个DataFrame都有两个索引, 一个是index(行索引), 一个是columns(列索引), 没有指定的话就使用下标当索引, 默认索引使用int类型
    """

    def test_create(self):
        """
        创建DataFrame
        index: 指定行索引, data大小需要跟index一致
        columns: 指定列索引, 列数不能大于columns
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
        访问数据
        DataFrame.loc[rowIndex]: 使用索引访问行,返回Series, 默认索引使用int类型
        DataFrame.iloc[n]: 使用下标访问行, 返回Series
        DataFrame[columnsIndex]: 使用索引访问列, 返回Series, 默认索引使用int类型
        DataFrame.iloc[:,n]: 使用下标访问列, 返回Series
        DataFrame.loc[rowIndexs]: 访问多行, rowIndexs为list, 返回DataFrame
        DataFrame[columnsIndexs]: 访问多列, columnsIndexs为list, 返回DataFrame
        iterrows: 遍历行, 返回tuple(行索引,Series)
        """
        data = [["A", 1], ["B", 2], ["C", 3]]
        df1 = pd.DataFrame(data, columns=["Col1", "Col2"], index=["Row1", "Row2", "Row3"])
        df2 = pd.DataFrame(data)

        # 访问行
        row1 = df1.loc["Row1"]
        self.assertEqual("A", row1.iloc[0])
        row1 = df1.iloc[0]
        self.assertEqual("A", row1.iloc[0])
        # 使用默认索引
        row1 = df2.loc[0]
        self.assertEqual("A", row1.iloc[0])
        row1 = df2.iloc[0]
        self.assertEqual("A", row1.iloc[0])

        # 访问列
        col1 = df1["Col1"]
        self.assertEqual("A", col1["Row1"])
        col1 = df1.iloc[:, 0]
        self.assertEqual("A", col1["Row1"])
        # 使用默认索引
        col1 = df2[0]
        self.assertEqual("A", col1.iloc[0])
        col1 = df2.iloc[:, 0]
        self.assertEqual("A", col1.iloc[0])

        # 遍历行, i为行索引, row为Series
        for i, row in df1.iterrows():
            print(row)

    def test_modify(self):
        """
        修改行列: 使用loc,iloc, [columnsIndex]获取行列,然后进行赋值
        新增行列: 使用loc[newIndex], [newColumnsIndex], 可以在末尾添加行列
                 使用concat可以在中间插入数据
        删除行列(不影响原有的数据): drop, 使用索引删除数据,可以是单个索引,也可以是多个索引(list)
                                axis: 0表示行(默认),1表示列
                                要使用下标删除数据的话,需要使用df.index[n],df.columns[n]获取索引
                                del: 只能用来删除列, del df[columnIndex]
        """
        data = [["A", 1], ["B", 2], ["C", 3]]
        df = pd.DataFrame(data, columns=["Col1", "Col2"], index=["Row1", "Row2", "Row3"])
        # 修改行
        df.loc["Row1"] = ["AA", 11]
        self.assertEqual("AA", df.iloc[0][0])
        # 修改列
        df["Col1"] = [11, 22, 33]
        self.assertEqual(11, df["Col1"]["Row1"])

        # 增加行, 数据要跟列数对上, 可以使用[col1, col2...] + [None] * (df.shape[1] - n)来填充
        df.loc["Row5"] = ["EE", 55]
        self.assertEqual("EE", df.iloc[3][0])
        # 增加列, 数据要跟行数对上
        df["Col3"] = [111, 222, 333, 555]
        self.assertEqual(111, df["Col3"]["Row1"])

        # 删除行
        new_df = df.drop("Row1")
        print(new_df)
        # 使用df.index[n]获取索引
        new_df = df.drop(df.index[0])
        print(new_df)
        # 删除列
        new_df = df.drop("Col1", axis=1)
        print(new_df)
        # 使用df.columns[n]获取索引
        new_df = df.drop(df.columns[0], axis=1)
        print(new_df)

    def test_index_and_columns(self):
        """
        索引
        rename: 修改索引名称, index修改行索引, columns列索引
        reset_index: 重置索引
            inplace: 默认不会修改原来的DataFrame, inplace为Ture时,则会修改原来的DataFrame
            drop: True:删除原来的索引, False: 原来的索引会成为一列
        set_index: 将指定的列作为索引, 如果需要新增索引时, 可以新增一列,然后将这列当作索引
            inplace: 默认不会修改原来的DataFrame, inplace为Ture时,则会修改原来的DataFrame
        df.columns =
            range(df.shape[1]): 将索引重置为默认索引(下标)
            [index]: 将列索引修改为指定的list
        """
        data = [["A", 1], ["B", 2], ["C", 3]]
        df = pd.DataFrame(data, columns=["Col1", "Col2"], index=["Row1", "Row2", "Row3"])
        # rename, 参数为旧索引和新索引的映射关系
        new_df = df.rename(
            index={"Row1": "newRow1", "Row2": "newRow2"},
            columns={"Col1": "newCol1", "Col2": "newCol2"},
        )
        print(new_df)
        # 将行索引重置为默认索引(下标)
        new_df = df.reset_index(drop=True)
        print(df)
        # 将Col1作为索引
        new_df = df.set_index("Col1")
        print(new_df)

        # 新增索引
        df["new_index"] = ["newRow1", "newRow2", "newRow3"]
        df.set_index("new_index", inplace=True)
        print(df)

        # 将列索引重置为默认索引(下标)
        df.columns = range(df.shape[1])
        print(df)

        # 修改列索引
        df.columns = ["Col1", "Col2"]
        print(df)

    def test_concat(self):
        """
        拼接行列, 默认为拼接行, axis=1为拼接列
        拼接行时, 就算行索引相同时, 也会拼接上去, 列索引不同的话, 则会新增列
        拼接列时, 就算列索引相同时, 也会拼接上去, 行索引不同的话, 则会新增行
        ignore_index=True: 会忽略掉之前的拼接的索引, 使用下标当索引
        """
        data1 = [["A", 1], ["B", 2]]
        data2 = [["AA", 11], ["BB", 22]]
        df1 = pd.DataFrame(data1, columns=["Col1", "Col2"], index=["Row1", "Row2"])
        df2 = pd.DataFrame(data2, columns=["Col1", "Col3"], index=["Row1", "Row3"])
        # 拼接行, 行索引使用下标
        df = pd.concat([df1, df2], ignore_index=True)
        print(df)
        # 拼接列, 列索引使用下标
        df = pd.concat([df1, df2], axis=1, ignore_index=True)
        print(df)

    def test_merge(self):
        """
        merge: 相当于数据库表的join, merge后, 行索引会变成默认索引
        how: join方法, inner(默认), left, right, outer, 跟数据库的join一样
        on: 关联的列索引, 多个使用list
        """
        data1 = [["A", "a", 1], ["B", "b", 2], ["C", "c", 3]]
        data2 = [["A", "a", 10], ["B", "bb", 20], ["CC", "cc", 30]]
        df1 = pd.DataFrame(data1, columns=["Col1", "Col2", "Col3"])
        df2 = pd.DataFrame(data2, columns=["Col1", "Col2", "Col4"])
        df = pd.merge(df1, df2, on="Col1", how="inner")
        print(df)
