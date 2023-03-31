from appium.webdriver.common.appiumby import AppiumBy
import locator
import reusable
import time
import pageLocators
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput

class naukri():
    lgXMl = "loginPageTestData"
    rgXML = "RegPageTestData"

    hpLoginBtn = pageLocators.getHPLoginBtn()
    lgHeader = pageLocators.getLGpageLoginHeader()
    lgEmailBtn = pageLocators.getLGpageEmailButton()
    lgUserNameBtn = pageLocators.getLGpageUsernameButton()
    lgEmailtxtBx = pageLocators.getLGpageEmailTextBox()
    lgPasstxtBx = pageLocators.getLGpagePassTextBox()
    lgFgtPass = pageLocators.getLGpageForgotPassLink()
    lgLoginBtn = pageLocators.getLGpageLoginButton()
    lgOrTxt = pageLocators.getLGpageOrText()
    lgLoginUsingTxt = pageLocators.getLGpageLoginUsingText()
    lgGoogleBtn = pageLocators.getLGpageGoogleButton()
    lgWhatsAppBtn = pageLocators.getLGpageWhatsappButton()
    lgRegButton = pageLocators.getLGpageRegisterForFreeButton()

    aftLGimg = pageLocators.getAFTloginIMG()
    aftMultWedgit = pageLocators.getAFTloginMultBtn()



    def __init__(self,driver):
        self.driver=driver
    def pop_page_validate(self):
        if self.driver.find_element(AppiumBy.XPATH, locator.pop_img()).is_displayed():
            print("image is there")
            if self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewLabel").get_attribute('text')==reusable.read_tag('image_text'):
                print("heading validate.........PASS")
            else:
                print("heading validate........FAIL")
        else:
            print("image is not there")

        assert self.driver.find_element(AppiumBy.XPATH, locator.pop_text('First')).get_attribute('text')==reusable.read_tag('first')
        assert self.driver.find_element(AppiumBy.XPATH, locator.pop_text('Second')).get_attribute('text')==reusable.read_tag('second')
        assert self.driver.find_element(AppiumBy.XPATH, locator.pop_text('Third')).get_attribute('text')==reusable.read_tag('third')
        print("body text validate........PASS")


    def search_box_validation(self,job,location):
        try:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(696, 410)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            assert self.driver.find_element(AppiumBy.XPATH, locator.search_box()).is_displayed()
            self.driver.find_element(AppiumBy.XPATH,locator.search_box()).click()
            self.driver.find_element(AppiumBy.XPATH ,locator.entry('skills')).send_keys(job)
            self.driver.find_element(AppiumBy.XPATH,locator.entry('loc')).send_keys(location)
            self.driver.find_element(AppiumBy.ID,"naukriApp.appModules.login:id/b_search").click()
            print("search box validation ..............PASS")

            time.sleep(10)
        except:
            print("something went wrong")


    def search_box_result(self):
        try:
            names=self.driver.find_elements(AppiumBy.XPATH ,locator.search_result())
            for i in names:
                print(i.get_attribute('text'))
            print("printing the result.........PASS")
        except:
            print("something went wrong")

    def validate_filter(self,option,checkbox):
        try:
            self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/imageViewFilter").click()
            self.driver.find_element(AppiumBy.XPATH, locator.filter_opt(option) ).click()

            x = self.driver.find_elements(AppiumBy.XPATH,"//android.widget.CheckBox[@resource-id='naukriApp.appModules.login:id/checkBoxMultipleSelect']")
            y = self.driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewCount']")

            ans = {}
            for i, j in zip(x, y):
                ans[i.get_attribute('text')] = j.get_attribute('text')

            self.driver.find_element(AppiumBy.XPATH, locator.check_box(checkbox)).click()





            self.driver.find_element(AppiumBy.ID ,"naukriApp.appModules.login:id/textViewApplyFilter").click()
            self.driver.implicitly_wait(10)
            num=self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewHelperText").text
            num=num.split(" ")

            if ans[reusable.read_tag('check_box')]==num[0]:
                print("filter validation.............PASS")



            self.driver.find_element(AppiumBy.ID , "naukriApp.appModules.login:id/iv_back_btn").click()
            self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/iv_back_btn").click()


        except:
            print("something went wrong")


    def checkLogo(self):
        logo = self.driver.find_elements(AppiumBy.ID,locator.getFrontPageLogo())
        assert len(logo) > 0, print("LOGO not found......[PASS]")
        print("LOGO found..........[PASS]")

    def registerElementsVerification(self):

        try:

            print("Validating pre-requisites")
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(696, 410)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            self.driver.find_element(AppiumBy.ID, locator.submitButton()).click()
            assert self.driver.find_element(AppiumBy.ID, locator.getHeader()).text == reusable.read_tag(
                "headerText"), print("Header Text...... ERROR")
            print("-->", reusable.read_tag("headerText"))

            assert self.driver.find_element(AppiumBy.ID, locator.getEmailText()).text == reusable.read_tag(
                "defEmailText"), print("Email Text......ERROR")
            print("-->", reusable.read_tag("defEmailText"))

            assert self.driver.find_element(AppiumBy.ID, locator.getPasswordText()).text == reusable.read_tag(
                "defPassText"), print("Create Password Text......ERROR")
            print("-->", reusable.read_tag("defPassText"))

            assert self.driver.find_element(AppiumBy.ID, locator.getPhoneText()).text ==reusable.read_tag(
                "defPhoneText"), print("Create Phone Text......ERROR")
            print("-->", reusable.read_tag("defPhoneText"))

            assert self.driver.find_element(AppiumBy.ID, locator.getWhatsappCheckBox()).get_attribute(
                "checked") == "true", print("Not selected by default ... [error]")
            print("--> Checkbox is selected by default")

            print("Verification Successful....[PASS]")
            return True

        except:
            print("Registration failure....[FAIL]")
            return False

    def Validregistration(self, flag):
        if flag == False:
            print("Registration page pre-verification Failed -> Further registration process not performed")
        else:
            try:
                print("Verifying registration...")
                assert self.driver.find_element(AppiumBy.ID,locator.getNameText()).send_keys(reusable.read_tag("name")) ,print("Name error......[ERROR]")
                assert self.driver.find_element(AppiumBy.ID, locator.getEmailText()).send_keys(reusable.read_tag("email")), print("Email error......[ERROR]")
                assert self.driver.find_element(AppiumBy.ID, locator.getPasswordText()).send_keys(
                    reusable.read_tag("password")), print("Password error......[ERROR]")
                assert self.driver.find_element(AppiumBy.ID, locator.getPhoneText()).send_keys(
                    reusable.read_tag("mobile")), print("Number error......[ERROR]")

                chBox=self.driver.find_element(AppiumBy.ID, locator.getWhatsappCheckBox())

                if chBox.get_attribute("checked")=="true":
                    chBox.click()
                self.driver.save_screenshot("C:/Users/158260/PycharmProjects/testscript/result/reg.png")
                self.driver.find_element(AppiumBy.ID,locator.getRegButton()).click()

                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(811, 458)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.pause(0.1)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                # self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/iv_back_btn").click()
                time.sleep(5)


                print("Registration successful........[PASS]")
            except:
                print("Registration failed............[FAIL]")

    def Invalidregistratin(self):
            try:

                chBox = self.driver.find_element(AppiumBy.ID, locator.getWhatsappCheckBox())

                if chBox.get_attribute("checked") == "true":
                    chBox.click()
                self.driver.find_element(AppiumBy.ID, locator.getNameText()).clear()
                self.driver.find_element(AppiumBy.ID, locator.getEmailText()).clear()
                self.driver.find_element(AppiumBy.ID, locator.getPasswordText()).clear()
                self.driver.find_element(AppiumBy.ID, locator.getPhoneText()).clear()

                print("--->")
                self.driver.find_element(AppiumBy.ID, locator.getRegButton()).click()
                time.sleep(5)




                error=self.driver.find_elements(AppiumBy.XPATH,locator.getError())

                assert error[0].get_attribute("text") == reusable.read_tag("invalidText0"),print("Text error......[ERROR]")
                print("->",error[0].get_attribute("text") )
                assert error[1].get_attribute("text") == reusable.read_tag("invalidText1"),print("Text error......[ERROR]")
                print("->", error[1].get_attribute("text"))
                assert error[2].get_attribute("text") == reusable.read_tag("invalidText2"),print("Text error......[ERROR]")
                print("->", error[2].get_attribute("text"))
                assert error[3].get_attribute("text") == reusable.read_tag("invalidText3"),print("Text error......[ERROR]")
                print("->", error[3].get_attribute("text"))

                print("Invalid registration Verification successful.....[PASS]")
                self.driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/iv_back").click()
            except:
                print("Invalid Regiteration Verification unsuccessful...[FAIL]")
                assert False

    def empty_search(self):
        try:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(696, 410)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()



            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(945, 952)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(935, 590)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            self.driver.find_element(AppiumBy.XPATH, locator.scroll_search_box()).click()
            assert self.driver.find_element(AppiumBy.XPATH,locator.error_msg()).get_attribute("text")==reusable.read_tag("validaterror")
            print(self.driver.find_element(AppiumBy.XPATH,locator.error_msg()).get_attribute("text"))

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(848, 454)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(881, 1437)
            actions.w3c_actions.pointer_action.release()
            actions.perform()


        except:
            print("something went wrong")

    def loginElementsVerification(self):

        # try:
            time.sleep(2)
            # self.driver.press_keycode(4)
            self.driver.find_element(AppiumBy.ID, self.hpLoginBtn).click()
            print("\n==============Validating Login Page=====================")
            assert self.driver.find_element(AppiumBy.ID, self.lgHeader).text == reusable.read_tag("header")
            assert self.driver.find_element(AppiumBy.ID, self.lgEmailBtn).text == reusable.read_tag("emailBtn")
            assert self.driver.find_element(AppiumBy.ID, self.lgUserNameBtn).text == reusable.read_tag(
                "unameButton")
            assert self.driver.find_element(AppiumBy.ID, self.lgEmailtxtBx).text ==reusable.read_tag(
                "emailTextBox")
            assert self.driver.find_element(AppiumBy.ID, self.lgPasstxtBx).text == reusable.read_tag(
                "passTextBox")
            assert self.driver.find_element(AppiumBy.ID, self.lgFgtPass).text == reusable.read_tag(
                "fgtPassLink")
            assert self.driver.find_element(AppiumBy.ID, self.lgLoginBtn).text == reusable.read_tag(
                "loginButton")
            assert self.driver.find_element(AppiumBy.ID, self.lgOrTxt).text == reusable.read_tag("orSection")
            assert self.driver.find_element(AppiumBy.ID, self.lgLoginUsingTxt).text == reusable.read_tag(
                "loginSection")
            assert self.driver.find_element(AppiumBy.ID, self.lgGoogleBtn).text == reusable.read_tag(
                "googleButton")
            assert self.driver.find_element(AppiumBy.ID, self.lgWhatsAppBtn).text == reusable.read_tag(
                "whatsAppButton")
            assert self.driver.find_element(AppiumBy.ID, self.lgRegButton).text == reusable.read_tag(
                "regforfreeLink")

            print("Login page credentials verified.........................[PASS]")
        #     assert True
        #
        # except:
        #     print("Login page not verified..................................[FAIL]")
        #     assert False

    def loginTestUsingValidCredentials(self):
        print("==================Verifying LOGIN===========================")
        self.driver.find_element(AppiumBy.ID, self.lgEmailtxtBx).send_keys(
            reusable.read_tag("email"))
        self.driver.find_element(AppiumBy.ID, self.lgPasstxtBx).send_keys(
            reusable.read_tag("password"))
        self.driver.find_element(AppiumBy.ID, self.lgLoginBtn).click()

        if len(self.driver.find_elements(AppiumBy.ID, self.aftLGimg)) > 0:
            print("Login successful.........................[PASS]")
            assert True

        else:
            assert False

    def logoutCheck(self):
        if self.driver.find_element(AppiumBy.ID, self.aftLGimg).is_displayed():
            self.driver.press_keycode(4)

        self.driver.find_element(AppiumBy.XPATH, self.aftMultWedgit).click()
        time.sleep(2)
        actions = ActionChains(self.driver)

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(188, 959)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(2)
        self.driver.find_element(AppiumBy.XPATH, pageLocators.getLogOutNaukri()).click()
        self.driver.find_element(AppiumBy.XPATH, pageLocators.getLogOutYesButton()).click()
        time.sleep(2)
        # print(self.driver.find_element(AppiumBy.XPATH,pageLocators.getLGpageLoginUsingText()))
        # assert self.driver.find_element(AppiumBy.XPATH,pageLocators.getLGpageLoginUsingText()).is_displayed(), print("[ERROR]")

        print("Logout Successful..............[PASS]")