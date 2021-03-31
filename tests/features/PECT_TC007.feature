
#
# Author: ITTDigital
#
@PECT_TC007
Feature: User navigates to 'Any' One of the pages and the tries to check the presence of a video

  Scenario: PECT_TC007_A_Confirm_Presence_of_a_Video_in_a_Page
    Given PECT_TC007_A User Access the Pfizer Eclinical Trial Portal
    Then PECT_TC007_A User navigates to 'Our research' Page
    Then PECT_TC007_A User scrolls down the Landing Page
    Then PECT_TC007_A User then searches for the presence of any Video
    Then PECT_TC007_A User confirms the presence of atleast one Video

