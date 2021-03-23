#
# AUTHOR : Vinay Srinivasan
#

# coding=utf-8
"""Testing Clear Trip Web Booking feature tests."""

from _winapi import WaitForMultipleObjects, NULL
from itertools import count
from webbrowser import Chrome

import pytest
import selenium

from selenium import webdriver
# from selenium.webdriver import chrome
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import webdriver

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    scenarios)

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.order(3)
# class Test_001_Clear_Trip_Booking():
import utilities
from utilities.screenshot_utils import test_failed_check

CLEAR_TRIP_SITE = "https://www.cleartrip.com/"
elements = []
mycookies = ""

FireFoxWebDriverPath = "./webdrivers/win/geckodriver.exe"
global driver
#driver = selenium.webdriver.firefox.webdriver.WebDriver(executable_path=FireFoxWebDriverPath)
driver = utilities.browser_utils.MyBrowser().get_browser()



def setup():
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


scenario_name = 'Testing_Clear_Trip_WebSite_Booking'


@scenario(feature_name='../features/Clear_Trip_Booking.feature', scenario_name=scenario_name)
def test_001_testing_clear_trip_website_booking():
    """Testing Clear Trip WebSite Booking."""
    pass


@given("Testing of Clear Trip Booking for 02")
def test_001_testing_of_clear_trip_booking_for_02():
    driver.implicitly_wait(10)


@then('Launch Chrome Web Driver')
def test_001_launch_chrome_web_driver():
    """Launch Chrome Web Driver."""
    driver.implicitly_wait(5)
    driver.maximize_window()


@then('Navigate to Clear Trip Web Site')
def test_001_navigate_to_clear_trip_web_site():
    """Navigate to Clear Trip Web Site."""
    driver.implicitly_wait(10)
    driver.get(CLEAR_TRIP_SITE)
    mycookies = driver.get_cookies()


@then("Select 'Flights' tab")
def test_001_select_flights_tab():
    """Select "Flights" tab."""
    driver.implicitly_wait(10)
    xPathVal = "//span[contains(@class, 'productIcon flights')]"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[1].click()


@then('Search Round Trip flight from Mum to Delhi')
def test_001_search_round_trip_flight_from_mum_to_delhi():
    """Search Round Trip flight from Mum to Delhi."""
    driver.implicitly_wait(20)
    xPathVal = "//*[(@id='OneWay') and (@class='tripType')]"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].click()
    xPathVal = "//input[(@id='RoundTrip') and (@class='tripType')]"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].click()
    elements[0].click()
    xPathVal = "//input[@id='FromTag']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].send_keys("Mumbai, IN - Chatrapati Shivaji Airport (BOM)" + Keys.TAB)
    xPathVal = "//input[@id='ToTag']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].send_keys("New Delhi, IN - Indira Gandhi Airport (DEL)" + Keys.TAB)


@then('Depart Date is 5 days from Today')
def test_001_depart_date_is_5_days_from_today():
    """Depart Date is 5 days from Today."""
    driver.implicitly_wait(25)
    xPathVal = "//input[@id='DepartDate']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].send_keys("16042021" + Keys.TAB)


@then('Return date is 6 days from today')
def test_001_return_date_is_6_days_from_today():
    """Return date is 6 days from today."""
    driver.implicitly_wait(15)
    xPathVal = "//input[@id='ReturnDate']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].send_keys("28042021" + Keys.TAB)


@then('Select Adults travelling = 2')
def test_001_select_adults_travelling_as_2():
    """Select Adults travelling = 2."""
    driver.implicitly_wait(10)
    xPathVal = "//select[@id='Adults']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].send_keys("2")


@then('Click on \'Search\'')
def test_001_click_on_search():
    """Click on 'Search'."""
    driver.implicitly_wait(10)
    xPathVal = "//input[@id='SearchBtn']"
    elements = driver.find_elements_by_xpath(xPathVal)
    elements[0].click()


@then('Select a Non-Stop Flight')
def test_001_select_a_nonstop_flight():
    """Select a Non-Stop Flight."""
    assert True


@then('Select the 02nd Spice Jet or Indigo from depart')
def test_001_select_the_02nd_spice_jet_or_indigo_from_depart():
    """Select the 02nd Spice Jet or Indigo from depart."""
    raise NotImplementedError


@then('Select the 02nd Jet Airways or Go Air from return')
def test_001_select_the_02nd_jet_airways_or_go_air_from_return():
    """Select the 02nd Jet Airways or Go Air from return."""
    raise NotImplementedError


@then('Click Booking')
def test_001_click_booking():
    """Click Booking."""
    raise NotImplementedError


@then('Avoid or Skip any insurance')
def test_001_avoid_or_skip_any_insurance():
    """Avoid or Skip any insurance."""
    raise NotImplementedError


@then('Accept the terms and conditions')
def test_001_accept_the_terms_and_conditions():
    """Accept the terms and conditions."""
    raise NotImplementedError


@then('Click Continue Booking')
def test_001_click_continue_booking():
    """Click Continue Booking."""
    raise NotImplementedError


@then('Enter an email address as \'ivav@sample.com\'')
def test_001_enter_an_email_address_as_ivavsamplecom():
    """Enter an email address as 'ivav@sample.com'."""
    raise NotImplementedError


@then('Click \'Continue\'')
def test_001_click_continue():
    """Click 'Continue'."""
    raise NotImplementedError


@then('Enter Traveller Details')
def test_001_enter_traveller_details():
    """Enter Traveller Details."""
    raise NotImplementedError


@then('On the Payments page, Use net banking')
def test_001_on_the_payments_page_use_net_banking():
    """On the Payments page, Use net banking."""
    raise NotImplementedError


@then('select \'KOT Bank\' and Click \'Payment\'')
def test_001_select_kot_bank_and_click_payment():
    """select 'KOT Bank' and Click 'Payment'."""
    raise NotImplementedError


@then('Verify KOT Net Banking page has opened up')
def test_001_verify_kot_net_banking_page_has_opened_up():
    """Verify KOT Net Banking page has opened up."""
    raise NotImplementedError


def teardown():
    test_failed_check(driver, scenario_name=scenario_name)
