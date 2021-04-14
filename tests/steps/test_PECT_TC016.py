# coding=utf-8
"""User navigates For Pfizer Clinical Trial and searches for a Trial feature tests."""
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


feature_name = "../features/PECT_TC016.feature"

scenario_name = "PECT_TC016_A_User_navigates_to_Find_a_Pfizer_Clinical_Trial_and_searches_a_Trial"


@pytest.mark.order(1)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc016_a_001_navigates_pfizer_clinical_trial_and_searches_trial():
    """PECT_TC016_A_User_navigates_to_Find_a_Pfizer_Clinical_Trial_and_searches_a_Trial."""
    print("PECT-TEST016-SCENARIO-A")
    return


@pytest.mark.order(1)
@when('PECT_TC016_A User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc016_a_001_user_access_the_pfizer_eclinical_trial_portal():
    """PECT_TC016_A User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(2)
@then('PECT_TC016_A User navigates to Find a Pfizer Clinical Trial segment of the home page')
def test_pect_tc016_a_002_navigates_to_find_pfizer_clinical_trial_segment():
    """PECT_TC016_A User navigates to Find a Pfizer Clinical Trial segment of the home page."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Find_a_Pfizer_clinical_trial
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)


@pytest.mark.order(3)
@then('PECT_TC016_A User then enters or populates the search value')
def test_pect_tc016_a_003_user_then_populates_the_search_value():
    """PECT_TC016_A User then enters or populates the search value."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Find_a_Pfizer_clinical_trial_Search_Text_Input
    #mystep = utilities.pect_utils.PECT_Common_Utils()
    #driver = mystep.PECT_Search_Text_in_Find_a_Trial_Search_Filter(driver, mytext="covid 19", index_location=0)
    driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="covid 19")


@pytest.mark.order(4)
@then('PECT_TC016_A User then enters or populates the location value')
def test_pect_tc016_a_004_then_enters_or_populates_the_location_value():
    """PECT_TC016_A User then enters or populates the location value."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Find_a_Pfizer_clinical_trial_Location_Text_Input
    driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=2)
    driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="New York")


@pytest.mark.order(5)
@then('PECT_TC016_A User then clicks on Find a Trial button')
def test_pect_tc016_a_005_user_then_clicks_on_find_a_trial_button():
    """PECT_TC016_A User then clicks on Find a Trial button."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Find_a_Trial_Button
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement_and_Click_it(driver, myxpath=myxpath, index_location=1)
    time.sleep(1)


scenario_name = "PECT_TC016_B_User_accesses_Pfizer_Clinical_Trial_and_searches_a_Trial"


@pytest.mark.order(6)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc016_b_006_accesses_pfizer_clinical_trial_and_searches_a_trial():
    """PECT_TC016_B_User_accesses_Pfizer_Clinical_Trial_and_searches_a_Trial."""
    print("PECT-TEST016-SCENARIO-B")
    return


@pytest.mark.order(6)
@when('PECT_TC016_B User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc016_b_006_user_access_the_pfizer_eclinical_trial_portal():
    """PECT_TC016_B User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(7)
@then('PECT_TC016_B User navigates to Find a Trial option at the Top and clicks it')
def test_pect_tc016_b_007_navigates_to_find_trial_option_and_clicks_it():
    """PECT_TC016_B User navigates to Find a Trial option at the Top and clicks it."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_navbar
    mystep = utilities.action_utils.Driver_Actions()
    driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=1)
    #driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="New York")


@pytest.mark.order(8)
@then('PECT_TC016_B User then accesses Search for a Pfizer clinical trial section')
def test_pect_tc016_b_008_accesses_search_a_pfizer_clinical_trial_section():
    """PECT_TC016_B User then accesses Search for a Pfizer clinical trial section."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Search_for_a_Pfizer_Clinical_Trial
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    ###mystep = utilities.action_utils.Driver_Actions()
    ###driver = mystep.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=0)
    #driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=1)
    #driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="New York")
    time.sleep(3)

