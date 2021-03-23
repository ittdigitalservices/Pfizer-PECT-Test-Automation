# coding=utf-8
"""User accesses About PECT Portal and accesses COVID-19 in the Vaccines Page feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import utilities
from utilities.pect_utils import PECT_Common_Utils

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
global myCovid19_Search_Count01
global mycovid19_Search_Count02

def setup():
    global driver
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    yield driver

    try:
        driver.close()
    except Exception as e:
        pass

    try:
        driver.quit()
    except Exception as e:
        pass


feature_name = '../features/PECT_TC003.feature'

scenario_name = 'PECT_TC003_C_Verifies_COVID_19_displayed_data'


@pytest.mark.order(9)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def test_pect_tc003_c_verifies_covid_19_displayed_data():
    """PECT_TC003_C_Verifies_COVID_19_displayed_data."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)


@pytest.mark.order(9)
@given('User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc003_c_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(10)
@then('User clicks on the Find a Trial link')
def test_pect_tc003_c_user_clicks_on_the_find_a_trial_link():
    """User clicks on the Find a Trial link."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Find_a_Trial_Navbar(driver)


@pytest.mark.order(11)
@then('User then accesses the Search Filter')
def test_pect_tc003_c_user_then_accesses_the_search_filter():
    """User then accesses the Search Filter."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Access_Trial_Search_Filter(driver)


@pytest.mark.order(12)
@then('User then searches for COVID-19 and collects certain displayed data like count')
def test_pect_tc003_c_user_searches_COVID_19_and_collects_data_count():
    """User then searches for COVID-19 and collects certain displayed data like count."""
    global driver
    global myCovid19_Search_Count01
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Pfizer_Home_Image(driver)
    mytext = "COVID 19"
    driver = mystep.PECT_Search_Text_in_Find_a_Trial_Search_Filter(driver, mytext, index_location=None)
    driver = mystep.PECT_Click_on_Find_a_Trial_Button(driver, index_location=1)
    try:
        time.sleep(7)
        driver, myCovid19_Search_Count01 = mystep.PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(driver, index_location=1)
    except Exception as e:
        pass
    #print("myCovid19_Search_Count01 = ", myCovid19_Search_Count01)




@pytest.mark.order(13)
@then('User then searches for covid-19 and collects certain displayed data like count')
def test_pect_tc003_c_user_searches_covid19_and_collects_data_count():
    """User then searches for covid-19 and collects certain displayed data like count."""
    global driver
    global mycovid19_Search_Count02
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Pfizer_Home_Image(driver)
    mytext = "covid-19"
    driver = mystep.PECT_Search_Text_in_Find_a_Trial_Search_Filter(driver, mytext, index_location=None)
    driver = mystep.PECT_Click_on_Find_a_Trial_Button(driver, index_location=1)
    try:
        time.sleep(7)
        driver, mycovid19_Search_Count02 = mystep.PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(driver, index_location=1)
    except Exception as e:
        pass
    #print("mycovid19_Search_Count02 = ", mycovid19_Search_Count02)



@pytest.mark.order(14)
@then('User then compares the data collected in the above step004 and step005')
def test_pect_tc003_c_user_compares_data_from_step004_and_step005():
    """User then compares the data collected in the above step004 and step005."""
    global myCovid19_Search_Count01
    global mycovid19_Search_Count02
    assert(myCovid19_Search_Count01 == mycovid19_Search_Count02)


def teardown():
    from utilities.screenshot_utils import test_failed_check
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    test_failed_check(driver, scenario_name=scenario_name)
    # driver.quit()



