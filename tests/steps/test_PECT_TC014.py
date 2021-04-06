# coding=utf-8
"""User navigates For Current Clinical Trial Participants and Performs Go Back To Top feature tests."""
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


def setup():
    global driver
    #driver.maximize_window()
    yield driver


feature_name = "../features/PECT_TC014.feature"

scenario_name = "PECT_TC014_A_User_accesses_Clinical_Trial_Participants_and_performs_go_back_to_top"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc014_a_001_accesses_clinical_trial_participants_and_go_to_top():
    """PECT_TC014_A_User_accesses_Clinical_Trial_Participants_and_performs_go_back_to_top."""
    print("PECT-TEST014-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC014_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc014_a_001_user_access_the_pfizer_eclinical_trial_portal():
    """PECT_TC014_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC014_A User navigates to For Participants')
def test_pect_tc014_a_002_user_navigates_to_for_participants():
    """PECT_TC014_A User navigates to For Participants."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC014_A User then clicks on the For Current Clinical Trial participants link')
def test_pect_tc014_a_003_user_clicks_current_clinical_trial_participants():
    """PECT_TC014_A User then clicks on the For Current Clinical Trial participants link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_current_clinical_trial_participants_link
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)


@pytest.mark.order(4)
@then('PECT_TC014_A User then scrolls down the utmost last of the Landing Page')
def test_pect_tc014_a_004_user_scrolls_down_the_landing_page():
    """PECT_TC014_A User then scrolls down the utmost last of the Landing Page."""
    global driver
    #mystep = utilities.pect_utils.PECT_Common_Utils()
    time.sleep(1)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_back_to_top
    #driver, xElement = mystep.PECT_Set_Focus_on_the_WebElement_using_xpath(driver, myxpath=myxpath, index_location=4)
    driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(5)
@then('PECT_TC014_A User then tries use Go Back To Top option')
def test_pect_tc014_a_005_user_then_tries_go_back_to_top_option():
    """PECT_TC014_A User then tries use Go Back To Top option."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    #driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)
    #driver = utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_back_to_top
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)
    #driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


scenario_name = "PECT_TC014_B_User_accesses_FAQs_and_performs_go_back_to_top"


@pytest.mark.order(6)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc014_b_006_accesses_faqs_and_performs_go_back_to_top():
    """PECT_TC014_B_User_accesses_FAQs_and_performs_go_back_to_top."""
    print("PECT-TEST014-SCENARIO-B")
    return


@pytest.mark.order(6)
@when('PECT_TC014_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc014_b_006_user_access_the_pfizer_eclinical_trial_portal():
    """PECT_TC014_B User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(7)
@then('PECT_TC014_B User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc014_b_007_user_verifies_home_icon_in_the_landing_page():
    """PECT_TC014_B User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(8)
@then('PECT_TC014_B User then access About clinical trials')
def test_pect_tc014_b_008_user_then_access_about_clinical_trials():
    """PECT_TC014_B User then access About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(9)
@then('PECT_TC014_B User then accesses the FAQ')
def test_pect_tc014_b_009_user_then_accesses_the_faq():
    """PECT_TC014_B User then accesses the FAQ."""
    global driver
    pfizer_clinical_trial_faqs = pom.pect_pom.PECT_WebElement_Locators().pfizer_clinical_trial_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_clinical_trial_faqs, index_location=0)


@pytest.mark.order(10)
@then('PECT_TC014_B User then scrolls down the utmost last of the Landing Page')
def test_pect_tc014_b_010_user_scrolls_down_the_landing_page():
    """PECT_TC014_B User then scrolls down the utmost last of the Landing Page."""
    global driver
    #mystep = utilities.pect_utils.PECT_Common_Utils()
    time.sleep(1)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_back_to_top
    #driver, xElement = mystep.PECT_Set_Focus_on_the_WebElement_using_xpath(driver, myxpath=myxpath, index_location=4)
    driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(11)
@then('PECT_TC014_B User then tries use Go Back To Top option')
def test_pect_tc014_b_011_user_then_tries_use_go_back_to_top_option():
    """PECT_TC014_B User then tries use Go Back To Top option."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    #driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)
    #driver = utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_back_to_top
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(12)
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

