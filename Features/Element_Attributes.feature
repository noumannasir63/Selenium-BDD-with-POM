Feature: Test All Attributes of Element


  Scenario: Open the Text Box Attribute
    Given Element Dropdown is open and clicks on Text Box Attribute
    When User give first name
    And User give Email of Text Box
    And User provide current Address
    And User provide permanent Address
    And User clicks on submit button
    Then verify that assertion result

  Scenario: Open the Check Box Attribute
    Given Element Dropdown is open and clicks on Check Box Attribute
    When User clicks on the Home Toggle bottom