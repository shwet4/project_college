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




def getFrontPageLogo():
    return "naukriApp.appModules.login:id/textViewLabel"

def submitButton():
    return "naukriApp.appModules.login:id/tv_register"

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

def scroll_search_box():
    return "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/tv_search_jobs']"

def error_msg():
    return "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textinput_error']"
