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
                    return driver
                except Exception as e00:
                    pass
        return driver

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
            self.retry_move_cursor_to_webelement(driver, xElement)
            #self.scroll_and_search_into_view_of_xElement(driver, xElement=xElement)
        return driver


    def move_cursor_to_webelement_by_xpath(self, driver, myxpath=None, index_location=None):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        #self.driver_page_home_action(driver)
        wait = WebDriverWait(driver, 10)
        xElements = None
        xElement = None
        if(index_location == None or index_location == 0):
            try:
                wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
            except Exception as e:
                pass

            try:
                xElements = driver.find_elements_by_xpath(myxpath)
            except Exception as e0:
                pass
            try:
                xElement = xElements[0]
            except Exception as e1:
                pass
        else:
            try:
                wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
            except Exception as e:
                pass

            try:
                xElements = driver.find_elements_by_xpath(myxpath)
            except Exception as e2:
                pass
            try:
                xElement = xElements[int(index_location)]
            except Exception as e3:
                pass

        myX = xElement.location['x']
        myY = xElement.location['y']
        size = xElement.size
        w = size['width']
        h = size['height']
        #print(str(myX) + " " + str(myY))
        #print("Width = " + str(w) + ", Height = " + str(h))

        try:
            action = ActionChains(driver)
            action.move_by_offset(int(myX), int(myY)).perform()
            action.move_to_element(xElement).perform()
            #action.move_by_offset(myX, myY).perform()
            #action.perform()
            #return driver, xElement
        except Exception as e4:
            try:
                self.retry_move_cursor_to_webelement(driver, xElement)
            except Exception as e5:
                pass
        return driver, xElement


    def move_cursor_to_webelement_by_xpath_and_click_it(self, driver, myxpath=None, index_location=None, counter=1):
        driver, xElement = self.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=index_location)
        if (xElement == None):
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Hover Over and Click on Object Failed")
            return driver
        self.retry_my_click(driver, xElement=xElement, counter=counter)
        return driver


    def driver_page_end_action(self, driver):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.send_keys(Keys.CONTROL + Keys.END)
            action.perform()
        except Exception as e1:
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
                    if(index_location != None):
                        try:
                            wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
                            xElements = driver.find_elements_by_xpath(myxpath)
                        except Exception as e01:
                            pass
                        try:
                            xElement = xElements[int(index_location)]
                        except Exception as e02:
                            pass
                    else:
                        try:
                            wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
                            xElements = driver.find_elements_by_xpath(myxpath)
                        except Exception as e03:
                            pass
                        try:
                            xElement = xElements[0]
                        except Exception as e04:
                            pass
                except Exception as e00:
                    pass
                try:
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement).perform()
                    #action.perform()
                    flag = True
                    #return driver, xElement
                except Exception as e5:
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
                    try:
                        xElement.click()
                    except Exception as e04:
                        self.retry_my_click(driver, xElement=xElement, counter=2)
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


    def retry_my_click(self, driver, xElement=None, counter=0):
        i =0
        flag = False
        for i in range(counter):
            if (flag == False):
                try:
                    time.sleep(3)
                    action = ActionChains(driver)
                    action.move_to_element(xElement).perform()
                    # action.perform()
                except Exception as e00:
                    pass
                try:
                    xElement.click()
                    flag = True
                    #return driver
                except Exception as e01:
                    flag = False
        if(flag == False):
            Test_Actions().mark_test_step_as_failed("Click on Object Failed after " + str(counter) + " attempts")
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
        """
        try:
            print(message)
            assert False
        except Exception as e:
            return
        """
        print(message)
        assert False
        return


