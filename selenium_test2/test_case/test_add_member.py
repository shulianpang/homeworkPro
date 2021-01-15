import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_test2.page.main import MainPage


class TestAddMember():
    def setup_class(self):
        self.main = MainPage()

    def teardown_method(self):
        pass
        # self.driver.quit()

    def test_add_member(self):
        result = self.main.goto_contact().add_menber().get_list()
        assert "name" in result

        # self.driver.get("https://work.weixin.qq.com/")
        # with open("../page/cookies.json","r") as f:
        #     cookies = json.load(f)
        #
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        #
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(3)
        # self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # sleep(2)
