import unittest
import os
from pathlib import Path

# 如果使用from .shutil_demo import ShutilDemo, 那么在执行ShutilDemo的测试方法时, 方法会被执行两次
# 原因是unittest在监测测试类时是将测试文件通过__import__()导入成模块的, 如果使用了from .shutil_demo import ShutilDemo,那么此文件被导入后, 当前模块也会存在ShutilDemo
from . import shutil_demo
from . import os_demo
from . import path_demo

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
file_dir = curdir / ".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

shutil_demo_test = shutil_demo.ShutilDemo()
os_demo_test = os_demo.OSDemo()
path_demo_test = path_demo.PathDemo()


class FileDirDemo(unittest.TestCase):
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

    @unittest.skip("在相应的测试类执行")
    def test_list_dir(self):
        """列出文件夹下的文件"""
        os_demo_test.test_list_dir()
        path_demo_test.test_list_dir()

    @unittest.skip("在相应的测试类执行")
    def test_copy(self):
        """复制文件(夹)"""
        # 文件 -> 文件夹
        shutil_demo_test.test_copy()
        # 文件 -> 文件
        shutil_demo_test.test_copyfile()
        shutil_demo_test.test_copy2()
        # 复制文件夹
        shutil_demo_test.test_copytree()

    @unittest.skip("在相应的测试类执行")
    def test_create_dir(self):
        """创建文件夹"""
        os_demo_test.test_makedirs()
        path_demo_test.test_mkdir()

    @unittest.skip("在相应的测试类执行")
    def test_remove(self):
        """删除文件"""
        # 删除文件
        os_demo_test.test_remove()
        path_demo_test.test_unlink()

    @unittest.skip("在相应的测试类执行")
    def test_remove_dir(self):
        """删除文件夹"""
        # 删除文件夹(空/非空)
        shutil_demo_test.test_rmtree()
        # 删除空文件夹
        os_demo_test.test_rmdir()
        path_demo_test.test_remove_dir()

    @unittest.skip("在相应的测试类执行")
    def test_move(self):
        """移动/重命名文件(夹)"""
        os_demo_test.test_rename()
        shutil_demo_test.test_move()

    @unittest.skip("在相应的测试类执行")
    def test_file_stat(self):
        """获取文件属性"""
        os_demo_test.test_file_stat()
        path_demo_test.test_file_stat()
