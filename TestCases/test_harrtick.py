import time

from selenium.common import NoSuchElementException
from Utilities.customlogger import Logger
from PageObjects.Hattrickgames import Hattrickgames
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class Test_hattrick:
    logger = Logger.logen()
    username = "kt11"
    password = "First@666"

    def test_001(self, setup):
        self.driver = setup
        self.ht = Hattrickgames(self.driver)
        self.ht.clickskip()
        self.ht.clickletsgetstarted()
        self.ht.setusername(self.username)
        self.ht.setpassword(self.password)
        self.ht.clicklogin()
        try:
            message = self.driver.find_element(AppiumBy.XPATH, self.ht.tost_xpath)
            print(message.get_attribute("text"))
        except NoSuchElementException:
            self.logger.info("Login Successful, login with %s", self.username)
        # try:
        #     self.ht.clicknotsavepassword()
        # except:
        #     pass
        try:
            self.ht.clickagree()
        except:
            pass
        if self.driver.find_element(AppiumBy.ID, self.ht.logo_id).is_displayed():
            preexp = self.ht.getexposure()
            prewlt = self.ht.getwalletamount()

            self.ht.clicksetting()
            self.ht.clickswitch()
            self.ht.clickclosewagerdialog()
            self.ht.clickcricket()
            time.sleep(3)
            element = self.driver.find_elements(AppiumBy.XPATH, self.ht.manualmatches_xpath)
            print(len(element))
            assert True == False

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(482, 1000)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(478, 450)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(5)

            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(482, 1000)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(478, 450)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            time.sleep(5)

            try:
                self.driver.find_element(AppiumBy.XPATH, self.ht.manualmatches_xpath).click()
            except Exception as e:
                print(e)
            self.ht.clickwintossback()
            self.ht.setbetprice(100)
            self.ht.clickplacebet()
            message = self.driver.find_element(AppiumBy.XPATH, self.ht.tost_xpath)
            messagetext = message.get_attribute("text")
            dbdata = []
            if "success" in messagetext:
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, self.ht.db_openbets_id)))
                    self.ht.clickopenbetdialog()
                    runnername, odds, stake, pl = self.ht.getopenbetdialoginfo()
                    dbdata.append(runnername)
                    dbdata.append(float(odds))
                    dbdata.append(float(stake))
                    dbdata.append(float(pl))
                    print(dbdata)
                except:
                    # open bet dialog not available
                    pass
                # print(runnername, odds, stake, pl)
                postexp = int(self.ht.getexposure())
                postwlt = int(self.ht.getwalletamount())

                self.driver.back()
                self.ht.clickmenufragement()
                self.ht.clickopenbetsbtn()
                rpdata = []
                try:
                    rprunnername, rpodds, rpstake, rppl = self.ht.getopenbetreportinfo()
                    rpdata.append(rprunnername)
                    rpdata.append(float(rpodds))
                    rpdata.append(float(rpstake))
                    rpdata.append(float(rppl))
                except:
                    # open bet report not updated
                    pass
                print(rpdata)
                actwlt = int(prewlt) - int(rpdata[2])
                actexp = int(preexp) + int(rpdata[2])

                assert actwlt == postwlt and actexp == postexp
