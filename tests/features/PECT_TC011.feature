
#
# Author: ITTDigital
#
@PECT_TC011
Feature: User navigates to Internal Medicine Page and accesses Like and Dislike button

  Scenario: PECT_TC011_A_User_accesses_Internal_Medicine_and_clicks_thumbs_up
    Given PECT_TC011_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC011_A User navigates to Our research Page
    Then PECT_TC011_A User then clicks on the Internal Medicine link
    Then PECT_TC011_A User then checks the Clinical Trials in landing page
    Then PECT_TC011_A User then clicks on the Like button of the page


  Scenario: PECT_TC011_B_User_accesses_Internal_Medicine_and_checks_thumbs_down
    Given PECT_TC011_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC011_B User navigates to Our research Page
    Then PECT_TC011_B User then clicks on the Internal Medicine link
    Then PECT_TC011_B User then checks the Clinical Trials in landing page
    Then PECT_TC011_B User then checks on the Dislike button of the page


