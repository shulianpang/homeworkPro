import json
from time import sleep
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testwechat():

    def setup_method(self):
        # chrome_args = webdriver.ChromeOptions()
        # chrome_args.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_args)
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_cookies(self):
        # 获取 cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("cookies.json", "w") as f:
        #     json.dump(cookies, f)
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json","r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        sleep(2)

    # def test_wechat(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     sleep(2)
    #     self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
    #     sleep(2)
    #     self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
