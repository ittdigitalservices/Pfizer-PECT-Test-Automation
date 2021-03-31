
#
# Author: ITTDigital
#
@PECT_TC003
Feature: User accesses About PECT Portal and accesses COVID-19 in the Vaccines Page


  Scenario: PECT_TC003_A_Access_COVID_19_information
    Given PECT_TC003_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC003_A User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC003_A User then accesses a COVID-19 information


  Scenario: PECT_TC003_B_verifying_certain_COVID19_information
    Given PECT_TC003_B User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC003_B User Verifies that the Home Icon is present in the Landing Page
    Then PECT_TC003_B User then clicks on Our Research
    Then PECT_TC003_B User then accesses the Vaccines and clicks on it
    Then PECT_TC003_B User then clicks COVID-19 information


  Scenario: PECT_TC003_C_Verifies_COVID_19_displayed_data
    Given PECT_TC003_C User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC003_C User clicks on the Find a Trial link
    Then PECT_TC003_C User then accesses the Search Filter
    Then PECT_TC003_C User then searches for COVID-19 and collects certain displayed data like count
    Then PECT_TC003_C User then searches for covid-19 and collects certain displayed data like count
    Then PECT_TC003_C User then compares the data collected in the above step004 and step005


