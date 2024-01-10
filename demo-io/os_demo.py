import unittest
import os
from pathlib import Path

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
file_dir = curdir/".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)
original_workdir = os.getcwd()

class OSDemo(unittest.TestCase):
    def setUp(self) -> None:
        # 修改工作路径
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
        # 可以是文件/文件夹, 支持相对路径
        file_stat = os.stat("dir/file")
        print(f"create time:{file_stat.st_ctime}, modify time:{file_stat.st_mtime}, size:{file_stat.st_size}")

    def test_file_exist(self):
        """判断文件存在"""
        # 可以是文件/文件夹, 支持相对路径
        print(os.path.exists("tmp"))

    def test_rename(self):
        """重命名"""
        os.makedirs("tmp/dir", exist_ok=True)
        # src/dest可以是文件/文件夹, 支持相对路径(dest不仅仅是名称, 否则就会把文件移动到工作路径中)
        os.rename("tmp/dir", "tmp/dir2")

    def test_remove(self):
        """删除文件"""
        with open("tmp/remove.txt", "w"):
            pass
        # 只能是文件, 必须存在
        os.remove("tmp/remove.txt")
    
    def test_rmdir(self):
        """删除空文件夹"""
        os.makedirs("tmp/remove")
        # 只能是空文件夹, 必须存在
        os.rmdir("tmp/remove")

    def test_list_dir(self):
        """列出文件夹下的所有文件"""
        # 支持相对路径
        # 结果是文件夹下所有文件(夹)的名称的list
        print(os.listdir("."))

    def test_expanduser(self):
        """解析～地址"""
        # 将~解析成$HOME
        print(os.path.expanduser("~/Downloads"))