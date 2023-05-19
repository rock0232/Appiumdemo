from appium import webdriver
import other_file

# Create the driver instance
cap = {"platformName": "Android", "appium:deviceName": "7916a41", "appium:appPackage": "com.subagent.run567",
       "appium:appWaitActivity": "com.subagent.run567.common.intro.IntroActivity",
       "appium:app": "C:\\Users\\KEY\\Downloads\\Run567_v2.apk"}

driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)

# Export the driver instance as a global variable
driver_instance = driver

# Perform test steps using the driver instance
# driver.find_element_by_id("element-id").click()
# ...

# driver.quit()
