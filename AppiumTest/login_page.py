from appium.webdriver.common.appiumby import AppiumBy
import pageLocators
from reusable import read_tag
import time


class login:
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

    def __init__(self, driver):
        self.driver = driver

    def loginElementsVerification(self):

        try:
            time.sleep(2)
            self.driver.press_keycode(4)
            self.driver.find_element(AppiumBy.ID, self.hpLoginBtn).click()
            print("\n==============Validating Login Page=====================")
            assert self.driver.find_element(AppiumBy.ID, self.lgHeader).text == read_tag("header",self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgEmailBtn).text == read_tag("emailBtn",
                                                                                                            self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgUserNameBtn).text == read_tag(
                "unameButton", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgEmailtxtBx).text ==read_tag(
                "emailTextBox", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgPasstxtBx).text == read_tag(
                "passTextBox", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgFgtPass).text == read_tag(
                "fgtPassLink", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgLoginBtn).text == read_tag(
                "loginButton", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgOrTxt).text == read_tag("orSection",
                                                                                                         self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgLoginUsingTxt).text == read_tag(
                "loginSection", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgGoogleBtn).text == read_tag(
                "googleButton", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgWhatsAppBtn).text == read_tag(
                "whatsAppButton", self.lgXMl)
            assert self.driver.find_element(AppiumBy.ID, self.lgRegButton).text == read_tag(
                "regforfreeLink", self.lgXMl)

            print("Login page credentials verified.........................[PASS]")
            assert True

        except:
            print("Login page not verified..................................[FAIL]")
            assert False

    def loginTestUsingValidCredentials(self):
        print("==================Verifying LOGIN===========================")
        self.driver.find_element(AppiumBy.ID, self.lgEmailtxtBx).send_keys(
            read_tag("email", self.rgXML))
        self.driver.find_element(AppiumBy.ID, self.lgPasstxtBx).send_keys(
            read_tag("password", self.rgXML))
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





