
#
# Author: ITTDigital
#
@PECT_TC016
Feature: User navigates For Pfizer Clinical Trial and searches for a Trial

  Scenario: PECT_TC016_A_User_navigates_to_Find_a_Pfizer_Clinical_Trial_and_searches_a_Trial
    Given PECT_TC016_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC016_A User navigates to Find a Pfizer Clinical Trial segment of the home page
    Then PECT_TC016_A User then enters or populates the search value
    Then PECT_TC016_A User then enters or populates the location value
    Then PECT_TC016_A User then clicks on Find a Trial button


  Scenario: PECT_TC016_B_User_accesses_Pfizer_Clinical_Trial_and_searches_a_Trial
    Given PECT_TC016_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC016_B User navigates to Find a Trial option at the Top and clicks it
    Then PECT_TC016_B User then accesses Search for a Pfizer clinical trial section
    Then PECT_TC016_B User then enters or populates the search value
    Then PECT_TC016_B User then enters or populates the location value
    Then PECT_TC016_B User then clicks on the Find a trial button


  Scenario: PECT_TC016_C_User_accesses_Pfizer_Clinical_Trial_and_Trial_Search_Result_content
    Given PECT_TC016_C User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC016_C User navigates to Find a Trial option at the Top and clicks it
    Then PECT_TC016_C User then accesses Search for a Pfizer clinical trial section
    Then PECT_TC016_C User then enters or populates the search value
    Then PECT_TC016_C User then enters or populates the location value
    Then PECT_TC016_C User then clicks on the Find a trial button
    Then PECT_TC016_C User then access the searched page contents


