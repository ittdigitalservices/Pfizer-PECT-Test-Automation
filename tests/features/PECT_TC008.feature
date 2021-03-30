
#
# Author: ITTDigital
#
@PECT_TC008
Feature: User accesses the Pfizer Eclinical Trial Portal and Scrolls Down to Contact Us

  Scenario: PECT_TC008_A_Confirm_Presence_of_Contact_Us_in_a_Page

    Given PECT_TC008_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC008_A User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC008_A User then scrolls down the Landing Page
    Then PECT_TC008_A User then verifies the option like 'Contact us' and so on

