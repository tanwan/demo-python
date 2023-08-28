from concurrent.futures import ThreadPoolExecutor, as_completed
import unittest
import time


executor = ThreadPoolExecutor(max_workers=3)


class ConcurrentDemo(unittest.TestCase):
    def test_executor_submit(self):
        """使用executor并发执行"""
        alltask = [executor.submit(simple_long_time_task, f"task{i}") for i in range(10)]
        # 当有task完成了,就会返回,直到所有task执行完毕
        for future in as_completed(alltask):
            print(future.done)

    def test_executor_map(self):
        """executro map方法"""
        # 因为executor_map需要2个参数,因此这边就需要2个列表,前一个表示调用executor_map的第一个参数,后面的列表表示第二个参数
        results1 = executor.map(executor_map, ["use variable", "use variable", "use variable", "use variable"], [1, 2, 3, 4])
        # 返回结果的顺序与调用的顺序一致,也就是就算当前任务先返回了,也会阻塞到它的前一个任务返回结果
        # 这边很明显跟as_completed是不一样的
        for result in results1:
            print(result)
        lst = [["use list", "use list", "use list", "use list"], [1, 2, 3, 4]]
        # 使用列表进行拆包
        results2 = executor.map(executor_map, *lst)
        for result in results2:
            print(result)


def simple_long_time_task(name):
    print(f"{name} start")
    time.sleep(3)
    print(f"{name} finish")


def executor_map(a, b):
    print(f"a:{a},b:{b},start")
    time.sleep(3)
    return f"a:{a},b:{b},finish"
