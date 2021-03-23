
#
# Author: ITTDigital
#
@PECT_TC002
Feature: User accesses the Pfizer Eclinical Trial Portal and accesses the TRIAL section

  Scenario: PECT_TC002_A_verification_of_certain_TRIAL_page_contents
    Given User Access the Pfizer Eclinical Trial Application Portal
    Then User Verifies that the Home Icon is present in the Landing Page
    Then User then clicks on About clinical trials
    Then User then accesses some of the TRIAL page contents and Verifies them

  Scenario: PECT_TC002_B_Access_the_Trial_Filters
    Given User Access the Pfizer Eclinical Trial Application Portal
    Given User Verifies that the Home Icon is present in the Landing Page
    Given User then clicks on Find a trial
    Given User then accesses the TRIAL Filters


