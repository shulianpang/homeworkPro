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
