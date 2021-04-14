
#
# Author: ITTDigital
#
@PECT_TC000
Feature: User navigates For Pfizer Clinical Trial and searches for a Trial

  Scenario: PECT_TC016_C_User_accesses_Pfizer_Clinical_Trial_and_Trial_Search_Result_content
    Given PECT_TC016_C User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC016_C User navigates to Find a Trial option at the Top and clicks it
    Then PECT_TC016_C User then accesses Search for a Pfizer clinical trial section
    Then PECT_TC016_C User then enters or populates the search value
    Then PECT_TC016_C User then enters or populates the location value
    Then PECT_TC016_C User then clicks on the Find a trial button
    Then PECT_TC016_C User then access the searched page contents

