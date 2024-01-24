import unittest
from pathlib import Path
import zipfile
import shutil
import os

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
tmp_dir = Path(curdir / ".file/tmp")
original_workdir = os.getcwd()


class ZipDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        shutil.rmtree(tmp_dir)
        tmp_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_unpack_zip(self):
        """
        解压zip
        zip.extractall
        shutil.unpack_archive
        """
        # 支持相对路径
        zip = zipfile.ZipFile("zip-file.zip")
        # namelist获取zip里面的文件名
        print("zip names:", zip.namelist())
        # extractall: 解压
        zip.extractall(path="tmp/zip")
        # 使用shutil解压, 支持相对路径
        shutil.unpack_archive("zip-file.zip", "tmp/shutil")

    def test_create_zip(self):
        """创建zip"""
        # 支持相对路径
        zip = zipfile.ZipFile("tmp/create.zip", "w")
        # 支持相对路径
        # arcname默认跟filename一致, 用来表示文件在压缩包中的相对路径和名称
        # zip-file.zip -> zip-file.zip
        # dir/file     -> dir(文件夹)/file
        # /etc/hosts   -> /etc(文件夹)/hosts, 因此使用绝对路径的话, 就需要指定arcname, 否则会把绝对路径也包含到压缩包中
        zip.write("zip-file.zip", arcname="zip-file.zip", compress_type=zipfile.ZIP_DEFLATED)
        zip.write("dir/file", compress_type=zipfile.ZIP_DEFLATED)
        print("zip names:", zip.namelist())
        zip.close()
