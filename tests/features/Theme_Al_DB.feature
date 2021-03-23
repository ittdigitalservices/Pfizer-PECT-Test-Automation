
#
# Author: Vinay Srinivasan
#

Feature: Testing_Theme_Al_DB_Website_Functionality

  Scenario: Checking_Cajun_spiced_fish_tacos_dishes_instructions
  Given Go to the ThemeAlDB and check if Avocado exists in the Popular Ingredients
  Then Under the ingredient Avocado check if Cajun spiced fish tacos exists
  Then On clicking the dish name Cajun spiced fish tacos instructions are displayed

  Scenario: Verifying_Katsu_Chicken_curry_and_Nutty_Chicken_Curry_dishes
  Given User visits site ThemeAlDB
  Then Searches for 'Chicken Curry' in 'Search for a meal'
  Then Verify that 2 dishes are found and are named 'Katsu Chicken curry' and 'Nutty Chicken Curry'


