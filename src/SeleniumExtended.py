
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from polling import poll, TimeoutException

import time

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
            print('wait_and_click: ', locator)
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}'," \
                              f"after timeout of {timeout}"
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return elm.text

    def wait_and_get_value(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return elm.get_attribute('value')


    def wait_till_is_selected(self, locator, parent_locator, is_selected=True, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        parent_elm = elm.find_element(*parent_locator)
        if is_selected:
            poll(lambda x=parent_elm: x.get_attribute('class')=='selected', step=1, timeout=timeout)
        else:
            poll(lambda x=parent_elm: x.get_attribute('class')=='', step=1, timeout=timeout)

    def wait_till_is_invisible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )

