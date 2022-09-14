import os
import json
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

def get_config(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

def set_up_web_driver(browser):
    if browser == 'chrome':
        webdriver_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] + '\\driver\\chrome'
        try:
            driver = webdriver.Chrome(executable_path= webdriver_dir + "\\chromedriver.exe")
        except SessionNotCreatedException as ex:
            # Please check Chrome and chromedriver versions
            # SessionNotCreatedException indicates that their versions do not match.
            raise SessionNotCreatedException(ex.msg)
        driver.implicitly_wait(3)
        return driver
    else:
        raise NotImplementedError('Webdriver {} is not supported yet.'.format(browser))
