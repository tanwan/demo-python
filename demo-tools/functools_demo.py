import unittest
import functools


class FunctoolsDemo(unittest.TestCase):
    def test_fun_cache(self):
        """使用缓存"""
        for i in range(3):
            use_cache("use cache")


@functools.lru_cache(maxsize=3)
def use_cache(arg):
    print(f"exec use_cache")
