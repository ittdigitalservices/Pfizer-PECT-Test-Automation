# coding=utf-8
"""User navigates For Current Clinical Trial Participants and checks URL route feature tests."""
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
global my_main_url
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)


def setup():
    global driver
    #driver.maximize_window()
    yield driver


feature_name = "../features/PECT_TC015.feature"

scenario_name = "PECT_TC015_A_User_accesses_Current_Clinical_Trial_Participants_and_checks_URL_route"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc015_a_001_current_clinical_trial_participants_and_checks_url():
    """PECT_TC015_A_User_accesses_Current_Clinical_Trial_Participants_and_checks_URL_route."""
    print("PECT-TEST015-SCENARIO-B")
    return


@pytest.mark.order(1)
@when('PECT_TC015_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc015_a_001_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC015_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    global my_main_url
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)
    my_main_url = driver.current_url


@pytest.mark.order(2)
@then('PECT_TC015_A User navigates to For Participants')
def test_pect_tc015_a_002_user_navigates_to_for_participants():
    """PECT_TC015_A User navigates to For Participants."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC015_A User then clicks on the For Current Clinical Trial participants link')
def test_pect_tc015_a_003_clicks_current_clinical_trial_participants():
    """PECT_TC015_A User then clicks on the For Current Clinical Trial participants link."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_participants
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_for_current_clinical_trial_participants_link
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)
    time.sleep(1)


@pytest.mark.order(4)
@then('PECT_TC015_A User then checks URL route')
def test_pect_tc015_a_004_user_then_checks_url_route():
    """PECT_TC015_A User then checks URL route."""
    global my_main_url
    my_current_url = driver.current_url
    print("\nMain URL = " + str(my_main_url))
    print("\nMy Current URL = " + str(my_current_url))

    i = len(str(my_main_url))
    j = len(str(my_current_url))
    print(i)
    print(j)
    if(str(my_current_url) != str(my_main_url)):
        print("URL has been Routed")
    else:
        print("URL has not been Routed")


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

