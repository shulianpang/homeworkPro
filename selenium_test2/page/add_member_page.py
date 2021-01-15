from selenium.webdriver.common.by import By

from selenium_test2.page.base_age import BasePage
from selenium_test2.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_menber(self):
        # 输入成员信息，点击保存
        self.find(By.ID, "username").send_keys("name")
        self.find(By.ID, "memberAdd_acctid").send_keys("13145212")
        self.find(By.ID, "memberAdd_phone").send_keys("13866668887")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)