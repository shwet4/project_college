# ====================LOGO and REGISTRATION PAGE======================================
def getFrontPageLogo():
    return "naukriApp.appModules.login:id/textViewLabel"

def submitButton():
    return "naukriApp.appModules.login:id/textViewNormalLogin"

def getHeader():
    return "naukriApp.appModules.login:id/tool_text"

def getNameText():
    return "naukriApp.appModules.login:id/resman_fullname_edittext"

def getEmailText():
    return "naukriApp.appModules.login:id/resman_email_edittext"

def getPasswordText():
    return "naukriApp.appModules.login:id/resman_password_edittext"

def getPhoneText():
    return "naukriApp.appModules.login:id/resman_phone_edittext"

def getWhatsappCheckBox():
    return "naukriApp.appModules.login:id/whatsapp_checkbox"

def getRegButton():
    return "naukriApp.appModules.login:id/resman_next_button"

def getErrorTextforPassword():
    return "naukriApp.appModules.login:id/textinput_error"

def getError():
    return "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textinput_error']"

def getLogOutNaukri():
    return "//android.widget.CompoundButton[@text='Log out of Naukri']"

def getLogOutYesButton():
    return "//android.widget.CompoundButton[@text='Yes']"

def getLogOutLogginOutText():
    return "//android.widget.TextView[@text='Okay. Logging you out. See you soon.']"



#==============================JobSearch==================================================
def filter_opt(index):
    return "//android.widget.TextView[@text='"+index+"']"

def pop_img():
    return "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewLabel']"
def pop_text(index):
    return  "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textView"+index+"']"

def search_box():
    return "//android.widget.EditText[@resource-id='naukriApp.appModules.login:id/editTextSearch']"

def entry(index):
    return  "//android.widget.EditText[@resource-id='naukriApp.appModules.login:id/et_"+index+"']"

def search_result():
    return "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewDesignation']"
def check_box(index):
    return "//android.widget.CheckBox[@text='"+index+"']"

def getImage():
    return "naukriApp.appModules.login:id/textViewLabel"


#==========================Login Page================================================
def getHPLoginBtn():
    return "naukriApp.appModules.login:id/tv_log_in"

def getLGpageLoginHeader():
    return "naukriApp.appModules.login:id/tv_header"

def getLGpageEmailButton():
    return "naukriApp.appModules.login:id/rd_email"

def getLGpageUsernameButton():
    return "naukriApp.appModules.login:id/rd_user_name"

def getLGpageEmailTextBox():
    return "naukriApp.appModules.login:id/et_email"

def getLGpagePassTextBox():
    return "naukriApp.appModules.login:id/et_password"

def getLGpageForgotPassLink():
    return "naukriApp.appModules.login:id/tv_password"

def getLGpageLoginButton():
    return "naukriApp.appModules.login:id/bt_login"

def getLGpageOrText():
    return "naukriApp.appModules.login:id/tv_or"

def getLGpageLoginUsingText():
    return "naukriApp.appModules.login:id/tv_login_using"

def getLGpageGoogleButton():
    return "naukriApp.appModules.login:id/firstTabGoogleLogin"

def getLGpageWhatsappButton():
    return "naukriApp.appModules.login:id/thirdTabWhatsappLogin"

def getLGpageRegisterForFreeButton():
    return "naukriApp.appModules.login:id/tv_register_free"

def getAFTloginIMG():
    return "naukriApp.appModules.login:id/textViewLabel"

def getAFTloginMultBtn():
    return "//android.widget.ImageButton[@index='0']"

