
#
# Author: ITTDigital
#
@PECT_TC006
Feature: User navigates to 'Our research' page using the 'Our research' link and verifies some Text Content


  Scenario: PECT_TC006_A_Verifies_Text_Content_in_the_Research_Page
    Given PECT_TC006_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC006_A User navigates to 'Our research' Page
    Then PECT_TC006_A User then verifies the presence of 'Visit our Research Page' link
    Then PECT_TC006_A User then accesses 'Visit our Research Page' link by clicking on it
    Then PECT_TC006_A User then verifies some Text Content in the 'Research Page'