@pytest.mark.order(9)
@then('PECT_TC016_B User then enters or populates the search value')
def test_pect_tc016_b_009_then_enters_or_populates_the_search_value():
    """PECT_TC016_B User then enters or populates the search value."""
    global driver
    ###myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_search_filter2
    ##mystep = utilities.pect_utils.PECT_Common_Utils()
    ##driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    myxpath2 = pom.pect_pom.PECT_WebElement_Locators().Search_for_a_Pfizer_Clinical_Trial
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.send_double_click_actions(driver, myxpath=myxpath2, index_location=0)
    driver = mystep1.send_Tab_Keys_using_driver_actions(driver, counter=2)
    driver = mystep1.send_Data_using_driver_actions(driver, mydata="covid 19")
    time.sleep(3)
    ##mystep = utilities.action_utils.Driver_Actions()
    #driver = mystep.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=0)
    ##driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=3)
    #driver = mystep.PECT_Send_Keys_to_WebElement_using_xpath(driver, myxpath=myxpath, index_location=0,myText="covid 19")

    ##mystep = utilities.browser_utils.MyBrowser()
    ##driver = mystep.hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="covid 19")
    #driver = mystep.hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=1, mytext="covid 19")

    #myxpath = pom.pect_pom.PECT_WebElement_Locators().Find_a_Pfizer_clinical_trial_Location_Text_Input
    #driver = utilities.action_utils.Driver_Actions().move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=2)
    #driver = utilities.browser_utils.MyBrowser().hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="New York")



@pytest.mark.order(10)
@then('PECT_TC016_B User then enters or populates the location value')
def test_pect_tc016_b_010_then_enters_or_populates_the_location_value():
    """PECT_TC016_B User then enters or populates the location value."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_location_filter2
    ##mystep = utilities.pect_utils.PECT_Common_Utils()
    ##driver = mystep.PECT_Send_Keys_to_WebElement_using_xpath(driver, myxpath=myxpath,index_location=0, myText="New York")
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.send_Tab_Keys_using_driver_actions(driver, counter=1)
    driver = mystep1.send_Data_using_driver_actions(driver, mydata="New York")
    time.sleep(3)
    ##mystep = utilities.action_utils.Driver_Actions()
    #driver = mystep.move_cursor_to_webelement_by_xpath(driver, myxpath=myxpath, index_location=0)
    ##driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=2)
    ##mystep = utilities.browser_utils.MyBrowser()
    ##driver = mystep.hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=0, mytext="New York")
    #driver = mystep.hover_and_send_keys_to_web_element(driver, myxpath=myxpath, index_location=1, mytext="New York")


@pytest.mark.order(11)
@then('PECT_TC016_B User then clicks on the Find a trial button')
def test_pect_tc016_b_011_user_then_clicks_on_the_find_a_trial_button():
    """PECT_TC016_B User then clicks on the Find a trial button."""
    global driver
    ##myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_submit_button2
    ##mystep = utilities.action_utils.Driver_Actions()
    ##driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=1)
    #driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=1, counter=1)
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.perform_Enter_using_driver_actions(driver)
    time.sleep(3)
    #driver = mystep1.send_Data_using_driver_actions(driver, mydata="New York")



scenario_name = "PECT_TC016_C_User_accesses_Pfizer_Clinical_Trial_and_Trial_Search_Result_content"


@pytest.mark.order(12)
@scenario(feature_name=feature_name, scenario_name=scenario_name)
def pect_tc016_c_012_accesses_pfizer_clinical_trial_search_result_content():
    """PECT_TC016_C_User_accesses_Pfizer_Clinical_Trial_and_Trial_Search_Result_content."""
    print("PECT-TEST016-SCENARIO-C")
    return


@pytest.mark.order(12)
@when('PECT_TC016_C User Access the Pfizer Eclinical Trial Application Portal')
def test_pect_tc016_c_012_user_accesses_pfizer_eclinical_trial_application():
    """PECT_TC016_C User Access the Pfizer Eclinical Trial Application Portal."""
    global driver
    import utilities
    driver = utilities.browser_utils.MyBrowser().set_browser_view_dimensions(driver)
    driver = utilities.browser_utils.MyBrowser().navigate_to_url(driver)
    driver = utilities.pect_utils.PECT_Common_Utils().PECT_Accept_Cookies(driver)


@pytest.mark.order(13)
@then('PECT_TC016_C User navigates to Find a Trial option at the Top and clicks it')
def test_pect_tc016_c_013_user_navigates_to_find_trial_option_and_clicks_it():
    """PECT_TC016_C User navigates to Find a Trial option at the Top and clicks it."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_navbar
    mystep = utilities.action_utils.Driver_Actions()
    driver = mystep.move_cursor_to_webelement_by_xpath_and_click_it(driver, myxpath=myxpath, index_location=0, counter=1)


