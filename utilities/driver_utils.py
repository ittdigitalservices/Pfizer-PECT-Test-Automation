import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import utilities


class Common_Actions:
    def __init__(self):
        pass

    def retry_move_cursor_to_webelement(self, driver, xElement):
        i = 0
        flag = False
        for i in range(7):
            if(flag == False):
                try:
                    time.sleep(1)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    flag = True
                    #return driver
                except Exception as e00:
                    pass
        return driver


    def retry_my_click(self, driver, xElement=None, counter=0):
        i =0
        flag = False
        for i in range(counter):
            if (flag == False):
                try:
                    time.sleep(1)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    try:
                        xElement.click()
                        flag = True
                        return driver
                    except Exception as e01:
                        pass
                except Exception as e00:
                    pass
        return driver

    def move_mouse_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        wait = WebDriverWait(driver, 10)
        #utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
        #self.driver_page_home_action(driver)
        try:
            time.sleep(3)
            myX = xElement.location['x']
            myY = xElement.location['y']
            size = xElement.size
            w = size['width']
            h = size['height']
            #print(str(myX) + " " + str(myY))
            #print("Width = " + str(w) + ", Height = " + str(h))
            action = ActionChains(driver)
            action.move_by_offset(int(myX), int(myY)).perform()
            action.move_to_element(xElement).perform()
            #action.perform()
            #return driver
        except Exception as e00:
            self.retry_move_cursor_to_webelement(driver, xElement)
            #utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_xElement(driver, xElement=xElement)
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