import unittest
import os
from pathlib import Path
import shutil

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
file_dir = curdir/".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)
original_workdir = os.getcwd()


class FileDemo(unittest.TestCase):
    def test_walk(self):
        """使用os.walk递归遍历文件夹下的所有文件"""
        # root是遍历时的root路径, dirs是root底下所有的目录, files是root下面所有的文件
        for root, dirs, files in os.walk(curdir):
            for file in files:
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


class OSDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(file_dir)
        print(f"work directory: {os.getcwd()}")

    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_makedirs(self):
        """创建文件夹"""
        # 创建文件夹, 中间文件夹也会创建, 使用exist_ok=True允许文件夹已经存在
        if not os.path.exists("tmp/dir1/dir2"):
            os.makedirs("tmp/dir1/dir2", exist_ok=True)

    def test_symlink(self):
        """创建软链接"""
        link = "tmp/link"
        if os.path.islink(link):
            os.unlink(link)
        # src: 绝对路径, dest: 支持相对路径
        os.symlink(file_dir/"dir", link)

    def test_file_stat(self):
        """获取文件属性"""
        file_stat = os.stat("dir/file")
        print(f"create time:{file_stat.st_ctime}, modify time:{file_stat.st_mtime}, size:{file_stat.st_size}")
