import pexpect
from pathlib import Path
import unittest

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