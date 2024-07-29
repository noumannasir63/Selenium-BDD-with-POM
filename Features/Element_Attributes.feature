Feature: Test All Attributes of Element

@second
  Scenario: Open the Text Box Attribute
    Given Element Dropdown is open and clicks on Text Box Attribute
    When User give first name
    And User give Email of Text Box
    And User provide current Address
    And User provide permanent Address
    Then User clicks on submit button