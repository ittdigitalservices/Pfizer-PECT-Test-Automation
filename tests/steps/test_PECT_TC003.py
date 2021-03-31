# coding=utf-8
"""User accesses About Pfizer Eclinical Trial Portal and accesses COVID-19 in the Vaccines Page feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then, when,
)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import utilities

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
global myCovid19_Search_Count01
global mycovid19_Search_Count02


def setup():
    global driver
    driver.maximize_window()
    yield driver


feature_name = '../features/PECT_TC003.feature'

scenario_name = 'PECT_TC003_A_Access_COVID_19_information'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc003_a_001_access_covid_19_information():
    """PECT_TC003_A_Access_COVID_19_information."""
    print("PECT-TEST003-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC003_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc003_a_001_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC003_A User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc003_a_002_user_verifies_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(3)
@then('PECT_TC003_A User then accesses a COVID-19 information')
def test_pect_tc003_a_003_user_then_accesses_covid19_information():
    """User then accesses a COVID-19 information."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_COVID_19_Trial_Info_Text(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Find_COVID_19_Trial_Info(driver)


scenario_name = 'PECT_TC003_B_verifying_certain_COVID19_information'


@pytest.mark.order(4)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc003_b_004_verifying_certain_covid19_information():
    """PECT_003_B_verifying_certain_COVID19_information."""
    print("PECT-TEST003-SCENARIO-B")
    return


@pytest.mark.order(4)
@when('PECT_TC003_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc003_b_004_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(5)
@then('PECT_TC003_B User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc003_b_005_user_verifies_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(6)
@then('PECT_TC003_B User then clicks on Our Research')
def test_pect_tc003_b_006_user_then_clicks_on_our_research():
    """User then clicks on Our Research."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Our_Research(driver)


@pytest.mark.order(7)
@then('PECT_TC003_B User then accesses the Vaccines and clicks on it')
def test_pect_tc003_b_007_user_then_accesses_vaccines_and_clicks_it():
    """User then accesses the Vaccines and clicks on it."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Vaccines(driver)


@pytest.mark.order(8)
@then('PECT_TC003_B User then clicks COVID-19 information')
def test_pect_tc003_b_008_user_then_clicks_covid19_information():
    """User then clicks COVID-19 information."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Vaccines(driver)
    driver = mystep.PECT_CoronaVirus_COVID_2019_info(driver)


scenario_name = 'PECT_TC003_C_Verifies_COVID_19_displayed_data'


@pytest.mark.order(9)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc003_c_009_verifies_covid_19_displayed_data():
    """PECT_TC003_C_Verifies_COVID_19_displayed_data."""
    print("PECT-TEST003-SCENARIO-C")
    return


@pytest.mark.order(9)
@when('PECT_TC003_C User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc003_c_009_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(10)
@then('PECT_TC003_C User clicks on the Find a Trial link')
def test_pect_tc003_c_010_user_clicks_on_the_find_a_trial_link():
    """User clicks on the Find a Trial link."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Find_a_Trial_Navbar(driver)


@pytest.mark.order(11)
@then('PECT_TC003_C User then accesses the Search Filter')
def test_pect_tc003_c_011_user_then_accesses_the_search_filter():
    """User then accesses the Search Filter."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Access_Trial_Search_Filter(driver)


@pytest.mark.order(12)
@then('PECT_TC003_C User then searches for COVID-19 and collects certain displayed data like count')
def test_pect_tc003_c_012_user_searches_COVID_19_and_collects_count():
    """User then searches for COVID-19 and collects certain displayed data like count."""
    global driver
    global myCovid19_Search_Count01
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Pfizer_Home_Image(driver)
    mytext = "COVID 19"
    driver = mystep.PECT_Search_Text_in_Find_a_Trial_Search_Filter(driver, mytext, index_location=None)
    driver = mystep.PECT_Click_on_Find_a_Trial_Button(driver, index_location=1)
    try:
        time.sleep(10)
        driver, myCovid19_Search_Count01 = mystep.PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(driver, index_location=1)
    except Exception as e:
        pass
    myCovid19_Search_Count01 = int(myCovid19_Search_Count01)
    print("myCovid19_Search_Count01 = ", myCovid19_Search_Count01)


@pytest.mark.order(13)
@then('PECT_TC003_C User then searches for covid-19 and collects certain displayed data like count')
def test_pect_tc003_c_013_user_searches_covid19_and_collects_count():
    """User then searches for covid-19 and collects certain displayed data like count."""
    global driver
    global mycovid19_Search_Count02
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Pfizer_Home_Image(driver)
    mytext = "covid-19"
    driver = mystep.PECT_Search_Text_in_Find_a_Trial_Search_Filter(driver, mytext, index_location=None)
    driver = mystep.PECT_Click_on_Find_a_Trial_Button(driver, index_location=1)
    try:
        time.sleep(10)
        driver, mycovid19_Search_Count02 = mystep.PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(driver, index_location=1)
    except Exception as e:
        pass
    mycovid19_Search_Count02 = int(mycovid19_Search_Count02)
    print("mycovid19_Search_Count02 = ", mycovid19_Search_Count02)


@pytest.mark.order(14)
@then('PECT_TC003_C User then compares the data collected in the above step004 and step005')
def test_pect_tc003_c_014_user_compares_data_from_step004_and_step005():
    """User then compares the data collected in the above step004 and step005."""
    global myCovid19_Search_Count01
    global mycovid19_Search_Count02
    if(int(myCovid19_Search_Count01) != 0) and (int(mycovid19_Search_Count02) != 0):
        if (int(myCovid19_Search_Count01) == int(mycovid19_Search_Count02)):
            assert True
        else:
            assert False


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(15)
def test_completion():
    global driver
    try:
        driver.close()
    except Exception as e:
        pass

    try:
        driver.quit()
    except Exception as e:
        pass
    driver = None

