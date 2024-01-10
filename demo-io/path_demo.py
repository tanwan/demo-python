import unittest
import os
from pathlib import Path, PurePath

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
tmp_dir = Path(curdir / ".file/tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


class PathDemo(unittest.TestCase):
    def test_path(self):
        """Path是PurePath的子类"""
        # 传入相对路径,Path可以以当前工作路径得出绝对路径,而PurePath不行
        print(f"absolute path:{Path('path1', 'path2', 'path3').absolute()}")
        # cwd获取当前工作路径,home获取用户路径
        print(f"cwd:{Path.cwd()},home:{Path.home()}")
        # os.path.expanduser 将~解析成$HOME
        print(os.path.expanduser("~/Downloads"))
        # 拼接路径
        print(os.path.join("/root", "path"))

    def test_pure_path(self):
        """PurePath"""
        # 相对路径
        relative_path1 = PurePath("path1", "path2", "file_demo.py")
        relative_path2 = PurePath("path1/path2/file_demo.py")
        # 可以用/直接拼接路径
        relative_path3 = PurePath("path1/path2") / "file_demo.py"
        print(f"relative path:{relative_path1},{relative_path2},{relative_path3}")
        # 绝对路径
        absolute_path1 = PurePath("/path1", "path2", "file_demo.py")
        absolute_path2 = PurePath("/path1/path2/file_demo.py")
        absolute_path3 = PurePath("/path1/path2") / "file_demo.py"
        print(f"absolute path:{absolute_path1},{absolute_path2},{absolute_path3}")

        # parent获取父路径,name获取文件名,suffix可以文件扩展
        print(f"parent:{absolute_path1.parent},name:{absolute_path1.name},suffix:{absolute_path1.suffix}")

        # 转成Path
        print(f"PurePath to Path:{Path(curdir)}")

    def test_file_stat(self):
        """获取文件属性"""
        file_stat = Path(curdir / ".file/dir/file").stat()
        print(f"create time:{file_stat.st_ctime}, modify time:{file_stat.st_mtime}, size:{file_stat.st_size}")

    def test_read(self):
        """使用Path读取文件"""
        print(f"use path read:{Path(curdir / '.file/file').read_text()}")

    def test_to_str(self):
        """path转字符串"""
        s = str(Path(curdir))
        print(f"tostr: {s}")

    def test_mkdir(self):
        """创建文件夹"""
        Path(tmp_dir / "dir").mkdir(exist_ok=True)
