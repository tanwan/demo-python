import unittest
import os
import paramiko
from pathlib import Path
from stat import S_ISREG
import pexpect
import sys

curdir = Path(__file__).parent
tmpDir = curdir / ".file/tmp/"
tmpDir.mkdir(parents=True, exist_ok=True)


class SysDemo(unittest.TestCase):
    def test_argv(self):
        """
        sys.argv[0]: 被执行脚本的路径
        sys.argv[1]: 第一个命令行参数
        """
        print(f"sys.argv[0]:{sys.argv[0]}")
        if len(sys.argv) > 1:
            print(f"sys.argv[1]:{sys.argv[1]}")


class ExecCommandDemo(unittest.TestCase):
    def test_exec(self):
        """执行指令"""
        # 执行并返回结果
        print(os.popen("ls").read())
        # 只执行,不返回
        os.system("ls")
        # 可以为命令行提供变量, 相当于在命令行在执行export
        os.environ["PARAM"] = "Demo"
        print("PARAM:" + os.popen("echo $PARAM").read())


class PexpectDemo(unittest.TestCase):
    def test_pexpect_scp(self):
        """使用pexpect实现scp"""
        curdir = Path(__file__).parent
        tmpDir = curdir / ".file/tmp"
        tmpDir.mkdir(parents=True, exist_ok=True)

        cmd = f"fscp -r root@192.168.0.101:/tmp/ {tmpDir}"
        print(cmd)
        # 通过启动一个子程序
        child = pexpect.spawn(cmd)
        # 并通过正则来判断输出
        child.expect("password")
        # 然后作出交互
        child.sendline("123456")
        print(child.read())


class SCPDemo(unittest.TestCase):
    def test_paramiko_scp(self):
        """使用paramiko实现scp"""
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
