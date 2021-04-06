# coding=utf-8
"""User navigates For Current Clinical Trial Participants and verifies Download option presence feature tests."""
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


feature_name = "../features/PECT_TC013.feature"

scenario_name = "PECT_TC013_A_User_accesses_Clinical_Trial_Participants_and_verifies_Download_option"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc013_a_001_accesses_clinical_trial_participants_and_download_option():
    """PECT_TC013_A_User_accesses_Clinical_Trial_Participants_and_verifies_Download_option."""
    print("PECT-TEST013-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC013_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc013_a_001_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC013_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC013_A User navigates to For Participants')
def test_pect_tc013_a_002_user_navigates_to_for_participants():
    """PECT_TC012_A User navigates to For Participants."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC013_A User then clicks on the For Current Clinical Trial participants link')
def test_pect_tc013_a_003_user_clicks_current_clinical_trial_participants():
    """User then clicks on the For Current Clinical Trial participants link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    #myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_past_clinical_trial_participants_link
    #driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_current_clinical_trial_participants_link
    #driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)


@pytest.mark.order(4)
@then('PECT_TC013_A User then checks the Download Option presence in the landing page')
def test_pect_tc013_a_004_user_checks_download_option_in_landing_page():
    """User then checks the Download Option presence in the landing page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    #driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)
    #driver = utilities.action_utils.Driver_Actions().driver_page_home_action(driver)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_download_checklist_pdf
    driver, xElement = mystep.PECT_Set_Focus_on_the_WebElement_using_xpath(driver, myxpath=myxpath, index_location=4)
    #driver, xElement = utilities.action_utils.Driver_Actions().scroll_and_search_into_view_of_element(driver, myxpath=myxpath, index_location=0)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(5)
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

