import paramiko
import unittest
from pathlib import Path
from stat import  S_ISREG

curdir = Path(__file__).parent
tmpDir = curdir / ".file/tmp/"
tmpDir.mkdir(parents=True, exist_ok=True)


class SCPDemo(unittest.TestCase):
    def test_paramiko_scp(self):
        """使用paramiko进行scp"""
        # 创建客户端
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("192.168.0.101", username="root", password="123456")
        # 获取sftp
        sftp = client.open_sftp()
        # paramiko不支持目录级别的复制
        sourceDir = "/tmp/"
        for attr in sftp.listdir_attr(sourceDir):
            if S_ISREG(attr.st_mode):
               sftp.get(sourceDir + attr.filename, tmpDir / attr.filename)
