
import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

renren = 'http://renren.com'
default_wait = 10


def test_():
    email = os.environ.get('email')
    password = os.environ.get('password')
    assert email and password

    wait_time = os.environ.get('wait', default_wait)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(chrome_options=options)

        driver.get(renren)

        input_email = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        input_password = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        btn_login = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, 'login'))
        )

        input_email.clear()
        input_password.clear()
        input_email.send_keys(email)
        input_password.send_keys(password)
        driver.execute_script('arguments[0].click()', btn_login)

        app_live = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li.app-live'))
        )
        profile_link = app_live.find_elements_by_class_name('app-link')[0].get_attribute('href')

        driver.get(profile_link)

        btn_fortune = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, 'assembleBtn'))
        )

        driver.execute_script('arguments[0].click()', btn_fortune)
    except WebDriverException:
        assert False
    else:
        assert True
    finally:
        driver.quit()