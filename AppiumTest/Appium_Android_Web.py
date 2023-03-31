from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
import reusable
import locator
class DockerApp():
    desired_caps = {'platformName': 'Android', 'platformVersion': '11.0', 'deviceName': 'Nexus',
                    'app': "C:/Users/158260/Downloads/naukri-com-17-1.apk", 'udid': 'emulator-5554'}

    def LaunchAppiumDriver(self):
        global driver

        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        driver.implicitly_wait(10)
        driver.update_settings({"waitForIdleTimeout": 1000})

    def close_driver(self):
        driver.quit()

    def pop_page_validate(self):
        if driver.find_element(AppiumBy.XPATH, locator.pop_img()).is_displayed():
            print("image is there")
            if driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewLabel").get_attribute('text')==reusable.read_tag('image_text'):
                print("heading validate.........PASS")
            else:
                print("heading validate........FAIL")
        else:
            print("image is not there")

        assert driver.find_element(AppiumBy.XPATH, locator.pop_text('First')).get_attribute('text')==reusable.read_tag('first')
        assert driver.find_element(AppiumBy.XPATH, locator.pop_text('Second')).get_attribute('text')==reusable.read_tag('second')
        assert driver.find_element(AppiumBy.XPATH, locator.pop_text('Third')).get_attribute('text')==reusable.read_tag('third')
        print("body text validate........PASS")


        # time.sleep(5)

    def search_box_validation(self):
        try:
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(696, 410)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            assert driver.find_element(AppiumBy.XPATH, locator.search_box()).is_displayed()
            driver.find_element(AppiumBy.XPATH,locator.search_box()).click()
            driver.find_element(AppiumBy.XPATH ,locator.entry('skills')).send_keys(reusable.read_tag('search_job'))
            driver.find_element(AppiumBy.XPATH,locator.entry('loc')).send_keys(reusable.read_tag('search_loc'))
            driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/b_search").click()
            print("search box validation ..............PASS")

            time.sleep(10)
        except:
            print("something went wrong")
    def search_box_result(self):
        try:
            names=driver.find_elements(AppiumBy.XPATH ,locator.search_result())
            for i in names:
                print(i.get_attribute('text'))
            print("printing the result.........PASS")
        except:
            print("something went wrong")

    def validate_filter(self):
        try:
            driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/imageViewFilter").click()
            driver.find_element(AppiumBy.XPATH, locator.filter_opt(reusable.read_tag('filter_opt')) ).click()

            x = driver.find_elements(AppiumBy.XPATH,"//android.widget.CheckBox[@resource-id='naukriApp.appModules.login:id/checkBoxMultipleSelect']")
            y = driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewCount']")

            ans = {}
            for i, j in zip(x, y):
                ans[i.get_attribute('text')] = j.get_attribute('text')

            driver.find_element(AppiumBy.XPATH, locator.check_box(reusable.read_tag('check_box'))).click()





            driver.find_element(AppiumBy.ID ,"naukriApp.appModules.login:id/textViewApplyFilter").click()
            driver.implicitly_wait(10)
            num=driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewHelperText").text
            num=num.split(" ")

            if ans[reusable.read_tag('check_box')]==num[0]:
                print("filter validation.............PASS")

        except:
            print("something went wrong")
















obj = DockerApp()
obj.LaunchAppiumDriver()
obj.pop_page_validate()
obj.search_box_validation()
obj.search_box_result()
obj.validate_filter()
obj.close_driver()

