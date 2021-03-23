from selenium import webdriver
from selenium.webdriver import ActionChains


class Common_Actions:
    def __init__(self):
        pass

    def move_mouse_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        action.move_to_element(xElement)
        action.perform()
        return driver

