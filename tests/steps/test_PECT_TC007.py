# coding=utf-8
"""User navigates to 'Any' One of the pages and the tries to check the presence of a video feature tests."""
import time

import pytest
import pytest_bdd

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pytest_bdd.plugin import pytest_bdd_before_scenario

from selenium.webdriver.common.keys import Keys

import pom
import utilities

global driver
driver = utilities.browser_utils.MyBrowser().get_browser()
driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)


def setup():
    global driver
    driver.maximize_window()
    yield driver


feature_name = '../features/PECT_TC007.feature'

scenario_name = 'PECT_TC007_A_Confirm_Presence_of_a_Video_in_a_Page'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc007_a_001_confirm_presence_of_a_video_in_a_page():
    """PECT_TC007_A_Confirm_Presence_of_a_Video_in_a_Page."""
    print("PECT-TEST007-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC007_A User Access the Pfizer Eclinical Trial Portal')
def test_pect_tc007_a_001_user_access_pfizer_eclinical_portal():
    """User Access the Pfizer Eclinical Trial Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC007_A User navigates to \'Our research\' Page')
def test_pect_tc007_a_002_user_navigates_to_research_page():
    """User navigates to 'Our research' Page."""
    global driver
    Pfizer_Research = pom.pect_pom.PECT_WebElement_Locators().our_research
    visit_our_research_page = pom.pect_pom.PECT_WebElement_Locators().visit_our_research_page
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Research, index_location=0)
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, index_location=0, myxpath=visit_our_research_page)


@pytest.mark.order(3)
@then('PECT_TC007_A User scrolls down the Landing Page')
def test_pect_tc007_a_003_user_scrolls_down_the_landing_page():
    """User scrolls down the Landing Page."""
    global driver
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=3)


@pytest.mark.order(4)
@then('PECT_TC007_A User then searches for the presence of any Video')
def test_pect_tc007_a_004_user_then_searches_presence_of_a_video():
    """User then searches for the presence of any Video."""
    global driver
    Pfizer_Video = pom.pect_pom.PECT_WebElement_Locators().pfizer_video
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=1)
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Video, index_location=0)


@pytest.mark.order(5)
@then('PECT_TC007_A User confirms the presence of atleast one Video')
def test_pect_tc007_a_005_user_confirms_the_presence_of_a_video():
    """User confirms the presence of atleast one Video."""
    global driver
    Pfizer_Video = pom.pect_pom.PECT_WebElement_Locators().pfizer_video
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=Pfizer_Video, index_location=0)
    time.sleep(120)
    driver = utilities.action_utils.Driver_Actions().driver_page_pause_action(driver)


def teardown():
    #global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(6)
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

