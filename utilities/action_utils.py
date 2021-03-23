from selenium import webdriver
from selenium.webdriver import ActionChains

class Driver_Actions:
    def __init__(self):
        pass

    def move_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.move_to_element(xElement)
            action.perform()
        except Exception as e:
            pass
        return driver

