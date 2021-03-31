# coding=utf-8
"""User navigates to Our research and accesses Internal Medicine feature tests."""
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



feature_name = "../features/PECT_TC010.feature"

scenario_name = "PECT_TC010_A_User_accesses_Internal_Medicine_from_Research_page"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc010_a_001_user_accesses_internal_medicine_from_research_page():
    """PECT_TC010_A_User_accesses_Internal_Medicine_from_Research_page."""
    print("PECT-TEST010-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC010_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc010_a_001_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC010_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC010_A User navigates to Our research Page')
def test_pect_tc010_a_002_user_navigates_to_our_research_page():
    """PECT_TC010_A User navigates to Our research Page."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().our_research
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC010_A User then clicks on the Internal Medicine link')
def test_pect_tc010_a_003_user_clicks_internal_medicine_link():
    """PECT_TC010_A User then clicks on the Internal Medicine link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_link
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(4)
@then('PECT_TC010_A User then checks the Clinical Trials in Internal Medicine landing page')
def test_pect_tc010_a_004_checks_clinical_trials_in_internal_medicine_page():
    """PECT_TC010_A User then checks the Clinical Trials in Internal Medicine landing page."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().internal_medicine_covid
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=2)
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_internal_medicine_clinical_trials
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=1)


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
