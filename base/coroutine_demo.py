import unittest
import asyncio
import time


class CoroutineTest(unittest.TestCase):
    def test_yield(self):
        """yield"""
        lst = [1, 2, 3]
        gen = simple_yield(lst)
        # 直接调用含有yield的函数是会返回generator对象的
        print(type(gen))
        # 当调用next方法的时候,才开始执行,并且只执行到yield就会挂起
        print(f"use send {next(gen)}")
        print(f"use next {next(gen)}")
        # 当继续调用next的时候,则从yield的地方继续执行
        print(f"use next {next(gen)}")

        gen = simple_yield(lst)
        # 使用send,第一次必须是None
        print(f"use send {gen.send(None)}")
        print(f"use send {gen.send('msg1')}")
        print(f"use send {gen.send('msg2')}")

        # 使用for
        gen = simple_yield(lst)
        for i in gen:
            print(f"use for {i}")

    def test_yield_from(self):
        """yield from"""

        for i in simple_yield_from():
            print(f"i:{i}")

    def test_coroutine(self):
        """协程"""
        # 事件循环
        loop = asyncio.get_event_loop()
        # 将async函数包装成future
        task = [asyncio.ensure_future(simple_coroutine_func("coroutine1")), asyncio.ensure_future(simple_coroutine_func("coroutine2"))]
        start = time.time()
        # 交给事件循环执行
        loop.run_until_complete(asyncio.wait(task))
        spend = time.time() - start
        print(f"spend:{spend}")
        loop.close()


def simple_yield(lst):
    """
    普通函数中如果出现了yield关键字,那么该函数就不再是普通函数,而是一个生成器
    生成器就是一种迭代器,可以使用for进行迭代,或者使用next
    """
    # 直接调用此函数并不会开始执行,而是先返回一个generator对象
    i = 0
    while i < len(lst):
        # yield可以分为两个部分,左边是用来接收send传的参数,右边是用来返回值的,它们都是可选的
        # 当执行到yield的时候
        # 1. 返回yield右边的值
        # 2. 挂起,等待next或者send恢复
        msg = yield lst[i]
        # 3. 使用next或者send恢复时,则开始为msg赋值,next传的都是None,send的第一次必须为None,后面才是实际值
        print(f"msg:{msg}")
        i = i + 1


def simple_yield_from():
    """
    yield from iterable(生成器/迭代器)
    相当于:
    for item in iterable:
        yield item
    """
    # yield from iterable会返回生成器/迭代器的元素,而yield iterable会直接返回生成器/迭代器
    yield from [1, 2, 3]


async def simple_coroutine_func(name):
    """协程"""
    print(f"simple_coroutine_func {name} start")
    # await用来挂起当前协程,后面只能跟async函数或者有__await__属性的对象
    await asyncio.sleep(2)
    print(f"simple_coroutine_func {name} end")
