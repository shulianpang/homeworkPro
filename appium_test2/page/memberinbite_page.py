from appium.webdriver.common.mobileby import MobileBy

from appium_test2.page.base_page import BasePage
from appium_test2.page.contactedit_page import ContactEditPage


class MemberInbitePage(BasePage):
    def addconnect_menual(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactEditPage(self.driver)

    def get_toast(self):
        ele = self.find_and_get_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return ele