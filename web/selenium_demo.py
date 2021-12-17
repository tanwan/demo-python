from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time
from bs4 import BeautifulSoup


class SeleniumDemo(unittest.TestCase):
    def test_selenium_find_element_by_id(self):
        """通过id定位"""
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.baidu.com")

        # 通过id定位
        # send_keys: 模拟键盘输入, send_keys(Keys(from selenium.webdriver.common.keys import Keys).RETURN): 回车
        # click: 点击
        # text: 获取元素文本内容
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        # 强制等待,无论如何都需要等待
        time.sleep(5)
        driver.quit()

    def test_selenium_find_element_by_css_selector(self):
        """通过CSS方式定位"""
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # 隐性等待设置了一个最长等待时间,如果在规定时间内网页加载完成,则执行下一步,否则一直等到时间截止,然后执行下一步
        driver.implicitly_wait(5)
        driver.get("https://www.baidu.com")

        # 通过CSS方式定位,find_element_by_css_selector:返回一个,find_elements_by_class_name: 返回多个
        driver.find_element_by_css_selector("span #kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        driver.quit()

    def test_selenium_find_element_by_xpath(self):
        """通过xpath方式定位"""
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.baidu.com")
        # 通过xpath方式定位
        driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
        driver.find_element_by_id("su").click()

        # 显示等待,通过条件去判断
        # presence_of_element_located: 元素在dom里面
        # visibility_of: 元素可见
        # By可以通过id/css/xpath定位元素
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s_ipt")))
        driver.quit()

    def test_headless(self):
        """使用无界面启动"""
        chrome_options = webdriver.ChromeOptions()
        # 使用headless模式
        chrome_options.add_argument("--headless")
        # windows上执行需要--disable-gpu
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.implicitly_wait(5)
        driver.get("https://www.baidu.com")
        driver.find_element_by_css_selector("#kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

        # driver.page_source: 网页的源码
        soup = BeautifulSoup(driver.page_source, features="lxml")
        all_a = soup.select("h3 a")
        for a in all_a:
            print(f"a.href = {a['href']}")
        driver.quit()
    
    def test_multi_windows(self):
        """多窗口"""
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.baidu.com?id=0')
        # current_window_handle: 当前窗口的句柄, window_handles: 所有的窗口句柄
        windows0 = driver.current_window_handle
        print(f"windows0:{driver.current_url}")

        # 使用window.open打开一个新窗口
        cmd = 'window.open("https://www.baidu.com?id=1")'
        driver.execute_script(cmd)
        # switch_to.window: 切换窗口,新打开的窗口是列表的最后一个
        driver.switch_to.window(driver.window_handles[-1])
        windows1 = driver.current_window_handle
        print(f"windows1:{driver.current_url}")

        time.sleep(3)

        cmd = 'window.open("https://www.baidu.com?id=2")'
        driver.execute_script(cmd)
        driver.switch_to.window(driver.window_handles[-1])
        windows2 = driver.current_window_handle
        print(f"windows2:{driver.current_url}")

        time.sleep(3)

        # switch_to.window: 切换窗口
        driver.switch_to.window(windows1)
        print(f"current: {driver.current_url}")
        time.sleep(3)

        # driver: 关闭当前的窗口
        driver.close()
        driver.switch_to.window(windows0)
        print(f"after close switch to window0: {driver.current_url}")

        time.sleep(5)
        driver.quit()
