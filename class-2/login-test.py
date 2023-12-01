import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edg

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('Start login test')

DRIVER_NAMES = ['chromium', 'Edge']
for driver_name in DRIVER_NAMES:
    if 'Chro' in driver_name:
        logger.info(f'Starting test with {driver_name} browser')
        driver = webdriver.Chrome(options=chop())
    else:
        logger.info(f'Starting test with {driver_name} browser')
        driver = webdriver.Edge(options=edg())

    driver.get('https://github.com/login')

    login_input = driver.find_element(By.NAME, 'login')
    login_input.send_keys('testowymail@mail.pl')

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('testowe-haslo-123')

    login_button = driver.find_element(By.NAME, 'commit')
    login_button.click()

    sleep(2)

    error_popup = driver.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div')
    logger.info('Site testing stopped at logging page with an error:')
    logger.warning(error_popup.text)

    logger.info(f'End login-test for {driver_name} browser')
    driver.close()