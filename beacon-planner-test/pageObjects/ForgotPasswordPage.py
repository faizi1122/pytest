import time
from selenium.webdriver.common.by import By
from utilities.conftest import *
from pageObjects.common.BasePage import BasePage


class ForgotPasswordPage(BasePage):
    forgot_password_locator = {
        "forgot_password_link": (By.XPATH, ".//span[contains(text(),'Forgot password?')]"),
        "reset_label": (By.XPATH, './/h1[text()="Reset"]'),
        "reset_message": (By.XPATH, './/h1[text()="Check your inbox"]'),
        "email_field": (By.XPATH, './/input[@type="text"]'),
        "reset_password_button": (By.XPATH, './/span[text()=" Reset Password "]'),
        "back_to_login_button": (By.XPATH, './/span[text()="Back to Login"]'),
        "login_page_label": (By.XPATH, './/h1[text()="Login"]'),
    }

    def check_forgot_password_link(self):
        self.click_element(self.forgot_password_locator["forgot_password_link"])
        reset = self.get_element_text(self.find_element(self.forgot_password_locator["reset_label"]))
        if reset == "Reset":
            assert True, "The user is able to reset link"
            time.sleep(2)
        else:
            try:
                assert False, "The user is not navigate to email sent page"
            except AssertionError as err:
                print(err)

    def check_password_reset_email(self, email):
        self.click_element(self.forgot_password_locator["forgot_password_link"])
        self.send_text_to_element(self.find_element(self.forgot_password_locator["email_field"]), email)
        self.click_element(self.forgot_password_locator["reset_password_button"])
        reset_link = self.get_element_text(self.find_element(self.forgot_password_locator['reset_message']))
        if reset_link == "Check your inbox":
            assert True, "The user is navigated to email sent success message"
        else:
            try:
                assert False, "The user is not navigate to email sent page"
            except AssertionError as err:
                print(err)

    def check_back_button_to_login(self):
        self.check_password_reset_email(get_config("CRED", "email"))
        self.click_element(self.forgot_password_locator["back_to_login_button"])
        login = self.get_element_text(self.find_element(self.forgot_password_locator["login_page_label"]))
        if login == "Login":
            assert True, "The user is navigated to login page"
        else:
            try:
                assert False, "The user is not navigated to login page"
            except AssertionError as err:
                print(err)
