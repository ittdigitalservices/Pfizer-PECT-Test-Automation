
#
# Author: ITTDigital
#
@PECT_TC015
Feature: User navigates For Current Clinical Trial Participants and checks URL route

  Scenario: PECT_TC015_A_User_accesses_Current_Clinical_Trial_Participants_and_checks_URL_route
    Given PECT_TC015_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC015_A User navigates to For Participants
    Then PECT_TC015_A User then clicks on the For Current Clinical Trial participants link
    Then PECT_TC015_A User then checks URL route
    
