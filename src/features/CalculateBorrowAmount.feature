Feature: Borrow Amount Calculation

  Scenario: Calculate borrow amount when application type is Single
    Given I go to borrow amount calculation page
    When application type is Single
    And number of dependants is 0
    And borrow type is Home to live in
    And major annual income is 80000
    And major other income is 10000
    And monthly living expenses is 300
    And current home loan monthly repayments is 0
    And other loan monthly repayments is 100
    And other monthly commitments is 0
    And total credit card limits is 10000
    And click 'Work out how much I could borrow'
    Then the borrow amount is expected to be 451000


