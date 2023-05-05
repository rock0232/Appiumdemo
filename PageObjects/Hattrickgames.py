from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.multi_action import A
from selenium.webdriver import ActionChains, Keys
from appium import webdriver
import time

class Hattrickgames:

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
    manualmatches_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.hattrickkgames:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']"
    wintossback_xpath = "//android.widget.TextView[@text='TO WIN THE TOSS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]//android.widget.LinearLayout/android.widget.LinearLayout[@resource-id='com.subagent.hattrickkgames:id/flBack']"
    inp_betprice_id = "com.subagent.hattrickkgames:id/edt_stack"
    btn_placebet_id = "com.subagent.hattrickkgames:id/btnBet"
    tost_xpath = "//android.widget.Toast[1]"
    cricket_xpath = "//android.widget.HorizontalScrollView//android.widget.LinearLayout[2]"
    logo_id = "com.subagent.hattrickkgames:id/txtUser"
    walletamount_id = "com.subagent.hattrickkgames:id/txt_wallet"
    exposure_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.hattrickkgames:id/rv_wallet']/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id='com.subagent.hattrickkgames:id/txt_amount']"
    deposit_id = "com.subagent.hattrickkgames:id/btn_deposit"
    setting_id = "com.subagent.hattrickkgames:id/iv_mode"
    switch_id = "com.subagent.hattrickkgames:id/switch_mode"
    db_openbets_id = "com.subagent.hattrickkgames:id/txt_match_unmatch"
    db_runnername_id = "com.subagent.hattrickkgames:id/txtRunnerName"
    db_oddsrate_id = "com.subagent.hattrickkgames:id/txtOddRate"
    db_stackrate_id = "com.subagent.hattrickkgames:id/txtStackRate"
    db_pl_id = "com.subagent.hattrickkgames:id/txtPLRate"
    close_openbets_id = "com.subagent.hattrickkgames:id/fab_close"
    close_wagerdialog_id = "com.subagent.hattrickkgames:id/iv_close"
    casino_id = "com.subagent.hattrickkgames:id/menu_schedule"
    promotion_id = "com.subagent.hattrickkgames:id/menu_cric_info"
    menu_id = "com.subagent.hattrickkgames:id/menu_setting"
    home_id = "com.subagent.hattrickkgames:id/menu_setting"
    center_menu_id = "com.subagent.hattrickkgames:id/fab_center"
    btn_openbets_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.hattrickkgames:id/rv_menu_list']/android.widget.LinearLayout[5]"
    rp_runnername_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[1]"
    rp_oddsrate_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[1]"
    rp_stackrate_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[2]"
    rp_pl_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[3]"
    rp_bettype_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.hattrickkgames:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[2]"
    cricketmatches_xpath = "//android.widget.HorizontalScrollView[@resource-id='com.subagent.hattrickkgames:id/sportTab']/android.widget.LinearLayout/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id='com.subagent.hattrickkgames:id/txt_total_sports']"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def setusername(self, username):
        self.driver.find_element(AppiumBy.ID, self.inp_username_id).clear()
        self.driver.find_element(AppiumBy.ID, self.inp_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(AppiumBy.ID, self.inp_password_id).clear()
        self.driver.find_element(AppiumBy.ID, self.inp_password_id).send_keys(password)

    def clicklogin(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_signin_id))).click()

    def clickskip(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_skip_id))).click()

    def clickletsgetstarted(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_submit_id))).click()

    def clicksignin(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_signintext_id))).click()

    def setnumber(self, number):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.inp_number_id))).send_keys(number)

    def clickagree(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_agree_id))).click()

    def clicknotsavepassword(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.btn_cancel_id))).click()

    def clickallowpermission(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.allow_permisssion_id))).click()

    def clickforcepermission(self):
        self.WebDriverWait.until(EC.presence_of_element_located((AppiumBy.ID, self.force_permission_id))).click()

    def clickonlythistime(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.this_permission_id))).click()

    def clickdenypermission(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.deny_permission_id))).click()

    def getmatchlist(self):
        pass

    def clickwintossback(self):
        self.WebDriverWait.until(EC.presence_of_element_located((AppiumBy.XPATH, self.wintossback_xpath))).click()

    def setbetprice(self, betprice):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.inp_betprice_id))).send_keys(betprice)

    def clickplacebet(self):
        self.WebDriverWait.until(EC.presence_of_element_located((
            AppiumBy.ID, self.btn_placebet_id
        ))).click()

    def clickcricket(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.cricket_xpath))).click()

    def clicklogo(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.logo_id))).click()

    def getwalletamount(self):
        walletamount = self.driver.find_element(AppiumBy.ID, self.walletamount_id).get_attribute("text")
        return float(walletamount)

    def clickwallet(self):
        self.driver.find_element(AppiumBy.ID, self.walletamount_id).click()

    def getexposure(self):
        element = self.driver.find_element(AppiumBy.ID, self.walletamount_id)
        self.WebDriverWait.until(EC.element_to_be_clickable((element)))
        element.click()
        exp = self.driver.find_element(AppiumBy.XPATH, self.exposure_xpath).get_attribute("text")
        self.driver.find_element(AppiumBy.ID, self.close_wagerdialog_id).click()
        return float(exp)

    def clickdeposti(self):
        self.driver.find_element(AppiumBy.ID, self.deposit_id).click()

    def clicksetting(self):
        self.driver.find_element(AppiumBy.ID, self.setting_id).click()

    def clickswitch(self):
        self.driver.find_element(AppiumBy.ID, self.switch_id).click()

    def clickopenbetdialog(self):
        self.driver.find_element(AppiumBy.ID, self.db_openbets_id).click()

    def getopenbetdialoginfo(self):
        runnername = self.driver.find_element(AppiumBy.ID, self.db_runnername_id).get_attribute("text")
        odds = self.driver.find_element(AppiumBy.ID, self.db_oddsrate_id).get_attribute("text")
        stake = self.driver.find_element(AppiumBy.ID, self.db_stackrate_id).get_attribute("text")
        pl = self.driver.find_element(AppiumBy.ID, self.db_pl_id).get_attribute("text")
        self.driver.find_element(AppiumBy.ID, self.close_openbets_id).click()
        return str(runnername), str(odds), str(stake), str(pl)

    def getopenbetreportinfo(self):
        runnername = self.driver.find_element(AppiumBy.XPATH, self.rp_runnername_xpath).get_attribute("text")
        odds = self.driver.find_element(AppiumBy.XPATH, self.rp_oddsrate_xpath).get_attribute("text")
        stake = self.driver.find_element(AppiumBy.XPATH, self.rp_stackrate_xpath).get_attribute("text")
        pl = self.driver.find_element(AppiumBy.XPATH, self.rp_pl_xpath).get_attribute("text")
        return str(runnername), str(odds), str(stake), str(pl)

    def clickopenbetsbtn(self):
        self.driver.find_element(AppiumBy.XPATH, self.btn_openbets_xpath).click()

    def clickmenufragement(self):
        self.driver.find_element(AppiumBy.ID, self.menu_id).click()

    def clickhome(self):
        self.driver.find_element(AppiumBy.ID, self.home_id).click()

    def clickpromotion(self):
        self.driver.find_element(AppiumBy.ID, self.promotion_id).click()

    def clickcasino(self):
        self.driver.find_element(AppiumBy.ID, self.casino_id).click()

    def clickclosedialog(self):
        self.driver.find_element(AppiumBy.ID, self.close_openbets_id).click()

    def gettoastmessage(self):
        return self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, self.tost_xpath))).get_attribute("text")

    def clickclosewagerdialog(self):
        self.driver.find_element(AppiumBy.ID, self.close_wagerdialog_id).click()
