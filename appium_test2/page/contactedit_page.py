from appium.webdriver.common.mobileby import MobileBy

from appium_test2.page.base_page import BasePage


class ContactEditPage(BasePage):
    def edit_name(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        return self

    def edit_gender(self, gender):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'女')]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'男')]").click()
        return self

    def edit_phone_num(self):
        return self

    def edit_email(self, email):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(
            email)
        return self

    def click_save(self):
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click()
        from appium_test2.page.memberinbite_page import MemberInbitePage
        return MemberInbitePage(self.driver)
