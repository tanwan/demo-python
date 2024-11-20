import unittest
from pathlib import Path

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
file_dir = curdir / ".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


class FileIODemo(unittest.TestCase):
    def test_read_file(self):
        """读文件"""
        with open(file_dir / "file") as file:
            # 一次性读全部
            print(f"read all:{file.read()}")
        with open(file_dir / "file") as file:
            # 按行
            for line in file:
                print(f"read by for line:{line}")
        with open(file_dir / "file") as file:
            # 使用readlines读取所有行
            lines = file.readlines()
            print(f"read lines:{lines}")
        # 使用Path读取文件
        print(f"use path read:{Path(file_dir / 'file').read_text()}")

    def test_write_file(self):
        """写文件"""
        # 文件写,w:覆盖写,a:追加写
        with open(tmp_dir / "tmp", "w") as file:
            file.write("write content")

    def test_read_then_write_file(self):
        """先读文件,后写"""
        self.test_write_file()
        # 文件写,w:覆盖写,a:追加写
        with open(tmp_dir / "tmp", "r+") as file:
            print(file.read())
            # 回到文件游标指回开头,否则写入将变成追回
            file.seek(0)
            file.write("override write content")
