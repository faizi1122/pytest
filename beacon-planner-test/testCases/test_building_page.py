from pageObjects.BuildingPage import BuildingPage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Site_Page:

    building_name = None

    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_add_building(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.BuildingPage = BuildingPage(self.driver)
        self.building_name = self.BuildingPage.add_building()

    def test_verify_edit_building(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.buildingPage = BuildingPage(self.driver)
        self.buildingPage.edit_building()
