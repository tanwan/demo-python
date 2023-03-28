import unittest
import os
from pathlib import Path, PurePath
import shutil
import zipfile

# __file__是当前脚本所在的路径
curdir = PurePath(__file__).parent
tmp_dir = Path(curdir / "file/tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


class PathDemo(unittest.TestCase):
    def test_path(self):
        """Path是PurePath的子类"""
        # 传入相对路径,Path可以以当前工作路径得出绝对路径,而PurePath不行
        print(f"absolute path:{Path('path1', 'path2', 'path3').absolute()}")
        # cwd获取当前工作路径,home获取用户路径, expanduser可以解析~为绝对路径
        print(f"cwd:{Path.cwd()},home:{Path.home()}, desktop: {os.path.expanduser('~/Desktop')}")

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
        # 可以用/直接拼接路径
        print(f"absolute path:{absolute_path1},{absolute_path2},{absolute_path3}")
        # parent获取父路径,name获取文件名,suffix可以文件扩展
        print(f"parent:{absolute_path1.parent},name:{absolute_path1.name},suffix:{absolute_path1.suffix}")

        # 转成Path
        print(f"PurePath to Path:{Path(curdir)}")

    def test_read(self):
        # 使用Path读取文件
        print(f"use path read:{Path(curdir / 'file/file').read_text()}")

    def test_to_str(self):
        s = Path(curdir).resolve()
        print(f"tostr: {s}")


class FileDemo(unittest.TestCase):
    def test_walk(self):
        """使用os.walk递归遍历文件夹下的所有文件"""
        # root是遍历时的root路径, dirs是root底下所有的目录, files是root下面所有的文件
        for root, dirs, files in os.walk(curdir):
            for file in files:
                print(f"file:{root + file}")
            for dir in dirs:
                print(f"dir:{root + dir}")

    def test_read_file(self):
        """读文件"""
        with open(curdir / "file/file") as file:
            # 一次性读全部
            print(f"read all:{file.read()}")
        with open(curdir / "file/file") as file:
            # 按行
            for line in file:
                print(f"read by for line:{line}")
        with open(curdir / "file/file") as file:
            # 使用readlines读取所有行
            lines = file.readlines()
            print(f"read lines:{lines}")
        # 使用Path读取文件
        print(f"use path read:{Path(curdir / 'file/file').read_text()}")

    def test_write_file(self):
        """写文件"""
        # 文件写,w:覆盖写,a:追加写
        with open(tmp_dir / "tmp", "w") as file:
            file.write("write content")


class ShutilDemo(unittest.TestCase):
    def test_shutil(self):
        """shutil操作"""
        source_dir = curdir / "file"
        tmp_source_dir = tmp_dir / "source"
        tmp_dest_dir = tmp_dir / "dest"
        tmp_dest2_dir = tmp_dir / "dest2"
        tmp_source_dir.mkdir(parents=True, exist_ok=True)
        tmp_dest2_dir.mkdir(parents=True, exist_ok=True)

        # copyfile:复制文件,dest不要求存在,如果存在,则会覆盖
        shutil.copyfile(source_dir / "file", tmp_source_dir / "file")

        if tmp_dest_dir.exists():
            # rmtree: 删除文件夹(只能是文件夹,必须存在)
            shutil.rmtree(tmp_dest_dir)

        # copytree: 复制目录, dest必须不存在
        shutil.copytree(tmp_source_dir, tmp_dest_dir)

        # copy: 复制文件(只能是文件)到dest, dest如果是目录,则复制文件到此目录下,如果是文件,则相当于shutil.copyfile
        shutil.copy(tmp_source_dir / "file", tmp_dest2_dir)

        # move: 将(文件/目录)移动到dest,  dest如果是目录,则移动到此目录下,如果是文件,则将源文件覆盖掉目标文件
        shutil.move(tmp_dest2_dir, tmp_dest_dir)
        # unpack_archive: 解压到dest目录下
        shutil.unpack_archive(source_dir / "zip-file.zip", tmp_dest_dir)


class ZipDemo(unittest.TestCase):
    def test_zip(self):
        """测试zip"""
        source_zip_dir = curdir / "file/zip-file.zip"
        zip = zipfile.ZipFile(source_zip_dir)
        # namelist获取zip里面的文件名
        print(f"zip names:{zip.namelist()}")
        # extractall: 解析
        zip.extractall(path=tmp_dir)

    def test_create_zip(self):
        """创建zip"""
        source_dir = curdir / "file"
        zip = zipfile.ZipFile(tmp_dir / "create.zip", "w")
        # 添加文件, arcname表示在zip文档中的名称,如果不指定,则会把文件的完整路径都打包进去
        zip.write(source_dir / "zip-file.zip", arcname="zip-file.zip", compress_type=zipfile.ZIP_DEFLATED)
        zip.write(source_dir / "file", arcname="file", compress_type=zipfile.ZIP_DEFLATED)
        zip.close()
