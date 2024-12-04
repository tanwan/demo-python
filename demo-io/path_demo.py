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
        # cwd获取当前工作路径,home获取用户路径
        print(f"cwd:{Path.cwd()},home:{Path.home()}")
        # expanduser 将~解析成$HOME
        print(Path("~/Downloads").expanduser())
        print(os.path.expanduser("~/Downloads"))
        # 拼接路径
        print(os.path.join("/root", "path"))

    def test_relative_absolute_path(self):
        """Path"""
        # 传入相对路径,Path可以以当前工作路径得出绝对路径
        print(f"absolute path:{Path('path1', 'path2', 'path3').absolute()}")
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

    def test_list_dir(self):
        """
        遍历文件夹
        如果遍历的是绝对路径, 那么结果也是绝对路径
        如果遍历的是相对路径, 那么结果也是相对路径(相对于工作路径)
        """
        # 如果遍历的是绝对路径, 那么结果也是绝对路径
        for item in Path(curdir).iterdir():
            # item也是Path
            print(item)
        # 如果遍历的是相对路径, 那么结果也是相对路径(相对于工作路径)
        for item in Path("demo-io").iterdir():
            # item也是Path
            print(item)

    def test_glob(self):
        """
        如果遍历的是绝对路径, 那么结果也是绝对路径
        如果遍历的是相对路径, 那么结果也是相对路径(相对于工作路径)
        glob: 按给定模式遍历文件夹, 不会递归遍历
        rglob: 按给定模式递归遍历文件夹
        patthern: *: 匹配任意字符, ?: 匹配单个字符, [abc]: 匹配给定的单个字符
        """
        # 如果遍历的是相对路径, 那么结果也是相对路径(相对于工作路径)
        for file in Path(".").glob("*"):
            print(file)
        # 如果遍历的是绝对路径, 那么结果也是绝对路径
        for file in Path(curdir).rglob("json*"):
            print(file)
