from pageObjects.RegistrationPage import RegistrationPage
from utilities.conftest import *


class Test_Register:

    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_all_valid_fields(self, setup):
        self.url_browser(setup)
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.check_all_valid_fields()

    def test_duplicate_email(self, setup):
        self.url_browser(setup)
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.check_duplicate_email(get_config("CRED", "name"), get_config("CRED", "email"),
                                                    get_config("CRED", "password"))

    def test_verify_back_to_login(self, setup):
        self.url_browser(setup)
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.register_user(get_config("CRED", "name"), get_config("CRED", "email"),
                                            get_config("CRED", "password"))
        self.registrationPage.check_back_to_login()

    def test_verify_signup(self, setup):
        self.url_browser(setup)
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.register_user(get_config("DETAIL", "name"), get_config("DETAIL", "email"),
                                            get_config("DETAIL", "password"))
        self.registrationPage.check_signup()

    def test_invalid_email(self, setup):
        self.url_browser(setup)
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.register_user(get_config("CRED", "name"), get_config("CRED", "email"),
                                            get_config("CRED", "password"))
        self.registrationPage.check_invalid_email()
    # def test_verify_signup_email(self, setup):
    #   pass
