import unittest
import pyautogui
from pathlib import Path

curdir = Path(__file__).parent
tmpDir = curdir / ".file/tmp/"
tmpDir.mkdir(parents=True, exist_ok=True)


class AutoGUIDemo(unittest.TestCase):
    def test_pause(self):
        """
        pyautogui.PAUSE=n: 为所有的PyAutoGUI自带api函数增加延迟,默认0.1秒
        pyautogui.sleep(n): 临时休眠, 需要延迟才执行下一个操作
        """
        pyautogui.PAUSE = 2
        pyautogui.moveTo(500, 500)
        pyautogui.moveTo(600, 500)
        pyautogui.sleep(3)
        pyautogui.moveTo(500, 500)

    def test_screen(self):
        """
        屏幕
        size(): 屏幕尺寸
        onScreen(x, y): 坐标是否在屏幕范围内
        pyautogui.screenshot(region=(x, y, width, heigth)): 截图, 不指定region, 则为整个屏幕
        """
        # 屏幕尺寸
        print(pyautogui.size())
        # 坐标是否在屏幕范围内
        print(pyautogui.onScreen(200, 200))
        # 屏幕截图
        img = pyautogui.screenshot(region=(100, 100, 200, 200))
        # 保存截图
        img.save(tmpDir / "screenshot.png")

    def test_mouse(self):
        """
        鼠标
        position(): 鼠标位置
        moveTo(x, y, duration=xx): 经过xx秒,将鼠标移动到指定坐标(绝对坐标)
        moveRel(x, y, duration=xx): 经过xx秒,将鼠标移动到指定坐标(相对当前坐标)
        click/rightClick/doubleClick: 鼠标点击
        click(100, 100, clicks=3, interval=0.1, duration=0.5): 经过0.5秒移动到指定坐标, 间隔0.1秒点击一次
        mouseDown/mouseUp: 按下/释放鼠标
        """
        # 鼠标位置
        print(pyautogui.position())
        # 经过xx秒,将鼠标移动到指定坐标(绝对坐标)
        pyautogui.moveTo(500, 500, duration=0.5)
        # 经过xx秒,将鼠标移动到指定坐标(相对当前坐标)
        pyautogui.moveRel(-100, 100, duration=0.5)
        # 鼠标点击 click/rightClick/doubleClick
        # pyautogui.click(100, 100, clicks=3, interval=0.1, duration=0.5): 经过0.5秒移动到指定坐标, 间隔0.1秒点击一次
        pyautogui.click()
        # 在指定位置按下鼠标xx秒
        pyautogui.mouseDown(500, 500, duration=1)
        pyautogui.mouseUp()

    def test_keyboard(self):
        """
        键盘
        press(keys): 按下键盘, 支持str和list,对应的名称在pyautogui.KEY_NAMES
        typewrite(str): 传入字符串
        hotkey(): 快捷键, 不生效的话, 可以使用多个pyautogui.keyDown()代替
        """
        # 按下键盘
        # 键盘对应的名称在 pyautogui.KEY_NAMES
        pyautogui.press(["B", "c"])
        # 传入字符串, 只支持英文
        pyautogui.typewrite("hello, world", interval=0.3)
        # 不生效的话,可以使用pyautogui.keyDown("command") pyautogui.hotkey("a")代替
        pyautogui.hotkey("command", "A")
