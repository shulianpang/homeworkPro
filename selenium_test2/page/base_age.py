import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("../page/cookies.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
