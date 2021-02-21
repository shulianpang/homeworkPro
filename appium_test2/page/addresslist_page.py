#点击添加成员
from appium.webdriver.common.mobileby import MobileBy

from appium_test2.page.base_page import BasePage
from appium_test2.page.memberinbite_page import MemberInbitePage


class AddressListPage(BasePage):
    def add_member(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        return MemberInbitePage(self.driver)