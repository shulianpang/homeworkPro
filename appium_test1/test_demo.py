# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = 'True'
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps['settings[waitForIdleTimeout]'] = 0
        # caps['autoGrantPermissions'] = True
        # caps['dontStopAppOnReset'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/guu")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/fk1")
        el2.send_keys("张三")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/dx1")
        el4.send_keys("123")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/dwx")
        el5.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        r = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/pt").text
        assert r == "外出打卡成功"

    @pytest.mark.parametrize('name,gender,email',[('hahaha11', '男', '1234512@qq.com'), ('hahaha12', '男', '1234513@qq.com')])
    def test_add_member(self, name, gender, email):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/csn").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/../android.widget.RelativeLayout").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'女')]").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'男')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(
            email)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'设置部门')]").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gzz').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click()
        r = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert r == "添加成功"

    @pytest.mark.parametrize('name',['hahaha12','hahaha2','hahaha3','hahaha4','hahaha5'])
    def test_delete_member(self,name):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ie5').click()
        self.driver.find_element(MobileBy.XPATH,f"//*[contains(@text,'{name}')]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/bom").click()


