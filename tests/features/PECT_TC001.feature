
#
# Author: ITTDigital
#
@PECT_TC001
Feature: User accesses the Pfizer Eclinical Trial Portal and verifies certain Home Page content


  Scenario: PECT_TC001_A_Verification_of_Landing_Page
    Given PECT_TC001_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC001_A User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC001_A User Accesses some of the Text Content and Verifies the Landing Page


  Scenario: PECT_TC001_B_Verification_of_certain_Home_Page_contents
    Given PECT_TC001_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC001_B User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC001_B User Accesses some of the Displayed Information Content and Verifies them



