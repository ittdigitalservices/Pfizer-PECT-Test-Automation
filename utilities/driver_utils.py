from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import utilities


class Common_Actions:
    def __init__(self):
        pass

    def move_mouse_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        wait = WebDriverWait(driver, 10)
        utilities.action_utils.Driver_Actions().driver_page_home_action(driver)

        #self.driver_page_home_action(driver)
        try:
            action = ActionChains(driver)
            action.move_to_element(xElement)
            action.perform()
        except Exception as e00:
            utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_xElement(driver, xElement=xElement)
        #action.perform()
        return driver


    def switch_to_my_window_handle(self, driver, handle_index=0):
        try:
            #driver.switch_to_window[handle_index]
            action = ActionChains(driver)
            action.send_keys(Keys.CONTROL + Keys.TAB)
            action.perform()

        except Exception as e0:
            pass

        return driver