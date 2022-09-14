from behave import given, when, then
from polling import poll, TimeoutException
from src.pages.MuchBorrowPage import MuchBorrowPage

@given('I go to borrow amount calculation page')
def step_impl(context):
    context.page = MuchBorrowPage(context.driver)
    context.page.go_to()

@when('application type is {app_type}')
@given('application type is {app_type}')
def step_impl(context, app_type):
    context.page.select_application_type(app_type)

@when('number of dependants is {num_of_dep}')
@given('number of dependants is {num_of_dep}')
def step_impl(context, num_of_dep):
    context.page.select_number_of_dependants(num_of_dep)

@then('number of dependants is {num_of_dep}')
def step_impl(context, num_of_dep):
    if int(num_of_dep) >= 5:
        num_of_dep = '5+'
    actual_number = context.page.get_number_of_dependants()
    assert actual_number == num_of_dep, 'actual value: {}, expected value: {}'.format(actual_number, num_of_dep)

@when('borrow type is {borrow_type}')
@given('borrow type is {borrow_type}')
def step_impl(context, borrow_type):
    context.page.select_borrow_type(borrow_type)

@when('major annual income is {annual_income}')
@given('major annual income is {annual_income}')
def step_impl(context, annual_income):
    context.page.fill_in_major_annual_income(annual_income)

@then('major annual income is {annual_income}')
def step_impl(context, annual_income):
    actual_value = context.page.get_major_annual_income()
    assert actual_value == annual_income, 'actual value: {}, expected value: {}'.format(actual_value, annual_income)

@when('major other income is {other_income}')
@given('major other income is {other_income}')
def step_impl(context, other_income):
    context.page.fill_in_major_other_income(other_income)

@then('major other income is {other_income}')
def step_impl(context, other_income):
    actual_value = context.page.get_major_other_income()
    assert actual_value == other_income, 'actual value: {}, expected value: {}'.format(actual_value, other_income)

@when('second annual income is {annual_income}')
@given('second annual income is {annual_income}')
def step_impl(context, annual_income):
    context.page.fill_in_second_annual_income(annual_income)

@then('second annual income is invisible')
def step_impl(context):
    context.page.second_annual_income_is_invisible()

@when('second other income is {other_income}')
@given('second other income is {other_income}')
def step_impl(context, other_income):
    context.page.fill_in_second_other_income(other_income)

@then('second other income is invisible')
def step_impl(context):
    context.page.second_other_income_is_invisible()

@when('monthly living expenses is {expense}')
@given('monthly living expenses is {expense}')
def step_impl(context, expense):
    context.page.fill_in_monthly_living_expenses(expense)

@then('monthly living expenses is {expense}')
def step_impl(context, expense):
    actual_value = context.page.get_monthly_living_expenses()
    assert actual_value == expense, 'actual value: {}, expected value: {}'.format(actual_value, expense)

@when('current home loan monthly repayments is {expense}')
@given('current home loan monthly repayments is {expense}')
def step_impl(context, expense):
    context.page.fill_in_current_home_loan_monthly_repayments(expense)

@then('current home loan monthly repayments is {expense}')
def step_impl(context, expense):
    actual_value = context.page.get_current_home_loan_monthly_repayments()
    assert actual_value == expense, 'actual value: {}, expected value: {}'.format(actual_value, expense)

@when('other loan monthly repayments is {expense}')
@given('other loan monthly repayments is {expense}')
def step_impl(context, expense):
    context.page.fill_in_other_loan_monthly_repayments(expense)

@then('other loan monthly repayments is {expense}')
def step_impl(context, expense):
    actual_value = context.page.get_other_loan_monthly_repayments()
    assert actual_value == expense, 'actual value: {}, expected value: {}'.format(actual_value, expense)

@when('other monthly commitments is {expense}')
@given('other monthly commitments is {expense}')
def step_impl(context, expense):
    context.page.fill_in_other_monthly_commitments(expense)

@then('other monthly commitments is {expense}')
def step_impl(context, expense):
    actual_value = context.page.get_other_monthly_commitments()
    assert actual_value == expense, 'actual value: {}, expected value: {}'.format(actual_value, expense)

@when('total credit card limits is {expense}')
@given('total credit card limits is {expense}')
def step_impl(context, expense):
    context.page.fill_in_total_credit_card_limits(expense)

@then('total credit card limits is {expense}')
def step_impl(context, expense):
    actual_value = context.page.get_total_credit_card_limits()
    assert actual_value == expense, 'actual value: {}, expected value: {}'.format(actual_value, expense)

@when("click 'Work out how much I could borrow'")
def step_impl(context):
    context.page.click_how_much_can_borrow()

@when("click 'Start over'")
def step_impl(context):
    context.page.click_start_over()

@given('fill in all fields')
def step_impl(context):
    context.execute_steps(u"""
        Given application type is Joint
        And number of dependants is 10
        And borrow type is Residential investment
        And major annual income is 80000
        And major other income is 10000
        And second annual income is 90000
        And second other income is 500
        And monthly living expenses is 100
        And current home loan monthly repayments is 200
        And other loan monthly repayments is 300
        And other monthly commitments is 400
        And total credit card limits is 500  
        """)

@then('the borrow amount is expected to be {amount}')
def step_impl(context, amount):
    try:
        poll(lambda: context.page.get_borrow_amount_result()==amount, step=1, timeout=10)
    except TimeoutException:
        actual_value = context.page.get_borrow_amount_result()
        assert actual_value == amount, 'actual value: {}, expected value: {}'.format(actual_value, amount)

@then('application type {app_type} is selected')
def step_impl(context, app_type):
    context.page.application_type_is_selected(app_type)

@then('application type {app_type} is not selected')
def step_impl(context, app_type):
    context.page.application_type_is_selected(app_type, False)

@then('borrow type {borrow_type} is selected')
def step_impl(context, borrow_type):
    context.page.borrow_type_is_selected(borrow_type)

@then('borrow type {borrow_type} is not selected')
def step_impl(context, borrow_type):
    context.page.borrow_type_is_selected(borrow_type, False)
