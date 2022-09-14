from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage


class MuchBorrowPage(BasePage):

    def __init__(self, driver):
        super(MuchBorrowPage, self).__init__(driver)
        print('MuchBorrowPage init')
        self.url = self.base_url + 'personal/home-loans/calculators-tools/much-borrow/'

    # Details locator
    SINGLE = (By.CSS_SELECTOR, "label[for='application_type_single']")
    JOINT = (By.CSS_SELECTOR, "label[for='application_type_joint']")
    NUM_OF_DEP = (By.CSS_SELECTOR, "select[title = 'Number of dependants']")
    OPTIONS = (By.TAG_NAME, "option")
    HOME_TO_LIVE_IN = (By.CSS_SELECTOR, "label[for='borrow_type_home']")
    RESIDENTIAL_INVESTMENT = (By.CSS_SELECTOR, "label[for='borrow_type_investment']")

    # Earnings locator
    ANNUAL_INCOME = (By.CSS_SELECTOR, "input[aria-labelledby='q2q1']")
    OTHER_INCOME = (By.CSS_SELECTOR, "input[aria-labelledby='q2q2']")
    SECOND_ANNUAL_INCOME = (By.CSS_SELECTOR, "input[aria-labelledby='q2q3']")
    SECOND_OTHER_INCOME = (By.CSS_SELECTOR, "input[aria-labelledby='q2q4']")

    # Expenses locator
    MONTHLY_LIVING_EXPENSES = (By.CSS_SELECTOR, "input[aria-labelledby='q3q1']")
    CURRENT_HOME_LOAN_MONTHLY_REPAYMENTS = (By.CSS_SELECTOR, "input[aria-labelledby='q3q2']")
    OTHER_LOAN_MONTHLY_REPAYMENTS = (By.CSS_SELECTOR, "input[aria-labelledby='q3q3']")
    OTHER_MONTHLY_COMMITMENTS = (By.CSS_SELECTOR, "input[aria-labelledby='q3q4']")
    TOTAL_CREDIT_CARD_LIMITS = (By.CSS_SELECTOR, "input[aria-labelledby='q3q5']")

    WORK_OUT_HOW_MUCH_I_CAN_BORROW = (By.CSS_SELECTOR, "#btnBorrowCalculater")
    BORROW_AMOUNT_RESULT = (By.CSS_SELECTOR, "#borrowResultTextAmount")
    START_OVER = (By.CSS_SELECTOR, "div[class='result__restart'] button[aria-label='Start over']")

    PARENT = (By.XPATH, "..")

    def select_application_type(self, app_type):
        if app_type == 'Single':
            self.sl.wait_and_click(MuchBorrowPage.SINGLE)
        elif app_type == 'Joint':
            self.sl.wait_and_click(MuchBorrowPage.JOINT)
        else:
            raise Exception('Application type {} is not supported'.format(app_type))

    def application_type_is_selected(self, app_type, is_selected=True):
        if app_type == 'Single':
            loc= MuchBorrowPage.SINGLE
        elif app_type == 'Joint':
            loc = MuchBorrowPage.JOINT
        else:
            raise Exception('Application type {} is not supported'.format(app_type))

        if is_selected:
            self.sl.wait_till_is_selected(loc, MuchBorrowPage.PARENT)
        else:
            self.sl.wait_till_is_selected(loc, MuchBorrowPage.PARENT, is_selected=False)


    def select_number_of_dependants(self, num):

        if int(num) >= 5:
            num = '5+'

        self.sl.wait_until_element_is_visible(MuchBorrowPage.NUM_OF_DEP)
        for opt in self.sl.wait_and_get_elements(MuchBorrowPage.OPTIONS):
            if opt.text == num:
                opt.click()
                break

    def get_number_of_dependants(self):
        self.sl.wait_until_element_is_visible(MuchBorrowPage.NUM_OF_DEP)
        for opt in self.sl.wait_and_get_elements(MuchBorrowPage.OPTIONS):
            if opt.is_selected():
                return opt.text

    def select_borrow_type(self, borrow_type):
        if borrow_type == 'Home to live in':
            self.sl.wait_and_click(MuchBorrowPage.HOME_TO_LIVE_IN)
        elif borrow_type == 'Residential investment':
            self.sl.wait_and_click(MuchBorrowPage.RESIDENTIAL_INVESTMENT)
        else:
            raise Exception('Borrow type {} is not supported'.format(borrow_type))

    def borrow_type_is_selected(self, borrow_type, is_selected=True):
        if borrow_type == 'Home to live in':
            loc= MuchBorrowPage.HOME_TO_LIVE_IN
        elif borrow_type == 'Residential investment':
            loc = MuchBorrowPage.RESIDENTIAL_INVESTMENT
        else:
            raise Exception('Application type {} is not supported'.format(borrow_type))

        if is_selected:
            self.sl.wait_till_is_selected(loc, MuchBorrowPage.PARENT)
        else:
            self.sl.wait_till_is_selected(loc, MuchBorrowPage.PARENT, is_selected=False)

    def fill_in_major_annual_income(self, income):
        self.sl.wait_and_input_text(MuchBorrowPage.ANNUAL_INCOME, income)

    def get_major_annual_income(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.ANNUAL_INCOME)

    def fill_in_major_other_income(self, income):
        self.sl.wait_and_input_text(MuchBorrowPage.OTHER_INCOME, income)

    def get_major_other_income(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.OTHER_INCOME)

    def fill_in_second_annual_income(self, income):
        self.sl.wait_and_input_text(MuchBorrowPage.SECOND_ANNUAL_INCOME, income)

    def second_annual_income_is_invisible(self):
        self.sl.wait_till_is_invisible(MuchBorrowPage.SECOND_ANNUAL_INCOME)

    def fill_in_second_other_income(self, income):
        self.sl.wait_and_input_text(MuchBorrowPage.SECOND_OTHER_INCOME, income)

    def second_other_income_is_invisible(self):
        self.sl.wait_till_is_invisible(MuchBorrowPage.SECOND_OTHER_INCOME)

    def fill_in_monthly_living_expenses(self, expense):
        self.sl.wait_and_input_text(MuchBorrowPage.MONTHLY_LIVING_EXPENSES, expense)

    def get_monthly_living_expenses(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.MONTHLY_LIVING_EXPENSES)

    def fill_in_current_home_loan_monthly_repayments(self, expense):
        self.sl.wait_and_input_text(MuchBorrowPage.CURRENT_HOME_LOAN_MONTHLY_REPAYMENTS, expense)

    def get_current_home_loan_monthly_repayments(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.CURRENT_HOME_LOAN_MONTHLY_REPAYMENTS)

    def fill_in_other_loan_monthly_repayments(self, expense):
        self.sl.wait_and_input_text(MuchBorrowPage.OTHER_LOAN_MONTHLY_REPAYMENTS, expense)

    def get_other_loan_monthly_repayments(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.OTHER_LOAN_MONTHLY_REPAYMENTS)

    def fill_in_other_monthly_commitments(self, expense):
        self.sl.wait_and_input_text(MuchBorrowPage.OTHER_MONTHLY_COMMITMENTS, expense)

    def get_other_monthly_commitments(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.OTHER_MONTHLY_COMMITMENTS)

    def fill_in_total_credit_card_limits(self, expense):
        self.sl.wait_and_input_text(MuchBorrowPage.TOTAL_CREDIT_CARD_LIMITS, expense)

    def get_total_credit_card_limits(self):
        return self.sl.wait_and_get_value(MuchBorrowPage.TOTAL_CREDIT_CARD_LIMITS)

    def click_how_much_can_borrow(self):
        self.sl.wait_and_click(MuchBorrowPage.WORK_OUT_HOW_MUCH_I_CAN_BORROW)

    def get_borrow_amount_result(self):
        amount =  self.sl.wait_and_get_text(MuchBorrowPage.BORROW_AMOUNT_RESULT)
        return amount[1:].replace(',', '')

    def click_start_over(self):
        self.sl.wait_and_click(MuchBorrowPage.START_OVER)
