
#
# Author: ITTDigital
#
@PECT_TC013
Feature: User navigates For Current Clinical Trial Participants and verifies Download option presence

  Scenario: PECT_TC013_A_User_accesses_Clinical_Trial_Participants_and_verifies_Download_option
    Given PECT_TC013_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC013_A User navigates to For Participants
    Then PECT_TC013_A User then clicks on the For Current Clinical Trial participants link
    Then PECT_TC013_A User then checks the Download Option presence in the landing page
