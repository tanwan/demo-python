import unittest
from pathlib import Path
import zipfile

# __file__是当前脚本所在的路径
curdir = Path(__file__).parent
tmp_dir = Path(curdir / ".file/tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

class ZipDemo(unittest.TestCase):
    def test_zip(self):
        """测试zip"""
        source_zip_dir = curdir / ".file/zip-file.zip"
        zip = zipfile.ZipFile(source_zip_dir)
        # namelist获取zip里面的文件名
        print(f"zip names:{zip.namelist()}")
        # extractall: 解析
        zip.extractall(path=tmp_dir)

    def test_create_zip(self):
        """创建zip"""
        source_dir = curdir / ".file"
        zip = zipfile.ZipFile(tmp_dir / "create.zip", "w")
        # 添加文件, arcname表示在zip文档中的名称,如果不指定,则会把文件的完整路径都打包进去
        zip.write(source_dir / "zip-file.zip", arcname="zip-file.zip", compress_type=zipfile.ZIP_DEFLATED)
        zip.write(source_dir / "file", arcname="file", compress_type=zipfile.ZIP_DEFLATED)
        zip.close()