from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time


class SeleniumDemo(unittest.TestCase):
    def test_selenium_find_element_by_id(self):
        """通过id定位"""
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.baidu.com")

        # 通过id定位
        # send_keys: 模拟键盘输入
        # click: 点击
        # text: 获取元素文本内容
        browser.find_element_by_id("kw").send_keys("selenium")
        browser.find_element_by_id("su").click()
        # 强制等待,无论如何都需要等待
        time.sleep(5)
        browser.quit()

    def test_selenium_find_element_by_css_selector(self):
        """通过CSS方式定位"""
        browser = webdriver.Chrome(ChromeDriverManager().install())
        # 隐性等待设置了一个最长等待时间,如果在规定时间内网页加载完成,则执行下一步,否则一直等到时间截止,然后执行下一步
        browser.implicitly_wait(5)
        browser.get("https://www.baidu.com")

        # 通过CSS方式定位
        browser.find_element_by_css_selector("#kw").send_keys("selenium")
        browser.find_element_by_id("su").click()
        browser.quit()

    def test_selenium_find_element_by_xpath(self):
        """通过xpath方式定位"""
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.baidu.com")
        # 通过xpath方式定位
        browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
        browser.find_element_by_id("su").click()

        # 显示等待,通过条件去判断
        # presence_of_element_located: 元素在dom里面
        # visibility_of: 元素可见
        # By可以通过id/css/xpath定位元素
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s_ipt")))
        browser.quit()
