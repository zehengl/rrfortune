import os

import rollbar
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

renren = "http://renren.com"


def test_rrfortune():
    """
    test for rrfortune
    """

    rollbar.init(os.environ.get("rollbar"))

    email = os.environ.get("email")
    password = os.environ.get("password")
    assert email and password

    wait_time = int(os.environ.get("wait", 10))

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)

        driver.get(renren)

        input_email = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        input_password = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        btn_login = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "login"))
        )

        input_email.clear()
        input_password.clear()
        input_email.send_keys(email)
        input_password.send_keys(password)
        driver.execute_script("arguments[0].click()", btn_login)

        btn_fortune = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.ID, "assembleBtn"))
        )

        driver.execute_script("arguments[0].click()", btn_fortune)

        popup = WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.ID, "forPopupBox"))
        )

        passed = popup.value_of_css_property("display") == "block"
        if not passed:
            rollbar.report_message("Test Failed")
        assert passed

    except WebDriverException:
        rollbar.report_message("Test Errored")
        assert False

    else:
        rollbar.report_message("Test Passed")
        assert True

    finally:
        driver.quit()
