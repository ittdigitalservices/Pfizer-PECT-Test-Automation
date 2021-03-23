
#
# Author: ITTDigital
#
@PECT_TC003
Feature: User accesses About PECT Portal and accesses COVID-19 in the Vaccines Page


  Scenario: PECT_TC003_A_Access_COVID_19_information
    Given User Access the Pfizer Eclinical Trial Application Portal
    Then User Verifies that the Home Icon is present in the Landing Page
    Then User then accesses a COVID-19 information


  Scenario: PECT_TC003_B_verifying_certain_COVID19_information
    Given User Access the Pfizer Eclinical Trial Application Portal
    Then User Verifies that the Home Icon is present in the Landing Page
    Then User then clicks on Our Research
    Then User then accesses the Vaccines and clicks on it
    Then User then clicks COVID-19 information


  Scenario: PECT_TC003_C_Verifies_COVID_19_displayed_data
    Given User Access the Pfizer Eclinical Trial Application Portal
    Then User clicks on the Find a Trial link
    Then User then accesses the Search Filter
    Then User then searches for COVID-19 and collects certain displayed data like count
    Then User then searches for covid-19 and collects certain displayed data like count
    Then User then compares the data collected in the above step004 and step005


