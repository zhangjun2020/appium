from time import sleep
from appium import webdriver
import pytest

class Test_demo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "zj"
        caps["platformVersion"] = "6.0"
        caps["appPackage"] = "com.xlgcx.enterprise"
        caps["appActivity"] = ".ui.main.SplashActivity"
        caps["noReset"] = "true"
        caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_case(self):
        sleep(20)

    def teardown(self):
        self.driver.quit()
