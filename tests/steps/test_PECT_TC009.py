# coding=utf-8
"""User accesses About Pfizer Eclinical Trial Portal and accesses FAQs feature tests."""
import time

import allure
import pytest
from pytest_bdd import (
    given,
    scenario,
    then, when,
)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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


feature_name = "../features/PECT_TC009.feature"

scenario_name = "PECT_TC009_A_Accesses_FAQs_in_the_Landing_Page"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc009_a_001_accesses_faqs_in_the_landing_page():
    "PECT_TC009_A_User_Accesses_FAQs_in_the_Landing_Page."
    print("PECT-TEST009-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC009_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc009_a_001_user_access_pfizer_eclinical_trial_portal():
    """User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC009_A User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc009_a_002_user_verifies_home_icon_in_landing_page():
    """User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(3)
@then('PECT_TC009_A User then hovers over About clinical trials')
def test_pect_tc009_a_003_then_hovers_over_about_clinical_trials():
    """then hovers over About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(4)
@then('PECT_TC009_A User then accesses the FAQ')
def test_pect_tc009_a_004_then_accesses_the_faq():
    """then accesses the FAQ."""
    global driver
    pfizer_clinical_trial_faqs = pom.pect_pom.PECT_WebElement_Locators().pfizer_clinical_trial_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_clinical_trial_faqs, index_location=0)


scenario_name = "PECT_TC009_B_Accesses_FAQs_in_the_Landing_Page"


@pytest.mark.order(5)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc009_b_005_accesses_faqs_in_the_landing_page():
    """PECT_TC009_B_Accesses_FAQs_in_the_Landing_Page."""
    print("PECT-TEST009-SCENARIO-B")
    return


@pytest.mark.order(5)
@when('PECT_TC009_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc009_b_005_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC009_B User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(6)
@then('PECT_TC009_B User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc009_b_006_user_verifies_home_icon_in_the_landing_page():
    """PECT_TC009_B User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(7)
@then('PECT_TC009_B User then clicks on About clinical trials')
def test_pect_tc009_b_007_user_then_clicks_on_about_clinical_trials():
    """PECT_TC009_B User then clicks on About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(8)
@then('PECT_TC009_B User then accesses the FAQ')
def test_pect_tc009_b_008_user_then_accesses_the_faq():
    """PECT_TC009_B User then accesses the FAQ."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_frequently_asked_questions
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = utilities.action_utils.Driver_Actions().driver_page_down_action(driver, my_iterator=6)
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


scenario_name = "PECT_TC009_C_Searches_FAQ_in_the_Landing_Page"


@pytest.mark.order(9)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc009_c_009_searches_faq_in_the_landing_page():
    """PECT_TC009_C_Searches_FAQ_in_the_Landing_Page."""
    print("PECT-TEST009-SCENARIO-C")
    return


@pytest.mark.order(9)
@when('PECT_TC009_C User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc009_c_009_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC009_C User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(10)
@then('PECT_TC009_C User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc009_c_010_user_verifies_home_icon_in_the_landing_page():
    """PECT_TC009_C User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(11)
@then('PECT_TC009_C User then accesses About clinical trials')
def test_pect_tc009_c_011_user_accesses_about_clinical_trials():
    """PECT_TC009_C User then accesses About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(12)
@then('PECT_TC009_C User then accesses the FAQ')
def test_pect_tc009_c_012_user_then_accesses_the_faq():
    """PECT_TC009_C User then accesses the FAQ."""
    global driver
    pfizer_clinical_trial_faqs = pom.pect_pom.PECT_WebElement_Locators().pfizer_clinical_trial_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_clinical_trial_faqs, index_location=0)


@pytest.mark.order(13)
@then('PECT_TC009_C User then searches the FAQ')
def test_pect_tc009_c_013_user_then_searches_the_faq():
    """PECT_TC009_C User then searches the FAQ."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_search_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=None)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_search_faq_form_field
    mystep = utilities.browser_utils.MyBrowser()
    from selenium.webdriver.common.keys import Keys
    mytext = "vaccine" + Keys.ENTER
    driver = mystep.hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=None, mytext=mytext)


scenario_name = "PECT_TC009_D_Accesses_FAQ_and_Expands_the_FAQ_sections"


@pytest.mark.order(14)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc009_d_014_accesses_faq_and_expands_the_faq_sections():
    """PECT_TC009_D_Accesses_FAQ_and_Expands_the_FAQ_sections."""
    print("PECT-TEST009-SCENARIO-D")
    return


@pytest.mark.order(14)
@when('PECT_TC009_D User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc009_d_014_user_access_the_pfizer_eclinical_trial_portal():
    """PECT_TC009_D User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(15)
@then('PECT_TC009_D User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc009_d_015_user_verifies_home_icon_in_the_landing_page():
    """PECT_TC009_D User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(16)
@then('PECT_TC009_D User then access About clinical trials')
def test_pect_tc009_d_016_user_access_about_clinical_trials():
    """PECT_TC009_D User then access About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(17)
@then('PECT_TC009_D User then accesses the FAQ')
def test_pect_tc009_d_017_user_then_accesses_the_faq():
    """PECT_TC009_D User then accesses the FAQ."""
    global driver
    pfizer_clinical_trial_faqs = pom.pect_pom.PECT_WebElement_Locators().pfizer_clinical_trial_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_clinical_trial_faqs, index_location=0)


@pytest.mark.order(18)
@then('PECT_TC009_D User then clicks Expand all')
def test_pect_tc009_d_018_user_then_clicks_expand_all():
    """PECT_TC009_D User then clicks Expand all."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_faqs_expand_all
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


scenario_name = "PECT_TC009_E_Accesses_FAQ_then_Expands_and_Collapses_the_sections"


@pytest.mark.order(19)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc009_e_019_accesses_faq_then_expands_and_collapses_the_sections():
    """PECT_TC009_E_Accesses_FAQ_then_Expands_and_Collapses_the_sections."""
    print("PECT-TEST009-SCENARIO-E")
    return


@pytest.mark.order(19)
@when('PECT_TC009_E User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc009_e_019_user_access_pfizer_eclinical_trial_portal():
    """PECT_TC009_E User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(20)
@then('PECT_TC009_E User Verifies that the Home Icon is present in the Landing Page')
def test_pect_tc009_e_020_user_verifies_home_icon_in_landing_page():
    """PECT_TC009_E User Verifies that the Home Icon is present in the Landing Page."""
    global driver
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Home_Page_Logo(driver)


@pytest.mark.order(21)
@then('PECT_TC009_E User then access About clinical trials')
def test_pect_tc009_e_021_user_access_about_clinical_trials():
    """PECT_TC009_E User then access About clinical trials."""
    global driver
    about_clinical_trials = pom.pect_pom.PECT_WebElement_Locators().about_clinical_trials
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=about_clinical_trials, index_location=0)


@pytest.mark.order(22)
@then('PECT_TC009_E User then accesses the FAQ')
def test_pect_tc009_e_022_user_then_accesses_the_faq():
    """PECT_TC009_E User then accesses the FAQ."""
    global driver
    pfizer_clinical_trial_faqs = pom.pect_pom.PECT_WebElement_Locators().pfizer_clinical_trial_faqs
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=pfizer_clinical_trial_faqs, index_location=0)


@pytest.mark.order(23)
@then('PECT_TC009_E User then clicks Expand all')
def test_pect_tc009_e_023_user_then_clicks_expand_all():
    """PECT_TC009_E User then clicks Expand all."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_faqs_expand_all
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(24)
@then('PECT_TC009_E User then clicks Collapse all')
def test_pect_tc009_e_024_user_then_clicks_collapse_all():
    """PECT_TC009_E User then clicks Collapse all."""
    global driver
    time.sleep(3)
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_faqs_collapse_all
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=0)


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(25)
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

