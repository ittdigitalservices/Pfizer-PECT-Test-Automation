# coding=utf-8
"""User navigates to Internal Medicine Page and accesses Email and Print Option feature tests."""
import time

import pytest

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


import pom
import utilities


global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
global myCovid19_Search_Count01
global mycovid19_Search_Count02


def setup():
    global driver
    #driver.maximize_window()
    yield driver


feature_name = "../features/PECT_TC012.feature"

scenario_name = "PECT_TC012_A_User_accesses_Internal_Medicine_and_checks_Email_option"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc012_a_001_checks_internal_medicine_and_email_option():
    """PECT_TC012_A_User_accesses_Internal_Medicine_and_checks_Email_option."""
    print("PECT-TEST012-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC012_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc012_a_001_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC012_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC012_A User navigates to Our research Page')
def test_pect_tc012_a_002_user_navigates_to_our_research_page():
    """PECT_TC012_A User navigates to Our research Page."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().our_research
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC012_A User then clicks on the Internal Medicine link')
def test_pect_tc012_a_003_user_clicks_internal_medicine_link():
    """PECT_TC012_A User then clicks on the Internal Medicine link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_link
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(4)
@then('PECT_TC012_A User then checks the Clinical Trials in landing page')
def test_pect_tc012_a_004_user_checks_clinical_trials_landing_page():
    """PECT_TC012_A User then checks the Clinical Trials in landing page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=2)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_clinical_trials
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=1)


@pytest.mark.order(5)
@then('PECT_TC012_A User then checks on the Email Option in the page')
def test_pect_tc012_a_005_user_checks_email_option_in_the_landing_page():
    """PECT_TC012_A User then checks on the Email Option in the page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_email
    #driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


scenario_name = "PECT_TC012_B_User_accesses_Internal_Medicine_and_checks_Print_option"


@pytest.mark.order(6)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc012_b_006_user_checks_internal_medicine_and_print_option():
    """PECT_TC012_B_User_accesses_Internal_Medicine_and_checks_Print_option."""
    print("PECT-TEST012-SCENARIO-B")
    return


@pytest.mark.order(6)
@when('PECT_TC012_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc012_b_006_access_pfizer_eclinical_trial_portal():
    """PECT_TC012_B User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(7)
@then('PECT_TC012_B User navigates to Our research Page')
def test_pect_tc012_b_007_user_navigates_to_our_research_page():
    """PECT_TC012_B User navigates to Our research Page."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().our_research
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(8)
@then('PECT_TC012_B User then clicks on the Internal Medicine link')
def test_pect_tc012_b_008_user_clicks_internal_medicine_link():
    """PECT_TC012_B User then clicks on the Internal Medicine link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_link
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(9)
@then('PECT_TC012_B User then checks the Clinical Trials in landing page')
def test_pect_tc012_b_009_user_checks_clinical_trials_in_landing_page():
    """PECT_TC012_B User then checks the Clinical Trials in landing page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=2)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_clinical_trials
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=1)


@pytest.mark.order(10)
@then('PECT_TC012_B User then checks on the Print Option in the page')
def test_pect_tc012_b_010_user_checks_print_option_in_landing_page():
    """PECT_TC012_B User then checks on the Print Option in the page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_print
    #driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=3)
    driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(11)
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
