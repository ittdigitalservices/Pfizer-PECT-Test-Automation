from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import utilities


class Global_Utils:
    def __self__(self):
        pass

    def find_visible_webelement_by_xpath(self, driver, myxpath):
        self.driver = driver
        self.myxpath = myxpath
        xElement = None
        try:
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.visibility_of_element_located(By.XPATH, myxpath))
            except Exception as e1:
                pass

            try:
                xElement = driver.find_element_by_xpath(myxpath)
            except Exception as e2:
                print("Element may be Hidden or Does not Exist")
                xElements = driver.find_elements_by_xpath(myxpath)
                xElement = xElements[0]
                return xElement
        except Exception as e:
            try:
                print("Element may be Hidden or Does not Exist")
                assert False
            except Exception as e00:
                return None

        return xElement

    def find_visible_webelements_by_xpath(self, driver, myxpath):
        self.driver = driver
        self.myxpath = myxpath
        xElements = None
        try:
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
            except Exception as e1:
                pass

            try:
                xElements = driver.find_elements_by_xpath(myxpath)
            except Exception as e2:
                pass

        except Exception as e:
            pass

        return xElements


    def find_clickable_webelement_by_xpath(self, driver, myxpath):
        self.driver = driver
        self.myxpath = myxpath
        xElement = None
        try:
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.visibility_of_element_located(By.XPATH, myxpath))
            except Exception as e0:
                pass

            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.element_to_be_clickable(By.XPATH, myxpath))
            except Exception as e1:
                pass

            try:
                xElement = driver.find_element_by_xpath(myxpath)
            except Exception as e2:
                pass

        except Exception as e:
            pass

        return xElement


    def find_clickable_webelements_by_xpath(self, driver, myxpath):
        self.driver = driver
        self.myxpath = myxpath
        xElements = None
        try:
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, myxpath))
            except Exception as e0:
                pass

            try:
                wait = WebDriverWait(driver, 10)
                wait.until(expected_conditions.element_to_be_clickable(By.XPATH, myxpath))
            except Exception as e1:
                pass

            try:
                xElements = driver.find_elements_by_xpath(myxpath)
            except Exception as e2:
                pass

        except Exception as e:
            pass

        return xElements

