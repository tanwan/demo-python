import unittest
import os
from pathlib import Path

# 使用pip install tabula-py
import tabula


curdir = Path(__file__).parent
original_workdir = os.getcwd()


class PDFDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        print(f"work directory: {os.getcwd()}")

    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_read_pdf_text(self):
        """pdf提取文字"""
        # pages: 'all', '1-2,3', [1,2]
        # format: csv, tsv(tab为分隔符的csv), json
        # lattice: True 使用表格的边框来确定数据单元格, 适用于有明显边框的表格pdf
        # stream: True 通过检测文本的连续性来识别表格中的数据, 适用于没有明显边框的pdf
        # password: 密码
        # pandas_options={"header": None}: 默认情况下tabula会将第一行当作列名, 使用此参数可以忽略
        dfs = tabula.read_pdf("demo.pdf", pages="all", stream=True, pandas_options={"header": None})
        # 读取出来的df是一个list,元素为DataFrame(二维表格型数据)
        print(dfs)

        # 转为csv
        tabula.convert_into("demo.pdf", "tmp/pdf.csv", output_format="csv", pages="all", stream=True)
