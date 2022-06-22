from pageObjects.SitePage import SitePage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Site_Page:
    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_add_site(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.sitePage = SitePage(self.driver)
        self.sitePage.add_site()

    def test_verify_edit_site(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.sitePage = SitePage(self.driver)
        self.sitePage.edit_site()
