import pytest
from appium import webdriver


@pytest.fixture(scope='class')
def appiumDriver(request):
    print("initiating chrome driver")

    desired_caps = {
        "deviceName": "Samsung",
        "platformName": "Android",
        "version": "9.0",
        "udid": "emulator-5556",
        "app": "C:/Users/158260/Downloads/naukri-com-17-1.apk"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    request.cls.driver = driver

    yield driver

    driver.quit()
