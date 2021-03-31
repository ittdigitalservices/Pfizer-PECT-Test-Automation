

# coding=utf-8
"""User navigates to Home Page and accesses 'Learn more about your rights as a participant' link feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
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


feature_name = '../features/PECT_TC004.feature'

scenario_name = 'PECT_TC004_A_Accesses_Participant_Rights_Link'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc004_a_001_accesses_participant_rights_link():
    """PECT_TC004_A_Accesses_Participant_Rights_Link."""
    print("PECT-TEST004-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC004_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc004_a_001_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC004_A User navigates to bottom of the Home Page')
def test_pect_tc004_a_002_user_navigates_to_bottom_of_the_home_page():
    """User navigates to bottom of the Home Page."""
    global driver
    rights_as_a_participant = pom.pect_pom.PECT_WebElement_Locators().rights_as_a_participant
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Navigate_to_Page_End(driver, myxpath=rights_as_a_participant, index_location=0)
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=rights_as_a_participant, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC004_A User then accesses \'Learn more about your rights as a participant\' link')
def test_pect_tc004_a_003_user_then_accesses_participant_rights_link():
    """User then accesses 'Learn more about your rights as a participant' link."""
    global driver
    rights_as_a_participant = pom.pect_pom.PECT_WebElement_Locators().rights_as_a_participant
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=rights_as_a_participant, index_location=0)
    clinical_trial_participants_text = pom.pect_pom.PECT_WebElement_Locators().clinical_trial_participants_text
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=clinical_trial_participants_text, index_location=0)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(4)
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

