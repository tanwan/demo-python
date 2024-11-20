import unittest
import os
from pathlib import Path

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
tmp_dir = Path(curdir / ".file/tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


class PathDemo(unittest.TestCase):
    def test_path(self):
        """Path是PurePath的子类"""
        # 传入相对路径,Path可以以当前工作路径得出绝对路径
        print(f"absolute path:{Path('path1', 'path2', 'path3').absolute()}")
        # cwd获取当前工作路径,home获取用户路径
        print(f"cwd:{Path.cwd()},home:{Path.home()}")
        # os.path.expanduser 将~解析成$HOME
        print(os.path.expanduser("~/Downloads"))
        # 拼接路径
        print(os.path.join("/root", "path"))

    def test_path(self):
        """Path"""
        # 相对路径
        relative_path1 = Path("path1", "path2", "file_demo.py")
        relative_path2 = Path("path1/path2/file_demo.py")
        # 可以用/直接拼接路径
        relative_path3 = Path("path1/path2") / "file_demo.py"
        print(f"relative path:{relative_path1},{relative_path2},{relative_path3}")
        # 绝对路径
        absolute_path1 = Path("/path1", "path2", "file_demo.py")
        absolute_path2 = Path("/path1/path2/file_demo.py")
        absolute_path3 = Path("/path1/path2") / "file_demo.py"
        print(f"absolute path:{absolute_path1},{absolute_path2},{absolute_path3}")

        # 绝对路径转相对路径
        relative_path4 = absolute_path1.relative_to(Path("/path1"))
        print(f"absolute > relative: {relative_path4}")

    def test_path_property(self):
        """Path的一些属性"""
        path = Path("/path1/path2/file_demo.py")
        # parent: 父路径,
        print(f"parent:{path.parent}")
        # name: 文件名(包括后缀), stem: 文件名(不包括后缀), suffix:文件扩展
        print(f"name with suffix:{path.name},name without suffix: {path.stem}, suffix:{path.suffix}")

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

    def test_unlink(self):
        """删除文件"""
        path = Path(tmp_dir / "remove.txt")
        with open(path, "w"):
            pass
        # 删除文件,必须存在
        path.unlink()

    def test_remove_dir(self):
        """删除空文件夹"""
        path = Path(tmp_dir / "remove")
        path.mkdir()
        # 删除空文件夹,必须存在
        path.rmdir()
