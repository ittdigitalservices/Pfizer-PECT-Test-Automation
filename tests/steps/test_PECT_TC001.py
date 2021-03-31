# coding=utf-8
"""User accesses the Pfizer Eclinical Trial Portal and verifies certain Home Page content feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then, when,
)
from pytest_bdd.hooks import pytest_bdd_after_scenario

import utilities
from utilities.pect_utils import PECT_Common_Utils

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)


def setup():
    global driver
    driver.maximize_window()
    yield driver


feature_name = '../features/PECT_TC001.feature'

scenario_name = 'PECT_TC001_A_Verification_of_Landing_Page'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc001_a_001_verification_of_landing_page():
    """PECT_TC001_B_Verification_of_Landing_Page."""
    print("PECT-TEST001-SCENARIO-B")
    return


@pytest.mark.order(1)
@when('PECT_TC001_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc001_a_001_user_access_the_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC001_A User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc001_a_002_user_verifies_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(3)
@then('PECT_TC001_A User Accesses some of the Text Content and Verifies the Landing Page')
def test_pect_tc001_a_003_user_accesses_home_content_and_verifies_it():
    """User Accesses some of the Text Content and Verifies the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Pfizer_Home_Image(driver)



scenario_name = 'PECT_TC001_B_Verification_of_certain_Home_Page_contents'


@pytest.mark.order(4)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc001_b_004_verification_of_certain_home_page_contents():
    """PECT_001_B_verification_of_certain_Home_Page_contents."""
    print("PECT-TEST001-SCENARIO-B")
    return


@pytest.mark.order(4)
@when('PECT_TC001_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc001_b_004_user_access_the_pfizer_eclinical_trial_app():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)


@pytest.mark.order(5)
@then('PECT_TC001_B User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc001_b_005_user_verifies_that_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(6)
@then('PECT_TC001_B User Accesses some of the Displayed Information Content and Verifies them')
def test_pect_tc001_b_006_user_accesses_information_content_and_verifies():
    """User Accesses some of the Displayed Information Content and Verifies them."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials_Link(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_About_Clinical_Trials_Text(driver)


def teardown():
    #global driver
    from utilities.screenshot_utils import take_test_screen_shot
    #utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(7)
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


