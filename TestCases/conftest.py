import os
from pathlib import Path
import pytest
from appium import webdriver
@pytest.fixture
def setup():
    global driver
    cap = {}
    cap["platformName"] = "Android"
    cap["appium:deviceName"] = "RZCT41GHXKR"  # Samsung
    # cap["appium:deviceName"] = "7916a41" # MI
    cap["appium:appPackage"] = "com.subagent.run567"
    cap["appium:appWaitActivity"] = "com.subagent.run567.common.intro.IntroActivity"
    cap["appium:app"] = "C:\\Users\\KEY\\Downloads\\Run567_v1.apk"
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
    # driver.quit()

def pytest_html_report_title(report):
    report.title = "Test Result Report"


def get_project_root() -> Path:
    return Path(__file__).parent.parent

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        filepath = os.getcwd()
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            # file_path = f"http://159.65.148.205:8000/{file_name}"
            file_path = f"{filepath}/{file_name}"
            if file_name:
                html = '<div> <img src="%s"' \
                       ' alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
    # driver.quit()

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_configure(config):
    config._metadata["Project Name"] = "Mainproject"
    config._metadata['Module Name'] = "Test Place Bet"
    config._metadata['Tester'] = "Rock"
    config._metadata['Browser'] = "Chrome"
