from pageObjects.BeaconPage import BeaconPage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Beacon_Page:

    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    def test_verify_add_beacon(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.beaconPage = BeaconPage(self.driver)
        self.beaconPage.add_beacon()

    def test_verify_add_beacon_type(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.beaconPage = BeaconPage(self.driver)
        self.beaconPage.add_new_beacontype()

    def test_verify_delet_beacon(self, setup):
        self.url_browser(setup)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
        self.beaconPage = BeaconPage(self.driver)
        self.beaconPage.delet_beacon()
