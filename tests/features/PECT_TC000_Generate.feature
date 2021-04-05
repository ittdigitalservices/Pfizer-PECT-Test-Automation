
#
# Author: ITTDigital
#
@PECT_TC000
Feature: User navigates For Current Clinical Trial Participants and verifies Download option presence

  Scenario: PECT_TC013_A_User_accesses_Clinical_Trial_Participants_and_verifies_Download_option
    Given PECT_TC012_A User navigates to For Participants
    Then User then clicks on the For Current Clinical Trial participants link
    Then User then checks the Download Option presence in the landing page
