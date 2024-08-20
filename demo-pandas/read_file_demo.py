import unittest
import os
import pandas as pd
from pathlib import Path

curdir = Path(__file__).parent
original_workdir = os.getcwd()


class ReadFileDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        print(f"work directory: {os.getcwd()}")

    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_read_csv(self):
        """
        读取csv
        header: 指定header所在的行数,None表示没有Header
        delimiter: 指定分隔符
        """
        df = pd.read_csv("demo.csv", delimiter=",", header=None)
        print(df)

    def test_read_excel(self):
        """
        读取excel
        header: 指定header所在的行数,None表示没有Header
        sheet_name: 指定sheet名称, 不指定默认读取active的sheet, sheet_name=None则读取所有的sheet,并且返回值为dict{sheetName:DataFrame}
        """
        df = pd.read_excel("demo.xlsx", header=None)
        print(df)
