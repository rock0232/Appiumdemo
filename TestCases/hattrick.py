import time
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from pathlib import Path
import os
# from TestCases.conftest import appfilepath
from PageObjects.B2B import B2B
from Utilities import xlutils
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


# import conftest
# driver = None
conftest_driver = []

# @pytest.fixture(params=xlutils.read_sheet(columnname="Application Package Name"))
# def apppackagename(request):
#     return request.param
#
#
# @pytest.fixture(params=xlutils.read_sheet(columnname="File Path"))
# def appfilepath(request):
#     return request.param


def getalldata():
    keys = xlutils.read_sheet("Application Package Name")
    values = xlutils.read_sheet("File Path")

    data_dict = dict(zip(keys, values))
    return data_dict


class Test_hattrick:
    logger = Logger.logen()
    username = "kt11"
    password = "First@666"

    def test_1(self, setup):
        self.driver = setup
        package = self.driver.current_package
        self.cmn = B2B(self.driver, package)
        self.cmn.clickskip()
        assert True == False
