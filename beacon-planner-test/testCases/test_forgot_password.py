from pageObjects.ForgotPasswordPage import ForgotPasswordPage
from utilities.conftest import *
import allure


class Test_Forgot_Password:
    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_forgot_password_link(self, setup):
        self.url_browser(setup)
        self.forgotPasswordPage = ForgotPasswordPage(self.driver)
        self.forgotPasswordPage.check_forgot_password_link()

    def test_verify_reset_email(self, setup):
        self.url_browser(setup)
        self.forgotPasswordPage = ForgotPasswordPage(self.driver)
        self.forgotPasswordPage.check_password_reset_email(get_config("DETAIL", "email"))

    def test_verify_back_to_button(self, setup):
        self.url_browser(setup)
        self.forgotPasswordPage = ForgotPasswordPage(self.driver)
        self.forgotPasswordPage.check_back_button_to_login()
