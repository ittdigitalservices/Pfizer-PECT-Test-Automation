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
                    action.move_to_element(xElement).perform()
                    #action.perform()
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
        #wait = WebDriverWait(driver, 10)
        #utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
        #self.driver_page_home_action(driver)
        try:
            time.sleep(1)
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


    def check_webelement_existence_using_xpath(self, driver, myxpath=None, index_location=None):
        xElements = None
        xElement = None
        try:
            time.sleep(1)
            xElements = driver.find_elements_by_xpath(myxpath)
        except Exception as e0:
            pass

        if((index_location != None) and (xElements != None)):
            try:
                xElement = xElements[int(index_location)]
                return xElement, True
            except Exception as e1:
                return None, False
        else:
            try:
                xElement = xElements[0]
                if(xElement != None):
                    return xElement, True
                else:
                    try:
                        xElement = driver.find_element_by_xpath(myxpath)
                        if(xElement != None):
                            return xElement, True
                    except Exception as e2:
                        return None, False
            except Exception as e3:
                return None, False

    def send_double_click_actions(self, driver, myxpath=None, index_location=0):
        xElements = None
        xElement = None

        try:
            xElements = driver.find_elements_by_xpath(myxpath)
        except Exception as e01:
            pass

        try:
            xElement = xElements[int(index_location)]
        except Exception as e02:
            pass

        try:
            action = ActionChains(driver)
            action.double_click(on_element=xElement)
            action.perform()

        except Exception as e03:
            pass

        return driver


    def send_Tab_Keys_using_driver_actions(self, driver, counter=1):
        i = 0
        for i in range(counter):
            try:
                action = ActionChains(driver)
                action.send_keys(Keys.TAB)
                action.perform()

            except Exception as e00:
                pass

        return driver


    def send_Data_using_driver_actions(self, driver, mydata=None):
        try:
            action = ActionChains(driver)
            action.send_keys(mydata)
            action.perform()

        except Exception as e00:
            pass
        return driver

    def perform_Enter_using_driver_actions(self, driver):
        try:
            action = ActionChains(driver)
            action.send_keys(Keys.ENTER)
            action.perform()

        except Exception as e00:
            pass
        return driver
