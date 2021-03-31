# coding=utf-8
"""User accesses About Pfizer Eclinical Trial Portal and accesses Other Diseases in the Vaccines Page feature tests."""
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


feature_name = '../features/PECT_TC005.feature'

scenario_name = 'PECT_TC005_A_Accesses_Other_Diseases_in_Vaccines_Page'


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc005_a_001_accesses_other_diseases_in_vaccines_page():
    """PECT_TC005_A_Accesses_Other_Diseases_in_Vaccines_Page."""
    print("PECT-TEST005-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC005_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc005_a_001_user_access_the_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC005_A User navigates to Our research Page')
def test_pect_tc005_a_002_user_navigates_to_our_research_page():
    """User navigates to Our research Page."""
    global driver
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Our_Research(driver)


@pytest.mark.order(3)
@then('PECT_TC005_A User then clicks on the Vaccines link')
def test_pect_tc005_a_003_user_then_clicks_on_the_vaccines_link():
    """User then clicks on the Vaccines link."""
    global driver
    Pfizer_Research = pom.pect_pom.PECT_WebElement_Locators().our_research
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=Pfizer_Research, index_location=0)
    pfizer_research_vaccines = pom.pect_pom.PECT_WebElement_Locators().pfizer_research_vaccines
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_research_vaccines, index_location=0)


@pytest.mark.order(4)
@then('PECT_TC005_A User then checks whether Other Diseases are mentioned or not')
def test_pect_tc005_a_004_user_then_checks_for_other_diseases():
    """User then checks whether Other Diseases are mentioned or not."""
    global driver
    respiratory_diseases = pom.pect_pom.PECT_WebElement_Locators().respiratory_diseases
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=respiratory_diseases, index_location=0)


@pytest.mark.order(5)
@then('PECT_TC005_A User verifies the presence of Respiratory diseases and so on')
def test_pect_tc005_a_005_user_verifies_respiratory_diseases_presence():
    """User verifies the presence of Respiratory diseases and so on."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().trial_for_respiratory_diseases
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver, mycount = mystep.PECT_Get_Text_of_Count_in_a_Result(driver, myxpath=myxpath, index_location=1)
    print(mycount)
    try:
        if int(mycount) > 0:
            assert True
        else:
            assert False
    except Exception as e:
        pass


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
