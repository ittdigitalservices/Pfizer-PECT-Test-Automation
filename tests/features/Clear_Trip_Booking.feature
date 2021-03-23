
#
# Author: Vinay Srinivasan
#

Feature: Testing Clear Trip Booking

  Scenario: Testing_Clear_Trip_WebSite_Booking
    Given Testing of Clear Trip Booking for 02
    Then Launch Chrome Web Driver
    Then Navigate to Clear Trip Web Site
    Then Select 'Flights' tab
    Then Search Round Trip flight from Mum to Delhi
    Then Depart Date is 5 days from Today
    And Return date is 6 days from today
    Then Select Adults travelling = 2
    Then Click on 'Search'
    Then Select a Non-Stop Flight
    Then Select the 02nd Spice Jet or Indigo from depart
    Then Select the 02nd Jet Airways or Go Air from return
    Then Click Booking
    And Avoid or Skip any insurance
    And Accept the terms and conditions
    And Click Continue Booking
    And Enter an email address as 'ivav@sample.com'
    Then Click 'Continue'
    Then Enter Traveller Details
    Then On the Payments page, Use net banking
    Then select 'KOT Bank' and Click 'Payment'
    Then Verify KOT Net Banking page has opened up

