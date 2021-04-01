import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import utilities


class Driver_Actions:
    def __init__(self):
        pass

    def move_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        self.driver_page_home_action(driver)
        try:
            action = ActionChains(driver)
            action.move_to_element(xElement)
            action.perform()
            #action.perform()
        except Exception as e:
            self.scroll_and_search_into_view_of_xElement(driver, xElement=xElement)
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
        wait = WebDriverWait(driver, 10)
        self.driver_page_home_action(driver)
        i = 0
        flag = False
        for i in range(9):
            if(flag == False):
                try:
                    if(index_location==None):
                        #xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath=myxpath)
                        wait.until(expected_conditions.visibility_of_element_located(By.XPATH, myxpath))
                        try:
                            xElement = driver.find_element_by_xpath(myxpath)
                        except Exception as e00:
                            pass

                    else:
                        wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
                        #xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath=myxpath)
                        try:
                            xElements = driver.find_elements_by_xpath(myxpath)
                            xElement = xElements[int(index_location)]
                        except Exception as e01:
                            pass
                except Exception as e0:
                    pass
                try:
                    #driver.execute_script("arguments[0].scrollIntoView();", xElement)
                    #self.move_cursor_to_webelement(driver, xElement)
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    flag = True
                    return driver
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=1)
        return driver


    def scroll_and_search_into_view_of_element(self, driver, myxpath=None, index_location=None):
        xElement = None
        xElements = None
        wait = WebDriverWait(driver, 10)
        self.driver_page_home_action(driver)
        i = 0
        flag = False
        for i in range(9):
            if(flag == False):
                try:
                    if(index_location==None):
                        try:
                            wait.until(expected_conditions.visibility_of_element_located(By.XPATH, myxpath))
                            xElement = driver.find_element_by_xpath(myxpath)
                        except Exception as e01:
                            pass
                    else:
                        try:
                            wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
                            xElements = driver.find_elements_by_xpath(myxpath)
                        except Exception as e02:
                            pass
                        try:
                            xElement = xElements[int(index_location)]
                        except Exception as e03:
                            pass
                except Exception as e0:
                    pass
                try:
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    flag = True
                    return driver, xElement
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=1)
                    pass
        return driver, xElement

    def scroll_and_search_into_view_and_click_element(self, driver, myxpath=None, index_location=None):
        xElement = None
        xElements = None
        wait = WebDriverWait(driver, 10)
        self.driver_page_home_action(driver)
        i = 0
        flag = False
        for i in range(9):
            if (flag == False):
                try:
                    if (index_location == None):
                        try:
                            wait.until(expected_conditions.visibility_of_element_located(By.XPATH, myxpath))
                            xElement = driver.find_element_by_xpath(myxpath)
                        except Exception as e01:
                            pass
                    else:
                        try:
                            wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
                            xElements = driver.find_elements_by_xpath(myxpath)
                        except Exception as e02:
                            pass
                        try:
                            xElement = xElements[int(index_location)]
                        except Exception as e03:
                            pass
                except Exception as e0:
                    pass
                try:
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    flag = True
                    xElement.click()
                    return driver
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=1)
                    pass
        print("Clicking on the WebElement Failed")
        try:
            assert False
        except Exception as e00:
            pass
        return driver


    def scroll_and_search_into_view_of_xElement(self, driver, xElement=None):
        i = 0
        flag = False
        wait = WebDriverWait(driver, 10)
        self.driver_page_home_action(driver)
        for i in range(9):
            if(flag == False):
                try:
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement)
                    action.perform()
                    flag = True
                    return driver, xElement
                except Exception as e1:
                    self.driver_page_down_action(driver, my_iterator=1)

        return driver, xElement


class Test_Actions:
    def __init__(self):
        pass

    def mark_test_step_as_failed(self, message="Test Step Failed"):
        try:
            print(message)
            assert False
        except Exception as e:
            print(message)
        return


