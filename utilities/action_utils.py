from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import utilities


class Driver_Actions:
    def __init__(self):
        pass

    def move_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.move_to_element(xElement).perform()
            #action.perform()
        except Exception as e:
            pass
        return driver


    def driver_page_down_action(self, driver, my_iterator=0):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            i = 0
            for i in range(int(my_iterator)):
                try:
                    action.send_keys(Keys.PAGE_DOWN)
                    action.perform()
                except Exception as e0:
                    pass

        except Exception as e1:
            pass
        return driver


    def driver_page_home_action(self, driver):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.send_keys(Keys.HOME)
            action.perform()
        except Exception as e0:
            pass
        return driver


    def driver_page_pause_action(self, driver):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.send_keys(Keys.PAUSE)
            action.perform()
        except Exception as e1:
            pass
        return driver


    def scroll_into_view_of_element(self, driver, myxpath=None, index_location=None):
        xElement = None
        xElements = None
        try:
            if(index_location==None):
                xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath=myxpath)
            else:
                xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath=myxpath)
                xElement = xElements[int(index_location)]
        except Exception as e0:
            pass
        try:
            driver.execute_script("arguments[0].scrollIntoView();", xElement)
        except Exception as e1:
            pass
        return driver


    def scroll_and_search_into_view_of_element(self, driver, myxpath=None, index_location=None):
        xElement = None
        xElements = None
        
        self.driver_page_home_action(driver)
        i = 0
        flag = False
        for i in range(21):
            if(flag == False):
                try:
                    if(index_location==None):
                        xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath=myxpath)
                    else:
                        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath=myxpath)
                        xElement = xElements[int(index_location)]
                except Exception as e0:
                    pass
                try:
                    self.move_cursor_to_webelement(driver, xElement)
                    flag = True
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=0)
                    pass
        return driver, xElement

    def scroll_and_search_into_view_and_click_element(self, driver, myxpath=None, index_location=None):
        xElement = None
        xElements = None

        self.driver_page_home_action(driver)
        i = 0
        flag = False
        for i in range(21):
            if (flag == False):
                try:
                    if (index_location == None):
                        xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver,
                                                                                                       myxpath=myxpath)
                    else:
                        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver,
                                                                                                         myxpath=myxpath)
                        xElement = xElements[int(index_location)]
                except Exception as e0:
                    pass
                try:
                    self.move_cursor_to_webelement(driver, xElement)
                    flag = True
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=0)
                    pass
        xElement.click()
        return driver


class Test_Actions:
    def __init__(self):
        pass

    def mark_test_step_as_failed(self, message="Test Step Failed"):
        try:
            assert False
            print(message)
        except Exception as e:
            print(message)


