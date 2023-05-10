from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from Utilities.customlogger import Logger
from PageObjects.Run567 import Run567
import pytest

class Test_Run567:
    logger = Logger.logen()
    username = "kt11"
    password = "First@666"

    @pytest.mark.test
    def test_001(self, setup):
        # Test Starting
        message1 = []
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
            message = self.driver.find_element(AppiumBy.XPATH, self.rn.tost_xpath)
            self.logger.info("User not login message = %s", message.get_attribute("text"))
        except NoSuchElementException:
            self.logger.info("Login Successful, login with %s", self.username)
        try:
            self.rn.clicknotsavepassword()
        except:
            pass
        try:
            self.rn.clickagree()
        except:
            pass
        # check home page is display after login to application
        if self.driver.find_element(AppiumBy.ID, self.rn.logo_id).is_displayed():
            preexp = self.rn.getexposure()
            prewlt = self.rn.getwalletamount()
            self.logger.info("User Wallet amount before bet place= %s", prewlt)
            self.logger.info("User exposure amount before bet place = %s", preexp)
            self.rn.clicksetting()
            self.rn.iswager("false")
            self.rn.clickclosewagerdialog()
            self.rn.clickcricket()
            # self.rn.scrollmarket()
            match_names = []
            dates = []
            totalmatches = int(self.rn.getcricketmatches())
            success = False
            # for j in range(int(totalmatches/8+1)):
            #     element = self.driver.find_elements(AppiumBy.XPATH, self.rn.manualmatches_xpath)
            #     name = self.driver.find_elements(AppiumBy.XPATH, self.rn.manualteamname_xpath)
            #     date = self.driver.find_elements(AppiumBy.XPATH, self.rn.match_date_xpath)
            #     for i in range(len(element)):
            #         element = self.driver.find_elements(AppiumBy.XPATH, self.rn.manualmatches_xpath)
            #         try:
            #             dt = date[i].get_attribute("text")
            #             mtch = name[i].get_attribute("text")
            #             if mtch in match_names:
            #                 ind = match_names.index(mtch)
            #                 if dt in dates[ind]:
            #                     pass
            #                 else:
            #                     element[i].click()
            #                     self.rn.clickwintossback()
            #                     self.rn.setbetprice(100)
            #                     # self.rn.clickplacebet()
            #
            #                     try:
            #                         message = self.driver.find_element(AppiumBy.XPATH, self.rn.tost_xpath)
            #                         messagetext = message.get_attribute("text")
            #                         message1.append(messagetext)
            #                     except:
            #                         pass
            #
            #                     if "Bet has been placed successfully." in message1:
            #                         success = True
            #                         break
            #                     else:
            #                         self.driver.back()
            #             else:
            #                 element[i].click()
            #                 self.rn.clickwintossback()
            #                 self.rn.setbetprice(100)
            #                 # self.rn.clickplacebet()
            #                 try:
            #                     message = self.driver.find_element(AppiumBy.XPATH, self.rn.tost_xpath)
            #                     messagetext = message.get_attribute("text")
            #                     message1.append(messagetext)
            #                 except:
            #                     pass
            #                 if "Bet has been placed successfully." in message1:
            #                     success = True
            #                     break
            #                 else:
            #                     self.driver.back()
            #                 dates.append(dt)
            #                 match_names.append(mtch)
            #         except Exception as e:
            #             # self.logger.info("Error in finding market and place Bet  %s", e)
            #             self.driver.back()
            #     if success:
            #         break
            #     else:
            #         self.rn.scrollmarket()

            if not success:
                self.rn.clickinplay()
                teamname = []
                live_status = False
                matchcount = int(self.rn.getinplaymatches())
                loopcount = int(matchcount/6)
                available = False
                if loopcount == 0:
                    loopcount = loopcount + 1
                for h in range(loopcount):
                    livematches = self.driver.find_elements(AppiumBy.XPATH, self.rn.inplay_teamname_xpath)
                    for k in range(len(livematches)):
                        try:
                            tmname = livematches[k].get_attribute("text")
                            if tmname not in teamname:
                                teamname.append(tmname)
                                livematches[k].click()
                                try:
                                    status = self.driver.find_element(AppiumBy.XPATH, self.rn.market_status_xpath).get_attribute("text")
                                    if status:
                                        self.logger.info("Bet Not place Market Status is %s In Match Name Starts With %s", status, tmname)
                                        available = False
                                except:
                                    available = True
                                if available:
                                    self.driver.find_element(AppiumBy.XPATH, self.rn.matchodds_back_xpath).click()
                                    self.rn.setbetprice(100)
                                    # self.rn.clickplacebet()
                                    # live_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                                    #     (AppiumBy.XPATH, self.rn.tost_xpath))).get_attribute("text")

                                    # live_message = self.driver.find_element(AppiumBy.XPATH, self.rn.tost_xpath).get_attribute("text")
                                    live_message = "test"
                                    message1.append("true")
                                    self.logger.info("Enter into market successfully match name =%s", tmname)
                                    if "success" in live_message:
                                        live_status = True
                                        message1.append(live_message)
                                        break
                                    else:
                                        self.driver.back()
                                else:
                                    self.driver.back()

                        except:
                            self.driver.back()
                            self.logger.info("exception occur %s match team name = %s", k, teamname)
                    if live_status:
                        break
                    else:
                        self.rn.scrollmarket()
            dbdata = []

            if "success" in message1[0]:
                self.logger.info("Bet has been placed successfully")
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((AppiumBy.ID, self.rn.db_openbets_id)))
                    self.rn.clickopenbetdialog()
                    runnername, odds, stake, pl = self.rn.getopenbetdialoginfo()
                    dbdata.append(runnername), self.logger.info("Bet Place Team Name = %s", runnername)
                    dbdata.append(float(odds)), self.logger.info("Bet Odds = %s", odds)
                    dbdata.append(float(stake)), self.logger.info("Bet Stake Amount = %s", stake)
                    dbdata.append(float(pl)), self.logger.info("P/L On Bet = %s", pl)

                except:
                    self.logger.info("open bet dialog not available")  # open bet dialog not available
                    pass
                postexp = int(self.rn.getexposure())
                self.logger.info("Exposure After Bet Place = %s", postexp)
                postwlt = int(self.rn.getwalletamount())
                self.logger.info("Wallet Amount After Bet Place = %s", postwlt)

                self.driver.back()
                self.rn.clickmenufragement()
                self.rn.clickopenbetsbtn()
                rpdata = []
                try:
                    rprunnername, rpodds, rpstake, rppl = self.rn.getopenbetreportinfo()
                    rpdata.append(rprunnername), self.logger.info("Bet Place Team Name = %s", rprunnername)
                    rpdata.append(float(rpodds)), self.logger.info("Bet Odds = %s", rpodds)
                    rpdata.append(float(rpstake)), self.logger.info("Bet Stake Amount = %s", rpstake)
                    rpdata.append(float(rppl)), self.logger.info("P/L On Bet = %s", rppl)
                except:
                    self.logger.info("Open Bet Report Not Open")  # open bet report not updated
                actwlt = int(prewlt) - int(rpdata[2])
                actexp = int(preexp) + int(rpdata[2])

                assert actwlt == postwlt and actexp == postexp, self.logger.info("Wallet Amount and Exposure Amount Not Updated After Bet Place")
                self.logger.info("Test Passed Wallet amount and Exposure is updated after Bet place")
            else:
                self.driver.back()

        else:
            self.logger.info("User not login")
