import unittest
import os


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
