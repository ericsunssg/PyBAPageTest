import os
from src.util.config import get_config, set_up_web_driver


def before_all(context):
    path = os.path.dirname(os.path.realpath(__file__))
    browser = get_config(path+'\\config.json')['browser']
    context.driver = set_up_web_driver(browser)

def after_all(context):
    if getattr(context, 'driver', None):
        context.driver.quit()