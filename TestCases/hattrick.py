import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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
cap["appium:app"] = "C:\\Users\\KEY\\Downloads\\Hattrick.Games_v3_02_05_2023.apk"
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

btn_next_id = "com.subagent.hattrickkgames:id/btn_next"
btn_submit_id = "com.subagent.hattrickkgames:id/btn_submit"
btn_englishlang_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout"
inp_username_id = "com.subagent.hattrickkgames:id/edtUsername"
inp_password_id = "com.subagent.hattrickkgames:id/edtPassword"
inp_number_id = "com.subagent.hattrickkgames:id/edtNumber"
btn_signin_id = "com.subagent.hattrickkgames:id/btnSignIn"
redio_keepmesign_id = "com.subagent.hattrickkgames:id/cb_keep_live"
btn_registertext_id = "com.subagent.hattrickkgames:id/txt_register"
btn_signup_id = "com.subagent.hattrickkgames:id/btnSignUp"
btn_signintext_id = "com.subagent.hattrickkgames:id/txt_login"
btn_skip_id = "com.subagent.hattrickkgames:id/btn_skip"
btn_agree_id = "com.subagent.hattrickkgames:id/bt_accept"
btn_cancel_id = "android:id/autofill_save_no"
allow_permisssion_id = "com.android.permissioncontroller:id/permission_allow_button"
force_permission_id = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
this_permission_id = "com.android.permissioncontroller:id/permission_allow_one_time_button"
deny_permission_id = "com.android.permissioncontroller:id/permission_deny_button"
lst_matches_id = "com.subagent.hattrickkgames:id/llHeader"
manualmatches_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.hattrickkgames:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']"
wintossback_xpath = "//android.widget.TextView[@text='TO WIN THE TOSS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]//android.widget.LinearLayout/android.widget.LinearLayout[@resource-id='com.subagent.hattrickkgames:id/flBack']"
inp_betprice_id = "com.subagent.hattrickkgames:id/edt_stack"
btn_betsubmit_id = "com.subagent.hattrickkgames:id/btnBet"
tost_class = "android.widget.Toast"
cricket_xpath = "//android.widget.HorizontalScrollView//android.widget.LinearLayout[2]"
logo_id = "com.subagent.hattrickkgames:id/txtUser"
walletamount_id = "com.subagent.hattrickkgames:id/txt_wallet"
deposit_id = "com.subagent.hattrickkgames:id/btn_deposit"
setting_id = "com.subagent.hattrickkgames:id/iv_mode"
seitch_id = "com.subagent.hattrickkgames:id/switch_mode"
db_openbets_id = "com.subagent.hattrickkgames:id/txt_match_unmatch"
db_runnername_id = "com.subagent.hattrickkgames:id/txtRunnerName"
db_oddsrate_id = "com.subagent.hattrickkgames:id/txtOddRate"
db_stackrate_id = "com.subagent.hattrickkgames:id/txtStackRate"
db_pl_id = "com.subagent.hattrickkgames:id/txtPLRate"
close_openbets_id = "com.subagent.hattrickkgames:id/fab_close"
casino_id = "com.subagent.hattrickkgames:id/menu_schedule"
promotion_id = "com.subagent.hattrickkgames:id/menu_cric_info"
menu_id = "com.subagent.hattrickkgames:id/menu_setting"
home_id = "com.subagent.hattrickkgames:id/menu_setting"
center_menu_id = "com.subagent.hattrickkgames:id/fab_center"
btn_openbets_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.hattrickkgames:id/rv_menu_list']/android.widget.LinearLayout[5]"
rp_runnername_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[1]"
rp_oddsrate_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[1]"
rp_stackprice_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[2]"
rp_pl_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[3]"
rp_bettype_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[2]"


driver.find_element(AppiumBy.ID, btn_skip_id).click()

driver.find_element(AppiumBy.ID, btn_submit_id).click()

driver.find_element(AppiumBy.ID, inp_username_id).send_keys("kt11")
driver.find_element(AppiumBy.ID, inp_password_id).send_keys("First@666")
try:
    driver.find_element(AppiumBy.ID, redio_keepmesign_id).click()
except Exception as e:
    print(e)
driver.find_element(AppiumBy.ID, btn_signin_id).click()

try:
    message = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Toast[1]")
    print(message.get_attribute("Name"))
except:
    pass
try:
    driver.find_element(AppiumBy.ID, btn_cancel_id).click()
except:
    pass
driver.find_element(AppiumBy.ID, btn_agree_id).click()
time.sleep(2.5)

driver.find_element(AppiumBy.XPATH, cricket_xpath).click()
time.sleep(2)

time.sleep(5)
upcoming = driver.find_elements(AppiumBy.XPATH, manualmatches_xpath)
print(len(upcoming))

for i in range(0, len(upcoming)):
    pass
time.sleep(5)

element = driver.find_element(AppiumBy.XPATH, wintossback_xpath)

time.sleep(10)
assert True == False
# driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.cardview.widget.CardView[3]/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()
element.click()
driver.find_element(AppiumBy.ID, inp_betprice_id).clear()
driver.find_element(AppiumBy.ID, inp_betprice_id).send_keys(100)

driver.find_element(AppiumBy.ID, btn_betsubmit_id).click()

message = WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast[1]")))
# message = driver.find_element(AppiumBy.XPATH, "//android.widget.Toast[1]")
print(message.get_attribute("Name"))

assert "Insufficient Balance" in message.get_attribute("Name")

