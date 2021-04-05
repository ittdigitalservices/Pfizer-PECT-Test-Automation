import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pom
import utilities
from pom.pect_pom import PECT_WebElement_Locators

"""This Class is PECT Common Contributed Utilities"""
class PECT_Common:
    def __int__(self):
        pass


class PECT_Common_Utils:
    def __init__(self):
        pass

    global myPECT_Hover_Counter
    myPECT_Hover_Counter = 0

    def PECT_Accept_Cookies(self, driver):
        myxpath = PECT_WebElement_Locators().agree_to_accept_cookies
        xElement = utilities.web_utils.Global_Utils().find_clickable_webelement_by_xpath(driver, myxpath)
        driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)

        try:
            xElement.click()
        except Exception as e:
            try:
                xElement.click()
            except Exception as e01:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Object Failed")
                pass
        return driver


    def PECT_About_Clinical_Trials(self, driver):
        import selenium
        xElement = None
        xElements = None
        myxpath = PECT_WebElement_Locators().about_clinical_trials

        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            xElement = xElements[0]
        except Exception as e00:
            pass

        driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)

        try:
            try:
                xElement.click()
            except Exception as e01:
                try:
                    utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
                except Exception as e02:
                    utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Object Failed")
                    assert False
        except Exception as e03:
            return driver
        return driver


    def PECT_Hover_About_Clinical_Trials(self, driver):
        import utilities
        xElements = None
        xElement = None
        myxpath = PECT_WebElement_Locators().about_clinical_trials

        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            xElement = xElements[0]
        except Exception as e00:
            pass
        try:
            mystep = utilities.driver_utils.Common_Actions()
            driver = mystep.retry_move_cursor_to_webelement(driver, xElement)
        except Exception as e01:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Hover to Object Failed")
            assert False
        return driver


    def PECT_Home_Page_Logo(self, driver):
        myxpath = PECT_WebElement_Locators().home_page_logo
        xElements = None
        xElement = None
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            xElement = xElements[0]
        except Exception as e00:
            pass

        try:
            mystep = utilities.driver_utils.Common_Actions()
            driver = mystep.retry_move_cursor_to_webelement(driver, xElement)
        except Exception as e1:
            pass

        try:
            xElement.click()
        except Exception as e2:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e3:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Home Logo Object Failed")
                assert False
        return driver


    def PECT_Pfizer_Home_Image(self, driver):
        myxpath = PECT_WebElement_Locators().pfizer_home_image
        xElements = None
        xElement = None
        try:
            xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        except Exception as e00:
            pass

        try:
            xElement = xElements[0]
        except Exception as e01:
            pass
        try:
            mystep = utilities.driver_utils.Common_Actions()
            driver = mystep.retry_move_cursor_to_webelement(driver, xElement)
        except Exception as e02:
            pass

        try:
            xElement.click()
        except Exception as e03:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e04:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Home Image Object Failed")
                assert False
        return driver


    def PECT_How_Clinical_Trial_Works(self, driver):
        myxpath = PECT_WebElement_Locators.how_clinical_trial_works
        xElements = None
        xElement = None
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            xElement = xElements[0]
        except Exception as e00:
            pass
        utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)
        try:
            xElement.click()
        except Exception as e01:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e02:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Clinical Trial Works Failed")
                assert False
        return driver


    def PECT_Our_Research(self, driver):
        myxpath = PECT_WebElement_Locators.our_research
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        xElement = None
        try:
            xElement = xElements[0]
        except Exception as e:
            pass

        try:
            xElement.click()
        except Exception as e00:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e01:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Our Research Object Failed")
                assert False
        return driver


    def PECT_Vaccines(self, driver):
        myxpath = PECT_WebElement_Locators.vaccines
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        xElement = None
        try:
            xElement = xElements[1]
        except Exception as e00:
            pass

        try:
            self.PECT_Hover_About_WebElement(driver, xElement)
        except Exception as e01:
            try:
                utilities.action_utils.Driver_Actions().retry_move_cursor_to_webelement(driver, xElement)
            except Exception as e02:
                pass
        try:
            xElement.click()
        except Exception as e03:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e04:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on PECT Vaccines Failed")
                assert False
        return driver


    def PECT_COVID_19_Trial_Info_Text(self, driver):
        myxpath = PECT_WebElement_Locators.pfizer_COVID_19_trial_info_text
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        xElement = None

        try:
            xElement = xElements[0]
        except Exception as e:
            pass

        try:
            self.PECT_Hover_About_WebElement(driver, xElement)
            xElements[0].click()
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Search for Covid19 Trial Text Failed")
            assert False
        return driver


    def PECT_Find_COVID_19_Trial_Info(self, driver):
        myxpath = PECT_WebElement_Locators.find_pfizer_COVID_19_trial_info
        try:
            driver = utilities.browser_utils.MyBrowser().hover_and_click_on_web_element(driver, myxpath, index_location=0)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Search for Covid19 Info Failed")
            assert False
        return driver


    def PECT_Hover_About_WebElement(self, driver, xElement):
        import utilities

        try:
            mystep = utilities.driver_utils.Common_Actions()
            driver = mystep.move_mouse_cursor_to_webelement(driver, xElement)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Hover over WebElement Object Failed")
            assert False
        return driver



    def PECT_Find_a_Trial_Navbar(self, driver):
        myxpath = PECT_WebElement_Locators.pfizer_find_a_trial_navbar

        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            self.PECT_Hover_About_WebElement(driver, xElements[0])
            xElements[0].click()
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Navbar Object Failed")
            assert False
        return driver


    def PECT_Hover_Over_Show_Filters(self, driver):
        myxpath = PECT_WebElement_Locators.pfizer_show_filters_link

        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)

        try:
            self.PECT_Hover_About_WebElement(driver, xElements[0])
            #xElements[0].click()
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Hover Over Show Filters Object Failed")
            assert False
        return driver


    def PECT_Access_Trial_Search_Filter(self, driver):
        myxpath = PECT_WebElement_Locators.pfizer_find_a_trial_search_filter

        try:
            xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        except Exception as e00:
            pass

        try:
            xElement = xElements[0]
        except Exception as e01:
            pass

        try:
            self.PECT_Hover_About_WebElement(driver, xElement)
        except Exception as e02:
            pass

        try:
            xElement.click()
        except Exception as e03:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
            except Exception as e:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Search Filter Object Failed")
                assert False
        return driver


    def PECT_CoronaVirus_COVID_2019_info(self, driver):
        myxpath = PECT_WebElement_Locators.coronavirus_COVID_2019
        #utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
        xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        xElement = None
        try:
            xElement = xElements[0]
        except Exception as e:
            pass

        try:
            self.PECT_Hover_About_WebElement(driver, xElement)
        except Exception as e:
            pass
        try:
            xElement.click()
        except Exception as e:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
                return driver
            except Exception as e1:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on Covid19 info Object Failed")
                assert False
        return driver


    def PECT_About_Clinical_Trials_Text(self, driver):
        myxpath = PECT_WebElement_Locators().about_clinical_trials_text
        xElement = None
        try:
            xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath)
        except Exception as e:
            pass

        try:
            utilities.action_utils.Driver_Actions().move_cursor_to_webelement(driver, xElement)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Clinical Trial Object Text was not found")
            assert False
        return driver


    def PECT_About_Clinical_Trials_Link(self, driver):
        myxpath = PECT_WebElement_Locators().about_clinical_trials_link
        xElement = None
        try:
            xElement = utilities.web_utils.Global_Utils().find_visible_webelement_by_xpath(driver, myxpath)
        except Exception as e:
            pass

        try:
            xElement.click()
        except Exception as e:
            try:
                utilities.driver_utils.Common_Actions().retry_my_click(driver, xElement=xElement, counter=2)
                return driver
            except Exception as e0:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Click on About Clinical Trials Failed")
                assert False
        return driver


    def PECT_Search_Text_in_Find_a_Trial_Search_Filter(self, driver, mytext, index_location=None):
        myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_search_filter
        try:
            driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath, index_location=index_location, mytext=mytext)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Search for Text in Trial Filter Failed")
            assert False
        return driver


    def PECT_Click_on_Find_a_Trial_Button(self, driver, index_location=0):
        myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_trial_button
        try:
            driver, xElement = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=index_location)
            #driver = utilities.browser_utils.MyBrowser().hover_and_click_on_web_element(driver, myxpath, index_location=index_location)
        except Exception as e:
            pass

        try:
            xElement.click()
        except Exception as e:
            try:
                utilities.action_utils.Driver_Actions().retry_my_click(driver, xElement=xElement, counter=2)
                return driver
            except Exception as e1:
                utilities.action_utils.Test_Actions().mark_test_step_as_failed("Search for Trial Button Failed")
                assert False
        return driver


    def PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(self, driver, index_location=0):
        mytext = None
        mycount = 0
        myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_search_filter_result

        try:
            driver, mytext = utilities.browser_utils.MyBrowser().hover_and_get_text_from_web_element(driver, myxpath=myxpath, index_location=index_location)
        except Exception as e0:
            pass
        try:
            #print(mytext)
            mycount = (mytext.split(" "))[0]
        except Exception as e1:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Get Count Failed")
            assert False

        return driver, mycount


    def PECT_Navigate_to_Page_End(self, driver, myxpath, index_location=None):
        try:
            driver = utilities.browser_utils.MyBrowser.navigate_to_end_of_the_page(driver, myxpath, index_location=index_location)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Navigation to Page End Failed")
            assert False
        return driver

    def PECT_Navigate_to_End_of_Page(self, driver):
        try:
            #driver = utilities.browser_utils.MyBrowser.navigate_to_end_of_the_page(driver, myxpath, index_location=index_location)
            driver = utilities.browser_utils.MyBrowser().navigate_to_page_end(driver)
        except Exception as e:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Navigation to Page End Failed")
            assert False
        return driver



    def PECT_Hover_Over_a_WebElement_and_Click_it(self, driver, myxpath, index_location=None):
        """
        try:
            #driver = utilities.browser_utils.MyBrowser().hover_and_click_on_web_element(driver, myxpath, index_location=index_location)
            driver, xElement = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=index_location)
        except Exception as e0:
            pass
        """
        driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=index_location, counter=1)


        """
        try:
            xElement.click()
            utilities.action_utils.Driver_Actions().retry_my_click(driver, xElement=xElement, counter=2)
        except Exception as e1:
            try:
                utilities.action_utils.Driver_Actions().retry_my_click(driver, xElement=xElement, counter=4)
                #return driver
            except Exception as e00:
                try:
                    utilities.action_utils.Test_Actions().mark_test_step_as_failed("Hover Over and Click on Object Failed")
                    assert False
                except Exception as e01:
                    return driver
            """
        return driver


    def PECT_Hover_Over_a_WebElement(self, driver, myxpath, index_location=None):
        xElement = None
        xElements = None

        try:
            xElements = utilities.web_utils.Global_Utils().find_visible_webelements_by_xpath(driver, myxpath)
        except Exception as e00:
            pass

        if(index_location != None):
            try:
                xElement = xElements[int(index_location)]
            except Exception as e01:
                pass
        else:
            try:
                xElement = xElements[0]
            except Exception as e02:
                pass

        try:
            time.sleep(1)
            driver = utilities.driver_utils.Common_Actions().move_mouse_cursor_to_webelement(driver, xElement)
        except Exception as e04:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Curzor Movement to WebElement Failed")
            assert False
        return driver


    def PECT_Get_Text_of_Count_in_a_Result(self, driver, myxpath="", index_location=0):
        mytext = None
        mycount = 0

        try:
            driver, mytext = utilities.browser_utils.MyBrowser().hover_and_get_text_from_web_element(driver, myxpath=myxpath, index_location=index_location)
        except Exception as e0:
            pass

        try:
            print(mytext)
            mycount = (mytext.split(' '))[0]
        except Exception as e1:
            utilities.action_utils.Test_Actions().mark_test_step_as_failed("Get Count from Result Failed")
            assert False
        return driver, mycount


    def PECT_Set_Focus_on_the_WebElement_using_xpath(self, driver, myxpath=None, index_location=None):
        mystep = utilities.action_utils.Driver_Actions()
        driver, xElement = mystep.set_focus_on_the_webelement_using_xpath(driver, myxpath=myxpath, index_location=index_location)
        return driver, xElement
