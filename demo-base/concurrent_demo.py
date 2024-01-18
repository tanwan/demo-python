from concurrent.futures import ThreadPoolExecutor, as_completed
import unittest
import time


executor = ThreadPoolExecutor(max_workers=3)


class ConcurrentDemo(unittest.TestCase):
    def test_executor_submit(self):
        """
        使用executor.submit并发执行
        返回future
        """
        alltasks = []
        # 这边也可以换成使用列表推导, 相当于[executor.submit(simple_long_time_task, f"task{i}") for i in range(5)]
        for i in range(5):
            # submit第一个参数是一个函数, 其它参数就作为这个函数的参数, 然后返回future
            future = executor.submit(long_time_task, f"task{i}", i)
            alltasks.append(future)
        # 使用as_completed, 当有task完成了,就会返回,直到所有task执行完毕, 或者直接调用future.result会阻塞直到获得结果
        for future in as_completed(alltasks):
            print("result:", future.result())

    def test_executor_map(self):
        """
        executro.map并发执行
        返回生成器, 结果的顺序跟调用的顺序是一致的
        """
        # 因为executor_map需要2个参数,因此这边就需要2个列表,前一个表示调用executor_map的第一个参数, 后面的列表表示第二个参数
        results = executor.map(long_time_task, ["use variable1", "use variable2", "use variable3", "use variable4"], [1, 2, 3, 4])
        # 返回结果的顺序与调用的顺序一致,也就是就算当前任务先返回了,也会阻塞到它的前一个任务返回结果
        for result in results:
            print(result)


def long_time_task(name, arg1):
    """函数的参数通过submit传递"""
    print(f"{name} start")
    time.sleep(3)
    print(f"{name} finish")
    return arg1
