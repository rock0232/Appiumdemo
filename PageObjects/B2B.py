from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from Utilities.customlogger import Logger


class B2B:
    logger = Logger.logen()

    def __init__(self, driver, apppackagename):
        self.driver = driver
        self.app_package = apppackagename
        self.WebDriverWait = WebDriverWait(self.driver, 7)

        self.btn_next_id = f"{self.app_package}:id/btn_next"
        self.btn_submit_id = f"{self.app_package}:id/btn_submit"
        self.btn_englishlang_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout"
        self.inp_username_id = f"{self.app_package}:id/edtUsername"
        self.inp_password_id = f"{self.app_package}:id/edtPassword"
        self.inp_number_id = f"{self.app_package}:id/edtNumber"
        self.btn_signin_id = f"{self.app_package}:id/btnSignIn"
        self.redio_keepmesign_id = f"{self.app_package}:id/cb_keep_live"
        self.btn_registertext_id = f"{self.app_package}:id/txt_register"
        self.btn_signup_id = f"{self.app_package}:id/btnSignUp"
        self.btn_signintext_id = f"{self.app_package}:id/txt_login"
        self.btn_skip_id = f"{self.app_package}:id/btn_skip"
        self.btn_agree_id = f"{self.app_package}:id/bt_accept"
        self.btn_cancel_id = "android:id/autofill_save_no"
        self.allow_permisssion_id = "com.android.permissioncontroller:id/permission_allow_button"
        self.force_permission_id = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
        self.this_permission_id = "com.android.permissioncontroller:id/permission_allow_one_time_button"
        self.deny_permission_id = "com.android.permissioncontroller:id/permission_deny_button"
        self.manualmatches_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']"
        self.wintoss_team1_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']/../../../../android.widget.RelativeLayout/android.widget.TextView[1]"
        self.wintoss_team2_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']/../../../../android.widget.RelativeLayout/android.widget.TextView[2]"
        self.match_date_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.RelativeLayout[1]//android.widget.TextView[@text='2']/../../../../../android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
        self.wintossback_xpath = f"//android.widget.TextView[@text='TO WIN THE TOSS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]//android.widget.LinearLayout/android.widget.LinearLayout[@resource-id='{self.app_package}:id/flBack']"
        self.inp_betprice_id = f"{self.app_package}:id/edt_stack"
        self.btn_placebet_id = f"{self.app_package}:id/btnBet"
        self.tost_xpath = "//android.widget.Toast[1]"
        self.cricket_xpath = "//android.widget.HorizontalScrollView//android.widget.LinearLayout[2]"
        self.logo_id = f"{self.app_package}:id/txtUser"
        self.walletamount_id = f"{self.app_package}:id/txt_balance"
        self.exposure_id = f"{self.app_package}:id/txt_liability"
        self.bonus_xpath = f"//androidx.recyclerview.widget.RecyclerView[@resource-id='{self.app_package}:id/rv_wallet']/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id='{self.app_package}:id/txt_amount']"
        self.deposit_id = f"{self.app_package}:id/btn_deposit"
        self.setting_id = f"{self.app_package}:id/iv_mode"
        self.switch_id = f"{self.app_package}:id/switch_mode"
        self.db_openbets_id = f"{self.app_package}:id/txt_match_unmatch"
        self.db_runnername_id = f"{self.app_package}:id/txtRunnerName"
        self.db_oddsrate_id = f"{self.app_package}:id/txtOddRate"
        self.db_stackrate_id = f"{self.app_package}:id/txtStackRate"
        self.db_pl_id = f"{self.app_package}:id/txtPLRate"
        self.close_openbets_id = f"{self.app_package}:id/fab_close"
        self.close_wagerdialog_id = f"{self.app_package}:id/iv_close"
        self.casino_id = f"{self.app_package}:id/menu_schedule"
        self.promotion_id = f"{self.app_package}:id/menu_cric_info"
        self.menu_id = f"{self.app_package}:id/menu_setting"
        self.home_id = f"{self.app_package}:id/menu_setting"
        self.center_menu_id = f"{self.app_package}:id/fab_center"
        self.btn_openbets_xpath = "//android.widget.TextView[@text='Open Bets']"
        self.rp_runnername_xpath = f"//androidx.cardview.widget.CardView[@resource-id='{self.app_package}:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[1]"
        self.rp_oddsrate_xpath = f"//androidx.cardview.widget.CardView[@resource-id='{self.app_package}:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[1]"
        self.rp_stackrate_xpath = f"//androidx.cardview.widget.CardView[@resource-id='{self.app_package}:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[2]"
        self.rp_pl_xpath = f"//androidx.cardview.widget.CardView[@resource-id='{self.app_package}:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[3]//android.widget.TextView[3]"
        self.rp_bettype_xpath = f"//androidx.cardview.widget.CardView[@resource-id='{self.app_package}:id/layout_main'][1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[1]//android.widget.TextView[2]"
        self.cricketmatches_xpath = f"//android.widget.HorizontalScrollView[@resource-id='{self.app_package}:id/sportTab']/android.widget.LinearLayout/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id='{self.app_package}:id/txt_total_sports']"
        self.drawer_xpath = '//android.widget.ImageButton[@content-desc="Open navigation drawer"]'
        self.drawerlive_id = f"{self.app_package}:id/txt_live_events"
        self.drawerupcoming_id = f"{self.app_package}:id/txt_upcoming"
        self.inplay_xpath = "//android.widget.TextView[@text='In-Play']"
        self.livematchlist_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']"
        self.market_status_xpath = f"//android.widget.TextView[@text='MATCH ODDS']/../../../../../android.widget.RelativeLayout//android.view.ViewGroup[1]/android.view.ViewGroup[@resource-id='{self.app_package}:id/titleLayout']/following-sibling::android.widget.TextView[1]"
        self.inplaymatces_xpath = f"//android.widget.HorizontalScrollView[@resource-id='{self.app_package}:id/sportTab']/android.widget.LinearLayout/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id='{self.app_package}:id/txt_inplay']"
        self.inplay_teamname1_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.TextView[@resource-id='{self.app_package}:id/txt_team1']"
        self.inplay_teamname2_xpath = f"//android.widget.RelativeLayout[@resource-id='{self.app_package}:id/llHeader']//android.widget.TextView[@resource-id='{self.app_package}:id/txt_team2']"
        self.matchodds_back_xpath = f"//android.widget.TextView[@text='MATCH ODDS']/../../../../../android.widget.RelativeLayout//androidx.recyclerview.widget.RecyclerView[@resource-id='{self.app_package}:id/runners_recycler']/android.view.ViewGroup[1]//android.widget.LinearLayout[@resource-id='{self.app_package}:id/flBack']"
        self.close_banner_id = f"{self.app_package}:id/iv_close_main"
        self.matchebet = f"{self.app_package}:id/txt_match_unmatch"

    def getmatchedcount(self):
        try:
            self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.matchebet)))
            matchtext = self.driver.find_element(AppiumBy.ID, self.matchebet).get_attribute("text")
            txt = []
            for i in matchtext:
                if i != "/":
                    txt.append(i)
                else:
                    break
            matchedbets = "".join(txt)
            return int(matchedbets)
        except:
            return 0

    def getmarketname(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.inplay_teamname1_xpath)))
        team1 = self.driver.find_element(AppiumBy.XPATH, self.inplay_teamname1_xpath).get_attribute("text")
        team2 = self.driver.find_element(AppiumBy.XPATH, self.inplay_teamname2_xpath).get_attribute("text")
        return team1, "vs", team2

    def closebanner(self):
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.close_banner_id)))
        self.driver.find_element(AppiumBy.ID, self.close_banner_id).click()

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
        self.WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.ID, self.inp_betprice_id))).send_keys(
            betprice)

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
        exp = self.driver.find_element(AppiumBy.ID, self.exposure_id).get_attribute("text")
        return float(exp)

    def clickdepostit(self):
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
            self.logger.info("Real Money is selected And Now Turn On Wager")
        elif stat.lower() == "true" and inp.lower() == "false":
            status.click()
            self.logger.info("Wager is selected And Now Turn On Real Money")
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
        return self.WebDriverWait.until(
            EC.visibility_of_element_located((AppiumBy.CLASS_NAME, self.tost_xpath))).get_attribute("text")

    def clickclosewagerdialog(self):
        self.driver.find_element(AppiumBy.ID, self.close_wagerdialog_id).click()
