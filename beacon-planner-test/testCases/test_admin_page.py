from pageObjects.AdminPage import AdminPage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Admin_Page:
    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_go_to_admin_page(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.adminPage = AdminPage(self.driver)
        adminURL = get_config("URL", "admin")
        self.driver.get(adminURL)
        self.adminPage.check_admin_page()
