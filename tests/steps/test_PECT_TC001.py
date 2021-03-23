# coding=utf-8
"""User accesses the Pfizer Eclinical Trial Portal and verifies certain Home Page content feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
)
from pytest_bdd.hooks import pytest_bdd_after_scenario

import utilities
from utilities.pect_utils import PECT_Common_Utils

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()


def setup():
    global driver
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


feature_name = '../features/PECT_TC001.feature'

scenario_name = 'PECT_TC001_A_Verification_of_Landing_Page'


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def test_pect_tc001_a_verification_of_landing_page():
    """PECT_TC001_B_Verification_of_Landing_Page."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(1)
@given('User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc001_a_user_access_the_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(2)
@then('User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc001_a_user_verifies_home_icon_is_present_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)

#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(3)
@then('User Accesses some of the Text Content and Verifies the Landing Page')
def test_pect_tc001_a_user_accesses_home_content_and_verifies_landing_page():
    """User Accesses some of the Text Content and Verifies the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Pfizer_Home_Image(driver)



scenario_name = 'PECT_TC001_B_Verification_of_certain_Home_Page_contents'


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(4)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def test_pect_tc001_b_verification_of_certain_home_page_contents():
    """PECT_001_B_verification_of_certain_Home_Page_contents."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(4)
@given('User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc001_b_user_access_the_pfizer_eclinical_trial_app():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    #driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)
    #driver.maximize_window()


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(5)
@then('User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc001_b_user_verifies_that_home_icon_in_the_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)
    #driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials(driver)


#@pytest.mark.flaky(reruns=0)
#@pytest.mark.repeat(0)
@pytest.mark.order(6)
@then('User Accesses some of the Displayed Information Content and Verifies them')
def test_pect_tc001_b_user_accesses_information_content_and_verifies_them():
    """User Accesses some of the Displayed Information Content and Verifies them."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials_Link(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials_Text(driver)


def teardown():
    global driver
    from utilities.screenshot_utils import test_failed_check
    #utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    test_failed_check(driver, scenario_name=scenario_name)
    # driver.quit()


