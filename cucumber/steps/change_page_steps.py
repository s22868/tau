import logging
from time import sleep
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.edge.options import Options as edg
from selenium.webdriver.common.by import By

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

@given('Start change page test with "{browser}"')
def start_change_page_test(context, browser):
    logger.info(f'Starting test with {browser} browser')
    if 'Chro' in browser:
        context.driver = webdriver.Chrome(options=chop())
    else:
        context.driver = webdriver.Edge(options=edg())
    context.driver.get('https://github.com')
    sleep(2)

@when('User clicks on login button')
def click_login_button(context):
    element = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button')
    element.click()
    sleep(2)

    login_btn = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a')
    login_btn.click()

@then('User should be redirected to the login page')
def verify_login_page_redirection(context):
    sleep(2)
    current_url = context.driver.current_url
    expected_url = 'https://github.com/login'
    if current_url == expected_url:
        logger.info(f'Correct transfer to the appropriate url = {current_url}')
    else:
        print(current_url)
        print(expected_url)
        logger.info(f'Incorrect transfer to the appropriate url. You should be on {expected_url}, and you are on {current_url}')

    logger.info('End change page test for current browser')
    context.driver.close()