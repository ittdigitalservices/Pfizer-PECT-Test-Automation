
#
# Author: ITTDigital
#
@PECT_TC002
Feature: User accesses the Pfizer Eclinical Trial Portal and accesses the TRIAL section


  Scenario: PECT_TC002_A_verification_of_certain_TRIAL_page_contents

    Given PECT_TC002_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC002_A User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC002_A User then clicks on About clinical trials
    Then PECT_TC002_A User then accesses some of the TRIAL page contents and Verifies them


  Scenario: PECT_TC002_B_Access_the_Trial_Filters

    When PECT_TC002_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC002_B User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC002_B User then clicks on Find a trial
    Then PECT_TC002_B User then accesses the TRIAL Filters


