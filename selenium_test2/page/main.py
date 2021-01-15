from selenium.webdriver.common.by import By

from selenium_test2.page.add_member_page import AddMemberPage
from selenium_test2.page.base_age import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
