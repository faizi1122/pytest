from pageObjects.ClientPage import ClientPage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Client_Page:

    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_add_partner(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.clientPage = ClientPage(self.driver)
        self.clientPage.check_add_partner(get_config("FORM", "partner_name"))

    def test_verify_add_client_without_partner(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.clientPage = ClientPage(self.driver)
        self.clientPage.check_add_client(get_config("FORM", "client_name"))

    def test_verify_add_client_with_partner(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.clientPage = ClientPage(self.driver)
        self.clientPage.update_client_random_partner(get_config("FORM", "client_name"))

    def test_recording(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.clientPage = ClientPage(self.driver)
        self.clientPage.recording(dict)
