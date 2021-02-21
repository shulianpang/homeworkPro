# 启动app、关闭app、重启app、进入首页
from appium.webdriver import webdriver

from appium_test2.page.base_page import BasePage
from appium_test2.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
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
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self):
        return MainPage().click_address()
