import pytest
import locator
import reusable
import sys
import time
sys.path.append('C:/Users/158260/PycharmProjects/testscript/AppiumTest')
from appium.webdriver.common.appiumby import AppiumBy
from pageobjects import naukri
from login_page import login
@pytest.mark.usefixtures('appiumDriver')
class TestNaukri:


    def test_pop_up_page(self):

        self.driver.update_settings({"waitForIdleTimeout": 1000})
        self.driver.implicitly_wait(10)
        obj=naukri(self.driver)
        obj.pop_page_validate()
        obj.search_box_validation(reusable.read_tag('search_job'),reusable.read_tag('search_loc'))
        obj.search_box_result()
        obj.validate_filter(reusable.read_tag('filter_opt'),reusable.read_tag('check_box'))


    def test_registration(self):
        self.driver.update_settings({"waitForIdleTimeout": 1000})
        self.driver.implicitly_wait(10)
        obj = naukri(self.driver)

        obj.Validregistration(obj.registerElementsVerification())
        obj.Invalidregistratin()

    def test_empty(self):
        self.driver.update_settings({"waitForIdleTimeout": 1000})
        self.driver.implicitly_wait(10)
        obj=naukri(self.driver)
        obj.empty_search()

    def test_login(self):
        obj=naukri(self.driver)
        self.driver.update_settings({"waitForIdleTimeout": 1000})
        self.driver.implicitly_wait(10)
        obj.loginElementsVerification()
        obj.loginTestUsingValidCredentials()
        obj.logoutCheck()




