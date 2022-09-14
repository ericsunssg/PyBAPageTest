from src.SeleniumExtended import SeleniumExtended


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.base_url = 'https://www.anz.com.au/'
        self.url = None

    def go_to(self):
        if self.url:
            self.driver.get(self.url)
        else:
            raise NotImplementedError()
        self.driver.maximize_window()
