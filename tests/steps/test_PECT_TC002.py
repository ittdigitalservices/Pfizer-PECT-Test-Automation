# coding=utf-8
"""User accesses the Pfizer Eclinical Trial Portal and accesses the TRIAL section feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then, when,
)

import utilities
from utilities.pect_utils import PECT_Common_Utils

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)


def setup():
    global driver
    driver.maximize_window()
    yield driver


feature_name = "../features/PECT_TC002.feature"

scenario_name = "PECT_TC002_A_verification_of_certain_TRIAL_page_contents"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc002_a_001_verification_of_certain_trial_page_contents():
    """PECT_002_A_verification_of_certain_TRIAL_page_contents."""
    print("PECT-TEST002-SCENARIO-A")
    return


@pytest.mark.order(1)
@when("PECT_TC002_A User Access the Pfizer Eclinical Trial Application Portal")
def test_pect_tc002_a_001_user_access_the_trial_application_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then("PECT_TC002_A User Verifies that the Home Icon is present in the Landing Page")
def test_pect_tc002_a_002_user_verifies_that_home_icon_is_present():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(3)
@then('PECT_TC002_A User then clicks on About clinical trials')
def test_pect_tc002_a_003_user_then_clicks_on_about_clinical_trials():
    """User then clicks on About clinical trials"""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials(driver)


@pytest.mark.order(4)
@then('PECT_TC002_A User then accesses some of the TRIAL page contents and Verifies them')
def test_pect_tc002_a_004_user_accesses_trial_contents_and_verifies_them():
    """User then accesses some of the TRIAL page contents and Verifies them."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Home_Page_Logo(driver)
    driver = mystep.PECT_Hover_About_Clinical_Trials(driver)
    driver = mystep.PECT_How_Clinical_Trial_Works(driver)


scenario_name = "PECT_TC002_B_Access_the_Trial_Filters"


@pytest.mark.order(5)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc002_b_005_accesses_trial_filters():
    """PECT_TC001_B_Accesses_Trial_Filters."""
    print("PECT-TEST002-SCENARIO-B")
    return


@pytest.mark.order(5)
@when('PECT_TC002_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc002_b_005_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(6)
@then('PECT_TC002_B User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc002_b_006_user_verifies_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(7)
@then('PECT_TC002_B User then clicks on Find a trial')
def test_pect_tc002_b_007_user_then_clicks_on_find_a_trial():
    """User then clicks on Find a trial."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Find_a_Trial_Navbar(driver)


@pytest.mark.order(8)
@then('PECT_TC002_B User then accesses the TRIAL Filters')
def test_pect_tc002_b_008_user_then_accesses_the_trial_filters():
    """User then accesses the TRIAL Filters."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Hover_Over_Show_Filters(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Access_Trial_Search_Filter(driver)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(9)
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

