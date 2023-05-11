from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, TimeoutException
from Utilities.customlogger import Logger
from PageObjects.Run567 import Run567
import pytest

class Test_Run567:
    logger = Logger.logen()
    username = "sp25"
    password = "Test@1234"

    @pytest.mark.test
    def test_001(self, setup):
        # Test Starting
        messagelist = []
        self.driver = setup
        self.driver.implicitly_wait(15)
        self.rn = Run567(self.driver)
        # Go Through Intro Screen
        self.rn.clickskip()
        self.rn.clickletsgetstarted()
        # Login Activity
        self.rn.setusername(self.username)
        self.rn.setpassword(self.password)
        self.driver.find_element(AppiumBy.ID, self.rn.redio_keepmesign_id).click()
        self.rn.clicklogin()
        # ckeck if any message for any failure
        try:
            message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                        (AppiumBy.XPATH, self.rn.tost_xpath))).get_attribute("text")
            self.logger.info("User not login message = %s", message)
        except TimeoutException or NoSuchElementException:
            self.logger.info("Login Successful, login with %s", self.username)
        try:
            self.rn.clicknotsavepassword()
        except TimeoutException:
            pass
        try:
            self.rn.clickagree()
        except TimeoutException:
            pass
        """ check home page is display after login to application """
        if self.driver.find_element(AppiumBy.ID, self.rn.logo_id).is_displayed():
            preexp = self.rn.getexposure()
            prewlt = self.rn.getwalletamount()
            self.logger.info("User Wallet amount before bet place= %s", prewlt)
            self.logger.info("User exposure amount before bet place = %s", preexp)
            self.rn.clicksetting()
            self.rn.iswager("false")
            self.rn.clickclosewagerdialog()
            self.rn.clickcricket()
            self.rn.scrollmarket()
            match_names = []
            dates = []
            totalmatches = int(self.rn.getcricketmatches())
            is_inplay = False
            for j in range(int(totalmatches/8+1)):
                element = self.driver.find_elements(AppiumBy.XPATH, self.rn.manualmatches_xpath)
                wintoss_team1 = self.driver.find_elements(AppiumBy.XPATH, self.rn.wintoss_team1_xpath)
                wintoss_team2 = self.driver.find_elements(AppiumBy.XPATH, self.rn.wintoss_team2_xpath)
                date = self.driver.find_elements(AppiumBy.XPATH, self.rn.match_date_xpath)
                for i in range(len(element)):
                    element = self.driver.find_elements(AppiumBy.XPATH, self.rn.manualmatches_xpath)
                    try:
                        dt = date[i].get_attribute("text")
                        wintoss_team1_name = wintoss_team1[i].get_attribute("text")
                        wintoss_team2_name = wintoss_team2[i].get_attribute("text")
                        wintoss_marketname = wintoss_team1_name + " VS " + wintoss_team2_name
                        if wintoss_team1_name in match_names:
                            ind = match_names.index(wintoss_team1_name)
                            if dt not in dates[ind]:
                                element[i].click()
                                self.rn.clickwintossback()
                                self.rn.setbetprice(100)
                                self.rn.clickplacebet()
                                try:
                                    messagetext = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                        (AppiumBy.XPATH, self.rn.tost_xpath))).get_attribute("text")
                                    messagelist.append(messagetext)

                                    if "Bet has been placed successfully." in messagelist:
                                        is_inplay = True
                                        self.logger.info(
                                            "Bet has been placed successfully Market Name is %s and message after bet place = %s ",
                                            wintoss_marketname, messagetext)
                                        break

                                    else:
                                        self.logger.info(
                                            "Bet Not Placed, Market Name is %s and message after bet place = %s ",
                                            wintoss_marketname, messagetext)
                                        self.driver.back()
                                except TimeoutException:
                                    pass
                        else:
                            element[i].click()
                            self.rn.clickwintossback()
                            self.rn.setbetprice(100)
                            self.rn.clickplacebet()
                            try:
                                messagetext = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                    (AppiumBy.XPATH, self.rn.tost_xpath))).get_attribute("text")
                                messagelist.append(messagetext)
                                if "Bet has been placed successfully." in messagelist:
                                    is_inplay = True
                                    self.logger.info("Bet has been placed successfully Market Name is %s and message after bet place = %s ", wintoss_marketname, messagetext)
                                    break

                                else:
                                    self.logger.info("Bet Not Placed, Market Name is %s and message after bet place = %s ", wintoss_marketname, messagetext)
                                    self.driver.back()
                            except TimeoutException:
                                pass
                            dates.append(dt)
                            match_names.append(wintoss_team1_name)
                    except Exception as e:
                        # self.logger.info("Error in finding market and place Bet ")
                        self.driver.back()
                if is_inplay:
                    break
                else:
                    self.rn.scrollmarket()

            if not is_inplay:
                self.rn.clickinplay()
                teamnamelist = []
                is_betplace = False
                matchcount = int(self.rn.getinplaymatches())
                loopcount = int(matchcount/6)
                available = False
                if loopcount == 0:
                    loopcount = loopcount + 1
                for h in range(loopcount):
                    inplay_matches = self.driver.find_elements(AppiumBy.XPATH, self.rn.inplay_teamname1_xpath)
                    team2_name = self.driver.find_elements(AppiumBy.XPATH, self.rn.inplay_teamname2_xpath)
                    for k in range(len(inplay_matches)):
                        try:
                            team1_name = inplay_matches[k].get_attribute("text")
                            team_2_name = team2_name[k].get_attribute("text")
                            if team1_name not in teamnamelist:
                                marketname = team1_name + " VS " + team_2_name
                                teamnamelist.append(marketname)
                                inplay_matches[k].click()
                                try:
                                    status = self.driver.find_element(AppiumBy.XPATH, self.rn.market_status_xpath).get_attribute("text")
                                    if status:
                                        self.logger.info("Bet Not place Market Status is %s In market %s", status, marketname)
                                        available = False
                                except NoSuchElementException or TimeoutException:
                                    available = True
                                if available:
                                    self.driver.find_element(AppiumBy.XPATH, self.rn.matchodds_back_xpath).click()
                                    self.rn.setbetprice(100)
                                    self.rn.clickplacebet()
                                    live_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                        (AppiumBy.XPATH, self.rn.tost_xpath))).get_attribute("text")
                                    messagelist.append(live_message)
                                    if "success" in live_message:
                                        is_betplace = False
                                        messagelist.append(live_message)
                                        self.logger.info("Bet placed successfully in market =%s", marketname)
                                        break
                                    else:
                                        self.logger.info("Bet not placed in market =%s and message after betplace = %s", marketname, live_message)
                                        self.driver.back()
                                else:
                                    self.driver.back()
                        except:
                            self.driver.back()
                            self.logger.info("exception occur %s market name = %s", k, teamnamelist[-1])
                    if is_betplace:
                        break
                    else:
                        self.rn.scrollmarket()
            dbdata = []
            isreport_open = False
            isdialog_open = False
            if "Bet has been placed successfully." in messagelist:
                self.logger.info("Bet has been placed successfully")
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((AppiumBy.ID, self.rn.db_openbets_id)))
                    self.rn.clickopenbetdialog()
                    runnername, odds, stake, pl = self.rn.getopenbetdialoginfo()
                    self.logger.info("Below Details From open Bet 'Dialog'")
                    dbdata.append(runnername), self.logger.info("Bet Place Team Name = %s", runnername)
                    dbdata.append(float(odds)), self.logger.info("Bet Odds = %s", odds)
                    dbdata.append(float(stake)), self.logger.info("Bet Stake Amount = %s", stake)
                    dbdata.append(float(pl)), self.logger.info("P/L On Bet = %s", pl)
                    isdialog_open = True

                except:
                    self.logger.info("open bet dialog not available")  # open bet dialog not available
                    pass
                postexp = int(self.rn.getexposure())
                postwlt = int(self.rn.getwalletamount())
                self.logger.info("Wallet Amount After Bet Place = %s", postwlt)
                self.logger.info("Exposure After Bet Place = %s", postexp)

                assert prewlt != postwlt and preexp != postexp, self.logger.info("Wallet Amount and Exposure Not Update After Bet Place ")
                try:
                    self.driver.back()
                    self.rn.clickmenufragement()
                    self.rn.clickopenbetsbtn()
                except:
                    pass

                rpdata = []
                try:
                    rprunnername, rpodds, rpstake, rppl = self.rn.getopenbetreportinfo()
                    self.logger.info("Below Details From open Bet 'Report'")
                    rpdata.append(rprunnername), self.logger.info("Bet Place Team Name = %s", rprunnername)
                    rpdata.append(float(rpodds)), self.logger.info("Bet Odds = %s", rpodds)
                    rpdata.append(float(rpstake)), self.logger.info("Bet Stake Amount = %s", rpstake)
                    rpdata.append(float(rppl)), self.logger.info("P/L On Bet = %s", rppl)
                    isreport_open = True
                except:
                    self.logger.info("Open Bet Report Not Open")  # open bet report not updated
                if isreport_open:
                    actwlt = int(prewlt) - int(rpdata[2])
                    actexp = int(preexp) + int(rpdata[2])
                    assert actwlt == postwlt and actexp == postexp, self.logger.info(
                        "Wallet Amount and Exposure Amount Not Updated After Bet Place")
                    self.logger.info("Test Passed Wallet amount and Exposure is updated after Bet place")
                elif isdialog_open:
                    actwlt = int(prewlt) - int(dbdata[2])
                    actexp = int(preexp) + int(dbdata[2])
                    assert actwlt == postwlt and actexp == postexp, self.logger.info("Wallet Amount and Exposure Amount Not Updated After Bet Place")
                    self.logger.info("Test Passed Wallet amount and Exposure is updated after Bet place")
            else:
                self.driver.back()

        else:
            self.logger.info("User not login")
