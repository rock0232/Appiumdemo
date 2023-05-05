import pytest
from appium import webdriver
@pytest.fixture
def setup():
    cap = {}
    cap["platformName"] = "Android"
    cap["appium:deviceName"] = "RZCT41GHXKR"  # Samsung
    # cap["appium:deviceName"] = "7916a41" # MI
    cap["appium:appPackage"] = "com.subagent.hattrickkgames"
    cap["appium:appWaitActivity"] = "com.subagent.hattrickkgames.common.intro.IntroActivity"
    cap["appium:app"] = "C:\\Users\\KEY\\Downloads\\Hattrick.Games_v3_02_05_2023.apk"
    cap["appium:ensureWebviewsHavePages"] = True
    cap["appium:nativeWebScreenshot"] = True
    cap["appium:newCommandTimeout"] = 3600
    cap["appium:connectHardwareKeyboard"] = True
    cap["autoDismissAlerts"] = True
    cap["autoGrantPermissions"] = True
    cap["autoAcceptAlerts"] = False

    driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()