from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


class SeleniumDemo(unittest.TestCase):
    def test_page_source(self):
        """
        网页源码
        driver.page_source: 网页源码, 可以交给soup处理
        """
        chrome_options = Options()

        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=chrome_options)

        # 将webdriver属性置为undefined
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

        # 隐性等待设置了一个最长等待时间,如果在规定时间内网页加载完成,则执行下一步,否则一直等到时间截止,然后执行下一步
        driver.implicitly_wait(5)
        driver.get("https://tp.wjx.top/vm/PcT5zae.aspx")

        # 显式等待 通过条件去判断
        # presence_of_element_located: 元素在dom里面
        # visibility_of: 元素可见
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "q1_28")))

        driver.find_element(By.ID, "q1_28").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_27").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_26").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_25").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_24").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_23").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_22").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_21").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_20").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(1)
        driver.find_element(By.ID, "q1_19").find_element(By.XPATH, "..").find_element(By.XPATH, "..").click()
        time.sleep(2)
        driver.find_element(By.ID, "ctlNext").click()
        time.sleep(2)
        driver.find_element(By.ID, "SM_BTN_1").click()
        time.sleep(10)

    def test_find_element_by_id(self):
        """
        通过id定位
        find_element: 默认是通过id查找元素
        send_keys: 模拟键盘输入, send_keys(Keys(from selenium.webdriver.common.keys import Keys).RETURN): 回车
        click: 点击
        text: 获取元素文本内容
        """
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.baidu.com")

        driver.find_element(By.ID, "kw").send_keys("selenium")
        driver.find_element(By.ID, "su").click()

        time.sleep(3)
        driver.quit()

    def test_find_element_by_css_selector(self):
        """
        通过CSS方式定位
        """
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.baidu.com")

        driver.find_element(By.CSS_SELECTOR, "span #kw").send_keys("selenium")
        driver.find_element(By.ID, "su").click()

        driver.quit()

    def test_find_element_by_xpath(self):
        """通过xpath方式定位"""
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.baidu.com")

        # 通过xpath方式定位
        driver.find_element(By.XPATH, "//input[@id='kw']").send_keys("selenium")
        driver.find_element(By.ID, "su").click()

        driver.quit()

    def test_headless(self):
        """使用无界面启动"""
        chrome_options = webdriver.ChromeOptions()
        # 使用headless模式
        chrome_options.add_argument("--headless")
        # windows上执行需要--disable-gpu
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=chrome_options)

        driver.get("https://www.baidu.com")
        driver.find_element(By.ID, "kw").send_keys("selenium")
        driver.find_element(By.ID, "su").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

        print(driver.page_source)
        driver.quit()

    def test_multi_windows(self):
        """多窗口"""
        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.baidu.com?id=0")
        # current_window_handle: 当前窗口的句柄, window_handles: 所有的窗口句柄
        windows0 = driver.current_window_handle
        print("windows0:", driver.current_url)

        # 使用window.open打开一个新窗口
        driver.execute_script('window.open("https://www.baidu.com?id=1")')
        # switch_to.window: 切换窗口,新打开的窗口是列表的最后一个
        driver.switch_to.window(driver.window_handles[-1])
        windows1 = driver.current_window_handle
        print("windows1:", driver.current_url)

        time.sleep(3)

        driver.execute_script('window.open("https://www.baidu.com?id=2")')
        driver.switch_to.window(driver.window_handles[-1])
        windows2 = driver.current_window_handle
        print("windows2:", driver.current_url)

        time.sleep(3)

        # switch_to.window: 切换窗口
        driver.switch_to.window(windows1)
        print("current: ", driver.current_url)
        time.sleep(3)

        # driver: 关闭当前的窗口
        driver.close()
        driver.switch_to.window(windows0)
        print("after close switch to window0: ", driver.current_url)

        time.sleep(3)
        driver.quit()
