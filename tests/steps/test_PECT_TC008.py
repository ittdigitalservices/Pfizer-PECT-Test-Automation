# coding=utf-8
"""User accesses the Pfizer Eclinical Trial Portal and Scrolls Down to Contact Us feature tests."""
import time
import pytest
import pytest_bdd


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
    driver.maximize_window()
    yield driver


feature_name = '../features/PECT_TC008.feature'

scenario_name = 'PECT_TC008_A_Confirm_Presence_of_Contact_Us_in_a_Page'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc008_a_001_confirm_presence_of_contact_us_in_a_page():
    """PECT_TC008_A_Confirm_Presence_of_Contact_Us_in_a_Page."""
    print("PECT-TEST008-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC008_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc008_a_001_user_access_the_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC008_A User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc008_a_002_user_verifies_that_the_home_icon_is_present():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Pfizer_Home_Image(driver)


@pytest.mark.order(3)
@then('PECT_TC008_A User then scrolls down the Landing Page')
def test_pect_tc008_a_003_user_then_scrolls_down_the_landing_page():
    """User then scrolls down the Landing Page."""
    global driver
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=4)


@pytest.mark.order(4)
@then('PECT_TC008_A User then verifies the option like \'Contact us\' and so on')
def test_pect_tc008_a_004_user_then_verifies_the_contact_us_option():
    """User then verifies the option like 'Contact us' and so on."""
    global driver
    pfizer_contact_us = pom.pect_pom.PECT_WebElement_Locators().pfizer_contact_us
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_contact_us, index_location=0)
    time.sleep(30)
    driver = utilities.driver_utils.Common_Actions().switch_to_my_window_handle(driver, handle_index=1)
    #driver = driver.switch_to_window(driver.window_handles[-1])


def teardown():
    #global driver
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

