Feature: 'Start over' Button

  Scenario: Clicking 'Start over' button to clear the form
    Given I go to borrow amount calculation page
    And fill in all fields
    When click 'Start over'
    Then application type Single is selected
    And  application type Joint is not selected
    And number of dependants is 0
    And borrow type Home to live in is selected
    And borrow type Residential investment is not selected
    And major annual income is 0
    And major other income is 0
    And second annual income is invisible
    And second other income is invisible
    And monthly living expenses is 0
    And current home loan monthly repayments is 0
    And other loan monthly repayments is 0
    And other monthly commitments is 0
    And total credit card limits is 0



