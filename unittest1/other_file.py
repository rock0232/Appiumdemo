# Import the driver instance from test_file.py
from unittest1.test import driver_instance

def test_perform_operation():
    # Use the imported driver instance to perform an operation
    # driver_instance.find_element_by_xpath("//button").click()
    # Perform other operations
    driver = driver_instance
    print(driver.current_activity)
    # ...
