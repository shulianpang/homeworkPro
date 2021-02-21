#点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from appium_test2.page.addresslist_page import AddressListPage
from appium_test2.page.base_page import BasePage


class MainPage(BasePage):
    def click_address(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)