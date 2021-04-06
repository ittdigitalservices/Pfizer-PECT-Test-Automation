
#
# Author: ITTDigital
#
@PECT_TC014
Feature: User navigates a Landing Page End and Performs Go Back To Top

  Scenario: PECT_TC014_A_User_accesses_Clinical_Trial_Participants_and_performs_go_back_to_top
    Given PECT_TC014_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC014_A User navigates to For Participants
    Then PECT_TC014_A User then clicks on the For Current Clinical Trial participants link
    Then PECT_TC014_A User then scrolls down the utmost last of the Landing Page
    Then PECT_TC014_A User then tries use Go Back To Top option

  Scenario: PECT_TC014_B_User_accesses_FAQs_and_performs_go_back_to_top
    Given PECT_TC014_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC014_B User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC014_B User then access About clinical trials
    Then PECT_TC014_B User then accesses the FAQ
    Then PECT_TC014_B User then scrolls down the utmost last of the Landing Page
    Then PECT_TC014_B User then tries use Go Back To Top option

