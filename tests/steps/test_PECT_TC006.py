# coding=utf-8
"""User accesses About Pfizer Eclinical Trial Portal and accesses Other Diseases in the Vaccines Page feature tests."""
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



feature_name = '../features/PECT_TC006.feature'

scenario_name = 'PECT_TC006_A_Verifies_Text_Content_in_the_Research_Page'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc006_a_001_verifies_text_content_in_the_research_page():
    """PECT_TC006_A_Verifies_Text_Content_in_the_Research_Page."""
    print("PECT-TEST006-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC006_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc006_a_001_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC006_A User navigates to \'Our research\' Page')
def test_pect_tc006_a_002_user_navigates_to_research_page():
    """User navigates to 'Our research' Page."""
    global driver
    Pfizer_Research = pom.pect_pom.PECT_WebElement_Locators().our_research
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Research, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC006_A User then verifies the presence of \'Visit our Research Page\' link')
def test_pect_tc006_a_003_user_verifies_research_page_link_presence():
    """User then verifies the presence of 'Visit our Research Page' link."""
    global driver
    Pfizer_Research = pom.pect_pom.PECT_WebElement_Locators().our_research
    visit_our_research_page = pom.pect_pom.PECT_WebElement_Locators().visit_our_research_page
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Research, index_location=0)
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=visit_our_research_page, index_location=0)


@pytest.mark.order(4)
@then('PECT_TC006_A User then accesses \'Visit our Research Page\' link by clicking on it')
def test_pect_tc006_a_004_user_accesses_research_page_link_by_clicking_it():
    """User then accesses 'Visit our Research Page' link by clicking on it."""
    global driver
    Pfizer_Research = pom.pect_pom.PECT_WebElement_Locators().our_research
    visit_our_research_page = pom.pect_pom.PECT_WebElement_Locators().visit_our_research_page
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Research, index_location=0)
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, index_location=0, myxpath=visit_our_research_page)


@pytest.mark.order(5)
@then('PECT_TC006_A User then verifies some Text Content in the \'Research Page\'')
def test_pect_tc006_a_005_user_verifies_some_text_in_the_research_page():
    """User then verifies some Text Content in the 'Research Page'."""
    global driver
    research_page_text_content = pom.pect_pom.PECT_WebElement_Locators().research_page_text_content
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=research_page_text_content, index_location=0)


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
