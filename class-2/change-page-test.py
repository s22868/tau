import logging
from time import sleep

from selenium import webdriver
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

logger.info('Start change page test')

DRIVER_NAMES = ['chromium', 'Edge']
for driver_name in DRIVER_NAMES:
    if 'Chro' in driver_name:
        logger.info(f'Starting test with {driver_name} browser')
        driver = webdriver.Chrome(options=chop())
    else:
        logger.info(f'Starting test with {driver_name} browser')
        driver = webdriver.Edge(options=edg())

    driver.get('https://github.com')
    sleep(2)
    element= driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button')
    element.click()

    sleep(2)

    login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a')
    login_btn.click()

    logger.info("Move to login page")
    sleep(2)
    current_url = driver.current_url
    expected_url = 'https://github.com/login'
    if current_url == expected_url:
        logger.info(f'Correct transfer to the appropriate url = {current_url}')
    else:
        print(current_url)
        print(expected_url)
        logger.info(f'Incorrect transfer to the appropriate url. You should be on {expected_url}, and you are on {current_url}')

    logger.info(f'End change page test for {driver_name} browser')
    driver.close()