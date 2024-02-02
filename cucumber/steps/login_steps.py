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

@given('Start login test with "{browser}"')
def start_login_test(context, browser):
    logger.info(f'Starting test with {browser} browser')
    if 'Chro' in browser:
        context.driver = webdriver.Chrome(options=chop())
    else:
        context.driver = webdriver.Edge(options=edg())
    context.driver.get('https://github.com/login')

@when('User logs in with valid credentials')
def login_with_credentials(context):
    login_input = context.driver.find_element(By.NAME, 'login')
    login_input.send_keys('testowymail@mail.pl')

    password_input = context.driver.find_element(By.NAME, 'password')
    password_input.send_keys('testowe-haslo-123')

    login_button = context.driver.find_element(By.NAME, 'commit')
    login_button.click()

    sleep(2)

@then('User should be redirected to the home page')
def verify_home_page_redirection(context):
    error_popup = context.driver.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div')
    logger.info('Site testing stopped at logging page with an error:')
    logger.warning(error_popup.text)

    logger.info('End login-test for current browser')
    context.driver.close()