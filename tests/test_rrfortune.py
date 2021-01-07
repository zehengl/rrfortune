import os

import rollbar
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class RenRenTestClass(BaseCase):
    def test_fortune_collection(self):
        rollbar.init(os.environ.get("rollbar"))

        try:
            email = os.environ.get("email")
            password = os.environ.get("password")

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
            rollbar.report_message("Test Errored")
        else:
            rollbar.report_message("Test Passed")
