from pageObjects.LoginPage import LoginPage
from utilities.conftest import *
import allure


class Test_Login:

    @allure.description("Verify that there is a Login header label in Login container")
    def test_verify_login_header_label(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login_header_label()

    def test_verify_mandatory_fields(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login_mandatory_fields()

    def test_valid_email_valid_password(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")

    @allure.description("Verify Proper Validation message appears when email field is invalid")
    def test_wrong_email_valid_password(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "wrong_email"), get_config("CRED", "password"), "Invalid")

    @allure.description("Verify Proper Validation message appears when email field is invalid")
    def test_valid_email_wrong_password(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "wrong_password"), "Invalid")

    @allure.description("Verify Don't have an account? deeplink navigates the user to New Account container")
    def test_signup_link(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_signup_link()

    @allure.description("Verify Forgot Password? deeplink navigates the user to Reset Container")
    def test_verify_forgot_password_link(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_forgot_password_link()

    # test placeholder
    def test_varify_placeholder(self, setup):
        dict = {
            "email_placeholder": "Email",
            "password_placeholder": "Password"
        }
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_placeholder(dict)
        print("at the end of test case")
