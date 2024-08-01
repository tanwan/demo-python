import unittest
import os
from pathlib import Path
from .shutil_demo import ShutilDemo
from .os_demo import OSDemo
from .path_demo import PathDemo

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
file_dir = curdir / ".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)
shutil_demo = ShutilDemo()
os_demo = OSDemo()
path_demo = PathDemo()


class FileDemo(unittest.TestCase):
    def test_walk(self):
        """使用os.walk递归遍历文件夹下的所有文件"""
        # root是遍历时的root路径, dirs是root底下所有的目录, files是root下面所有的文件
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                # 使用Path拼接路径
                print(Path(root, file))
                # 使用os.path.join拼接路径
                print(f"file:{os.path.join(root, file)}")
            # 如果要过滤一些文件夹,可以把要过滤的文件夹从dirs删除掉
            for dir in dirs:
                print(f"dir:{os.path.join(root, dir)}")

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

    @unittest.skip("在相应的测试类执行")
    def test_copy(self):
        """复制文件(夹)"""
        # 复制文件
        shutil_demo.test_copy()
        shutil_demo.test_copyfile()
        # 复制文件夹
        shutil_demo.test_copytree()

    @unittest.skip("在相应的测试类执行")
    def test_create_dir(self):
        """创建文件夹"""
        os_demo.test_makedirs()
        path_demo.test_mkdir()

    @unittest.skip("在相应的测试类执行")
    def test_remove(self):
        """删除文件(夹)"""
        # 删除文件
        os_demo.test_remove()
        # 删除文件夹(空/非空)
        shutil_demo.test_rmtree()
        # 删除空文件夹
        os_demo.test_rmdir()

    @unittest.skip("在相应的测试类执行")
    def test_move(self):
        """移动/重命名文件(夹)"""
        os_demo.test_rename()
        shutil_demo.test_move()

    @unittest.skip("在相应的测试类执行")
    def test_file_stat(self):
        """获取文件属性"""
        os_demo.test_file_stat()
        path_demo.test_file_stat()
