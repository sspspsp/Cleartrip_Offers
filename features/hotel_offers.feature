Feature: Offers

  Background: common steps
    Given launch the browser
    When open cleartrip homepage
    And cancel pop-up


  Scenario: Click on offers
    And click on offers
    Then verify offer page is opening
    And click on hotels
    Then verify hotel offers are opening
    And click on any offer
    Then verify details of offer opening
    And click on book now
    Then verify booking window opening
    And click on reset filters
    Then verify filters are resetting
