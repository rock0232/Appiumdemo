from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from Utilities.customlogger import Logger

class Run567:
    logger = Logger.logen()

    btn_next_id = "com.subagent.run567:id/btn_next"
    btn_submit_id = "com.subagent.run567:id/btn_submit"
    btn_englishlang_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout"
    inp_username_id = "com.subagent.run567:id/edtUsername"
    inp_password_id = "com.subagent.run567:id/edtPassword"
    inp_number_id = "com.subagent.run567:id/edtNumber"
    btn_signin_id = "com.subagent.run567:id/btnSignIn"
    redio_keepmesign_id = "com.subagent.run567:id/cb_keep_live"
    btn_registertext_id = "com.subagent.run567:id/txt_register"
    btn_signup_id = "com.subagent.run567:id/btnSignUp"
    btn_signintext_id = "com.subagent.run567:id/txt_login"
    btn_skip_id = "com.subagent.run567:id/btn_skip"
    btn_agree_id = "com.subagent.run567:id/bt_accept"
    btn_cancel_id = "android:id/autofill_save_no"
    allow_permisssion_id = "com.android.permissioncontroller:id/permission_allow_button"
    force_permission_id = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    this_permission_id = "com.android.permissioncontroller:id/permission_allow_one_time_button"
    deny_permission_id = "com.android.permissioncontroller:id/permission_deny_button"
    manualmatches_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.run567:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']"
    manualteamname_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.run567:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']/../../../../android.widget.RelativeLayout//androidx.appcompat.widget.LinearLayoutCompat//android.widget.RelativeLayout/android.widget.TextView[1]"
    match_date_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.run567:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']/../../../../../android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
    wintossback_xpath = "//android.widget.TextView[@text='TO WIN THE TOSS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]//android.widget.LinearLayout/android.widget.LinearLayout[@resource-id='com.subagent.run567:id/flBack']"
    inp_betprice_id = "com.subagent.run567:id/edt_stack"
    btn_placebet_id = "com.subagent.run567:id/btnBet"
    tost_xpath = "//android.widget.Toast[1]"
    cricket_xpath = "//android.widget.HorizontalScrollView//android.widget.LinearLayout[2]"
    logo_id = "com.subagent.run567:id/txtUser"
    walletamount_id = "com.subagent.run567:id/txt_wallet"
    exposure_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.run567:id/rv_wallet']/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id='com.subagent.run567:id/txt_amount']"
    bonus_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.run567:id/rv_wallet']/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id='com.subagent.run567:id/txt_amount']"
    deposit_id = "com.subagent.run567:id/btn_deposit"
    setting_id = "com.subagent.run567:id/iv_mode"
    switch_id = "com.subagent.run567:id/switch_mode"
    db_openbets_id = "com.subagent.run567:id/txt_match_unmatch"
    db_runnername_id = "com.subagent.run567:id/txtRunnerName"
    db_oddsrate_id = "com.subagent.run567:id/txtOddRate"
    db_stackrate_id = "com.subagent.run567:id/txtStackRate"
    db_pl_id = "com.subagent.run567:id/txtPLRate"
    close_openbets_id = "com.subagent.run567:id/fab_close"
    close_wagerdialog_id = "com.subagent.run567:id/iv_close"
    casino_id = "com.subagent.run567:id/menu_schedule"
    promotion_id = "com.subagent.run567:id/menu_cric_info"
    menu_id = "com.subagent.run567:id/menu_setting"
    home_id = "com.subagent.run567:id/menu_setting"
    center_menu_id = "com.subagent.run567:id/fab_center"
    btn_openbets_xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.run567:id/rv_menu_list']/android.widget.LinearLayout[4]"
    rp_runnername_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.run567:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[1]"
    rp_oddsrate_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.run567:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[1]"
    rp_stackrate_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.run567:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[2]"
    rp_pl_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.run567:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[3]"
    rp_bettype_xpath = "//androidx.cardview.widget.CardView[@resource-id='com.subagent.run567:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[2]"
    cricketmatches_xpath = "//android.widget.HorizontalScrollView[@resource-id='com.subagent.run567:id/sportTab']/android.widget.LinearLayout/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id='com.subagent.run567:id/txt_total_sports']"
    drawer_xpath = '//android.widget.ImageButton[@content-desc="Open navigation drawer"]'
    drawerlive_id = "com.subagent.run567:id/txt_live_events"
    drawerupcoming_id = "com.subagent.run567:id/txt_upcoming"
    inplay_xpath = "//android.widget.TextView[@text='In-Play']"
    livematchlist_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.run567:id/llHeader']"
    market_status_xpath = "//android.widget.TextView[@text='MATCH ODDS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id='com.subagent.run567:id/titleLayout']/following-sibling::android.widget.TextView[1]"
    inplaymatces_xpath = "//android.widget.HorizontalScrollView[@resource-id='com.subagent.run567:id/sportTab']/android.widget.LinearLayout/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id='com.subagent.run567:id/txt_inplay']"
    inplay_teamname_xpath = "//android.widget.RelativeLayout[@resource-id='com.subagent.run567:id/llHeader']//android.widget.TextView[@resource-id='com.subagent.run567:id/txt_team1']"
    matchodds_back_xpath = "//android.widget.TextView[@text='MATCH ODDS']/../../../../../android.widget.RelativeLayout//androidx.recyclerview.widget.RecyclerView[@resource-id='com.subagent.run567:id/runners_recycler']/android.view.ViewGroup[1]//android.widget.LinearLayout[@resource-id='com.subagent.run567:id/flBack']"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 20)

    def scrollmarket(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(546, 1720)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(568, 1500)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def getinplaymatches(self):
        return str(self.driver.find_element(AppiumBy.XPATH, self.inplaymatces_xpath).get_attribute("text"))

    def getcricketmatches(self):
        return str(self.driver.find_element(AppiumBy.XPATH, self.cricketmatches_xpath).get_attribute("text"))

    def clickdrawerupcoming(self):
        self.driver.find_element(AppiumBy.ID, self.drawerupcoming_id).click()

    def clickdrawer(self):
        self.driver.find_element(AppiumBy.XPATH, self.drawer_xpath).click()

    def clickinplay(self):
        self.driver.find_element(AppiumBy.XPATH, self.inplay_xpath).click()

    def setusername(self, username):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.inp_username_id)))
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

    def iswager(self, inp):
        status = self.driver.find_element(AppiumBy.ID, self.switch_id)
        stat = status.get_attribute("checked")
        if stat.lower() == "true" and inp.lower() == "true":
            self.logger.info("Wager Is Selected")
        elif stat.lower() == "false" and inp.lower() == "true":
            status.click()
            self.logger.info("Wager is selected And Now Turn On Real Money")
        elif stat.lower() == "true" and inp.lower() == "false":
            status.click()
            self.logger.info("Real Money is selected And Now Turn On Wager")
        elif stat.lower() == "false" and inp.lower() == "false":
            self.logger.info("Real money is selected")

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
