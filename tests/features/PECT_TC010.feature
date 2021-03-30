
#
# Author: ITTDigital
#
@PECT_TC010
Feature: User navigates to Our research and accesses Internal Medicine

  Scenario: PECT_TC010_A_User_accesses_Internal_Medicine_from_Research_page
    Given PECT_TC010_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC010_A User navigates to Our research Page
    Then PECT_TC010_A User then clicks on the Internal Medicine link
    Then PECT_TC010_A User then checks the Clinical Trials in Internal Medicine landing page
