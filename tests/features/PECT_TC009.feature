
#
# Author: ITTDigital
#
@PECT_TC009
Feature: User accesses About Pfizer Eclinical Trial Portal and accesses FAQs

  Scenario: PECT_TC009_A_Accesses_FAQs_in_the_Landing_Page
    Given PECT_TC009_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC009_A User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC009_A User then hovers over About clinical trials
    Then PECT_TC009_A User then accesses the FAQ


  Scenario: PECT_TC009_B_Accesses_FAQs_in_the_Landing_Page
    Given PECT_TC009_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC009_B User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC009_B User then clicks on About clinical trials
    Then PECT_TC009_B User then accesses the FAQ


  Scenario: PECT_TC009_C_Searches_FAQ_in_the_Landing_Page
    Given PECT_TC009_C User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC009_C User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC009_C User then accesses About clinical trials
    Then PECT_TC009_C User then accesses the FAQ
    Then PECT_TC009_C User then searches the FAQ


  Scenario: PECT_TC009_D_Accesses_FAQ_and_Expands_the_FAQ_sections
    Given PECT_TC009_D User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC009_D User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC009_D User then access About clinical trials
    Then PECT_TC009_D User then accesses the FAQ
    Then PECT_TC009_D User then clicks Expand all

  Scenario: PECT_TC009_E_Accesses_FAQ_then_Expands_and_Collapses_the_sections
    Given PECT_TC009_E User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC009_E User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC009_E User then access About clinical trials
    Then PECT_TC009_E User then accesses the FAQ
    Then PECT_TC009_E User then clicks Expand all
    Then PECT_TC009_E User then clicks Collapse all


