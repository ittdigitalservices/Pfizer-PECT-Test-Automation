# coding=utf-8
#
# AUTHOR : Vinay Srinivasan
#

import pytest
import pytest_bdd
import selenium

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import utilities
from utilities.screenshot_utils import test_failed_check

#FireFoxWebDriverPath = "./webdrivers/win/geckodriver.exe"
ChromeDriverPath = "./webdrivers/win/chromedriver.exe"
ThemeAlDB = "https://www.themealdb.com/"

feature_name = "../features/test_000_Theme_Al_DB.feature"

#driver = selenium.webdriver.firefox.webdriver.WebDriver(executable_path=FireFoxWebDriverPath)
#driver = selenium.webdriver.chrome.webdriver.WebDriver(executable_path=ChromeDriverPath)
driver = utilities.browser_utils.MyBrowser().get_browser()


def setup():
    # driver = selenium.webdriver.firefox.webdriver.WebDriver(executable_path=FireFoxWebDriverPath)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


scenario_name = 'Checking_Cajun_spiced_fish_tacos_dishes_instructions'


@scenario(feature_name='../features/Theme_Al_DB.feature',
          scenario_name=scenario_name)
def test_000_checking_cajun_spiced_fish_tacos_dishes_instructions():
    """Checking_Cajun_spiced_fish_tacos_dishes_instructions."""
    pass


@given("Go to the ThemeAlDB and check if Avocado exists in the Popular Ingredients")
def test_000_go_to_the_themealdb_and_check_if_avocado_exists_in_the_popular_ingredients():
    """Go to the ThemeAlDB and check if Avocado exists in the Popular Ingredients."""
    driver.get(ThemeAlDB)
    driver.implicitly_wait(10)
    driver.get("https://www.themealdb.com/browse.php?s=Avocado")


@then("Under the ingredient Avocado check if Cajun spiced fish tacos exists")
def test_000_under_the_ingredient_avocado_check_if_cajun_spiced_fish_tacos_exists():
    """Under the ingredient Avocado check if Cajun spiced fish tacos exists.."""
    driver.implicitly_wait(10)
    driver.get("https://www.themealdb.com/meal.php?c=52960")


@then("On clicking the dish name Cajun spiced fish tacos instructions are displayed")
def test_000_on_clicking_the_dish_name_cajun_spiced_fish_tacos_instructions_are_displayed():
    """On clicking the dish name Cajun spiced fish tacos instructions are displayed."""
    driver.implicitly_wait(10)
    driver.get("https://www.themealdb.com/ingredient/2-Salmon")


scenario_name = 'Verifying_Katsu_Chicken_curry_and_Nutty_Chicken_Curry_dishes'


@scenario(feature_name='../features/Theme_Al_DB.feature', scenario_name=scenario_name)
def test_000_verifying_katsu_chicken_curry_and_nutty_chicken_curry_dishes():
    """Verifying_Katsu_Chicken_curry_and_Nutty_Chicken_Curry_dishes."""
    pass


@given("User visits site ThemeAlDB")
def test_000_user_visits_site_themealdb():
    """User visits site ThemeAlDB."""
    driver.get(ThemeAlDB)


@then("Searches for 'Chicken Curry' in 'Search for a meal'")
def test_000_searches_for_chicken_curry_in_search_for_a_meal():
    """Searches for 'Chicken Curry' in 'Search for a meal'."""
    driver.implicitly_wait(10)
    driver.get("https://www.themealdb.com/browse.php?s=katsu")


@then("Verify that 2 dishes are found and are named 'Katsu Chicken curry' and 'Nutty Chicken Curry'")
def test_000_verify_that_2_dishes_are_found_and_are_named_katsu_chicken_curry_and_nutty_chicken_curry():
    """Verify that 2 dishes are found and are named 'Katsu Chicken curry' and 'Nutty Chicken Curry'."""
    driver.implicitly_wait(10)
    driver.get("https://www.themealdb.com/meal.php?c=52820")


def teardown():
    test_failed_check(driver, scenario_name=scenario_name)
    # driver.close()
    # driver.quit()
