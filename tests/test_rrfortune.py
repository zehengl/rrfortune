import os

import rollbar
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class RenRenTestClass(BaseCase):
    def test_fortune_collection(self):
        email = os.environ.get("email")
        password = os.environ.get("password")
        token = os.environ.get("rollbar")

        self.assert_true(email and password and token)

        try:
            rollbar.init(token)
            self.open("http://renren.com")

            self.wait_for_element("email", by=By.ID)
            self.wait_for_element("password", by=By.ID)
            self.type("email", email, by=By.ID)
            self.type("password", password, by=By.ID)
            self.click("login", by=By.ID)

            self.wait_for_element("assembleBtn", by=By.ID)
            self.click("assembleBtn", by=By.ID)

            # self.wait_for_element("forPopupBox", by=By.ID)
            self.assert_element_visible("forPopupBox", by=By.ID)
        except:
            rollbar.report_message("Test Erred")
            self.assert_true(False)
        else:
            rollbar.report_message("Test Passed")
