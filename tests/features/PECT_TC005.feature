
#
# Author: ITTDigital
#
@PECT_TC005
Feature: User accesses About Pfizer Eclinical Trial Portal and accesses Other Diseases in the Vaccines Page


  Scenario: PECT_TC005_A_Accesses_Other_Diseases_in_Vaccines_Page
    Given PECT_TC005_A User Access the Pfizer Eclinical Trial Application Portal
    Then PECT_TC005_A User navigates to Our research Page
    Then PECT_TC005_A User then clicks on the Vaccines link
    Then PECT_TC005_A User then checks whether Other Diseases are mentioned or not
    Then PECT_TC005_A User verifies the presence of Respiratory diseases and so on
