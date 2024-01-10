import unittest
from pathlib import Path
import shutil
import os

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
tmpdir = curdir / ".file/tmp"
original_workdir = os.getcwd()


class ShutilDemo(unittest.TestCase):

    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        print(f"work directory: {os.getcwd()}")
        tmpdir.mkdir(exist_ok=True)
    
    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_copyfile(self):
        """将file复制到tmp/file文件"""
        # copyfile: 复制文件, src/dest只能是文件, 支持相对路径, dest不会创建文件夹, 会覆盖掉已有的文件
        shutil.copyfile("file", "tmp/file")

    def test_copy(self):
        """将file复制到tmp文件夹下"""
        # copy: 复制文件, src只能是文件,支持相对路径, dest可以是文件/文件夹, dest不会创建文件夹, 会覆盖掉已有的文件
        shutil.copy("file", "tmp")

    def test_copytree(self):
        """将dir文件夹下的文件复制到/tmp/dir文件夹下"""
        shutil.rmtree("tmp", ignore_errors=True)
        # copytree: 复制文件夹, src/dest只能是文件夹,支持相对路径, dest必须不存在
        shutil.copytree("dir", "tmp/dir")

    def test_rmtree(self):
        """删除文件夹"""
        # 删除文件夹, src必须是存在的文件夹,支持相对路径, 如果不存在还需要忽略错误, 则使用ignore_errors=True, 清空文件夹使用先删除文件夹再创建实现
        shutil.rmtree("tmp", ignore_errors=True)

    def test_move(self):
        """移动文件"""
        shutil.rmtree("tmp/dir", ignore_errors=True)
        shutil.rmtree("tmp/dir2/dir", ignore_errors=True)
        shutil.copytree("dir", "tmp/dir")
        # move: 移动文件/文件夹, src/dest可以是文件/文件夹, 支持相对路径, dest的上一级文件夹必须存在
        # src/dest: 文件(存在) -> src覆盖desc文件
        # src:文件, dest:文件夹(存在) -> src移动到dest文件夹下, src会覆盖desc文件夹下同名的文件
        # src/dest: 文件夹(存在,dest不能有src同名的文件夹) -> src文件夹移动到dest文件夹下
        # src:文件夹, dest:不存在 -> src文件夹下的所有文件移动到dest文件夹下
        shutil.move("tmp/dir", "tmp/dir2")

    def test_unpack_archive(self):
        """解压文件"""
        shutil.rmtree("tmp", ignore_errors=True)
        # 解压到dest目录下
        shutil.unpack_archive("zip-file.zip", "tmp/zip")