@pytest.mark.order(14)
@then('PECT_TC016_C User then accesses Search for a Pfizer clinical trial section')
def test_pect_tc016_c_014_accesses_search_for_pfizer_clinical_trial_section():
    """PECT_TC016_C User then accesses Search for a Pfizer clinical trial section."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().Search_for_a_Pfizer_Clinical_Trial
    mystep = utilities.pect_utils.PECT_Common_Utils()
    driver = mystep.PECT_Hover_Over_a_WebElement(driver, myxpath=myxpath, index_location=0)
    time.sleep(3)


@pytest.mark.order(15)
@then('PECT_TC016_C User then enters or populates the search value')
def test_pect_tc016_c_015_user_then_enters_or_populates_the_search_value():
    """PECT_TC016_C User then enters or populates the search value."""
    global driver
    myxpath2 = pom.pect_pom.PECT_WebElement_Locators().Search_for_a_Pfizer_Clinical_Trial
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.send_double_click_actions(driver, myxpath=myxpath2, index_location=0)
    driver = mystep1.send_Tab_Keys_using_driver_actions(driver, counter=2)
    driver = mystep1.send_Data_using_driver_actions(driver, mydata="covid 19")
    time.sleep(3)


@pytest.mark.order(16)
@then('PECT_TC016_C User then enters or populates the location value')
def test_pect_tc016_c_016_user_then_enters_or_populates_the_location_value():
    """PECT_TC016_C User then enters or populates the location value."""
    global driver
    myxpath = pom.pect_pom.PECT_WebElement_Locators().pfizer_find_a_trial_location_filter2
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.send_Tab_Keys_using_driver_actions(driver, counter=1)
    driver = mystep1.send_Data_using_driver_actions(driver, mydata="New York")
    time.sleep(3)


@pytest.mark.order(17)
@then('PECT_TC016_C User then clicks on the Find a trial button')
def test_pect_tc016_c_017_user_then_clicks_on_the_find_a_trial_button():
    """PECT_TC016_C User then clicks on the Find a trial button."""
    global driver
    mystep1 = utilities.driver_utils.Common_Actions()
    driver = mystep1.perform_Enter_using_driver_actions(driver)
    time.sleep(3)


@pytest.mark.order(18)
@then('PECT_TC016_C User then access the searched page contents')
def test_pect_tc016_c_018_user_then_access_the_searched_page_contents():
    """PECT_TC016_C User then access the searched page contents."""
    global driver
    try:
        time.sleep(10)
        mystep = utilities.pect_utils.PECT_Common_Utils()
        driver, mycovid19_Search_Result = mystep.PECT_Get_Text_of_Count_in_Find_a_Trial_Search_Result(driver, index_location=1)
    except Exception as e:
        pass
    mycovid19_Search_Result = int(mycovid19_Search_Result)
    print("\nCovid Search Result = " + str(mycovid19_Search_Result) + "\n")
    if(mycovid19_Search_Result != 0):
        assert True
    else:
        assert False
    return driver


def teardown():
    global driver
    from utilities.screenshot_utils import take_test_screen_shot
    # utilities.take_browser_screenshot.take_full_screenshot(driver, scenario_name=scenario_name)
    take_test_screen_shot(driver, scenario_name=scenario_name)
    # driver.quit()


@pytest.mark.order(19)
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


