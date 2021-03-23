
#
# Author: ITTDigital
#
@PECT_TC000
Feature: User accesses About PECT Portal and accesses COVID-19 in the Vaccines Page


  Scenario: PECT_TC003_C_Verifies_COVID_19_displayed_data
    Given User Access the Pfizer Eclinical Trial Application Portal
    Then User clicks on the Find a Trial link
    Then User then accesses the Search Filter
    Then User then searches for COVID-19 and collects certain displayed data like count
    Then User then searches for covid-19 and collects certain displayed data like count
    Then User then compares the data collected in the above step004 and step005


