import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
# from appium.webdriver.common.multi_action import A
from appium.webdriver.common.appiumby import AppiumBy

cap = {}
cap["platformName"] = "Android"
cap["appium:deviceName"] = "RZCT41GHXKR"  # Samsung
# cap["appium:deviceName"] = "7916a41" # MI
cap["appium:appPackage"] = "com.subagent.hattrickkgames"
cap["appium:appWaitActivity"] = "com.subagent.hattrickkgames.common.intro.IntroActivity"
cap["appium:app"] = "C:\\Users\\KEY\\Downloads\\Hattrick.Games_v3_02_05_2023.apk "
cap["appium:ensureWebviewsHavePages"] = True
cap["appium:nativeWebScreenshot"] = True
cap["appium:newCommandTimeout"] = 3600
cap["appium:connectHardwareKeyboard"] = True
cap["autoDismissAlerts"] = True
cap["autoGrantPermissions"] = True
cap["autoAcceptAlerts"] = False
# {
#     "platformName": "Android",
#     "appium:deviceName": "RZCT41GHXKR",
#     # "appium:deviceName": "7916a41",  # MI
#     "appium:appPackage": "com.playsta",  # Samsung
#     "appium:appWaitActivity": "com.playsta.common.intro.IntroActivity",
#     "appium:app": "C:\\Users\\KEY\\Downloads\\PlaySta_v1.apk",
#     'autoGrantPermissions': 'true',
#     "autoDismissAlerts": "true",
#     "autoAcceptAlerts": "false"
# }

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)
driver.implicitly_wait(10)

btn_next_id = "com.playsta:id/btn_next"
btn_submit_id = "com.playsta:id/btn_submit"
btn_englishlang_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout"
inp_username_id = "com.playsta:id/edtUsername"
inp_password_id = "com.playsta:id/edtPassword"
inp_number_id = "com.playsta:id/edtNumber"
btn_signin_id = "com.playsta:id/btnSignIn"
redio_keepmesign_id = "com.playsta:id/cb_keep_live"
btn_registertext_id = "com.playsta:id/txt_register"
btn_signup_id = "com.playsta:id/btnSignUp"
btn_signintext_id = "com.playsta:id/txt_login"
btn_skip_id = "com.playsta:id/btn_skip"
btn_agree_id = "com.playsta:id/bt_accept"
btn_cancel_id = "android:id/autofill_save_no"
allow_permisssion_id = "com.android.permissioncontroller:id/permission_allow_button"
force_permission_id = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
this_permission_id = "com.android.permissioncontroller:id/permission_allow_one_time_button"
deny_permission_id = "com.android.permissioncontroller:id/permission_deny_button"
lst_matches_id = "com.playsta:id/llHeader"
manualmatches_xpath = "//android.widget.RelativeLayout[@resource-id='com.playsta:id/llHeader']//android.widget.RelativeLayout//android.widget.LinearLayout//android.widget.TextView[@text='2']"
wintossback_xpath = "//androidx.cardview.widget.CardView[@text='TO WIN THE TOSS']//androidx.cardview.widget.CardView"
inp_betprice_id = "com.playsta:id/edt_stack"
btn_betsubmit_id = "com.playsta:id/btnBet"
tost_class = "android.widget.Toast"
# //android.widget.RelativeLayout//android.widget.LinearLayout//androidx.cardview.widget.CardView
# //android.widget.RelativeLayout//android.widget.LinearLayout[@text='TO WIN THE TOSS']
# driver.execute_script("arguments[0].scrollIntoView(true);", )
driver.find_element(AppiumBy.ID, btn_skip_id).click()

# for i in range(0,4):
#     driver.find_element(AppiumBy.ID, btn_next_id).click()

driver.find_element(AppiumBy.ID, btn_submit_id).click()

driver.find_element(AppiumBy.ID, inp_username_id).send_keys("sp25")
driver.find_element(AppiumBy.ID, inp_password_id).send_keys("Test@123")
try:
    driver.find_element(AppiumBy.ID, redio_keepmesign_id).click()
except Exception as e:
    print(e)
driver.find_element(AppiumBy.ID, btn_signin_id).click()
for i in range(0,10):
    try:
        time.sleep(0.5)
        message = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
        print(message.get_attribute("Name"))
    except:
        pass
# WebDriverWait(driver, 15).until(EC.visibility_of_any_elements_located((AppiumBy.XPATH, "//android.widget.Toast")))
# time.sleep()
# els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
# print(len(els1))
# assert "invalid" in els1
try:
    driver.find_element(AppiumBy.ID, btn_cancel_id).click()
except:
    pass
driver.find_element(AppiumBy.ID, btn_agree_id).click()
time.sleep(2.5)
matches = driver.find_elements(AppiumBy.ID, lst_matches_id)
# print(len(matches))
# for i in range(len(matches)):
#     driver.execute_script("arguments[0].scrollIntoView(true);", matches[i])
# driver.scroll()

upcoming = driver.find_element(AppiumBy.XPATH, manualmatches_xpath)
# upcoming = driver.find_elements(AppiumBy.XPATH, "//android.widget.RelativeLayout//android.widget.TextView[@text='2']")
# upcoming = driver.find_elements(AppiumBy.XPATH, "//android.widget.LinearLayout/android.widget.TextView")
# upcoming = driver.find_elements(AppiumBy.XPATH, "//androidx.cardview.widget.CardView")
# print(upcoming.text)
upcoming.click()
driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.cardview.widget.CardView[3]/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()

driver.find_element(AppiumBy.ID, inp_betprice_id).clear()
driver.find_element(AppiumBy.ID, inp_betprice_id).send_keys(100)

driver.find_element(AppiumBy.ID, btn_betsubmit_id).click()

# WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((AppiumBy.XPATH, "//android.widget.Toast[1]")))
message = driver.find_element(AppiumBy.XPATH, "//android.widget.Toast[1]")
print(message.get_attribute("Name"))
# els1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
