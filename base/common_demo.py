import unittest
import functools

import sys


if __name__ == "__main__":
    # 直接执行此脚本,然后添加命令行参数
    # sys.argv[0],表示执行脚本的路径
    print(f"sys.argv[0]:{sys.argv[0]}")
    if len(sys.argv) > 1:
        # sys.argv[1]:第一个命令行参数
        print(f"sys.argv[1]:{sys.argv[1]}")


class CommonDemo(unittest.TestCase):
    """
    一些常用的方法
    """

    def test_fun_cache(self):
        """使用缓存"""
        for i in range(3):
            use_cache("use cache")


@functools.lru_cache(maxsize=3)
def use_cache(arg):
    print(f"exec use_cache")
