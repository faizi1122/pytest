from pageObjects.LevelPage import LevelPage
from pageObjects.LoginPage import LoginPage
from utilities.conftest import *


class Test_Level_Page:

    def url_browser(self, setup):
        self.driver = setup
        baseURL = get_config("URL", "url")
        self.driver.get(baseURL)

    # def test_level_csv_file_columns(self, setup):
    #     self.url_browser(setup)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
    #     self.levelPage = LevelPage(self.driver)
    #     self.levelPage.csv_file_columns()
    #
    # def test_verify_add_level(self, setup):
    #     self.url_browser(setup)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
    #     self.levelPage = LevelPage(self.driver)
    #     self.levelPage.add_level()
    #
    # def test_verify_edit_level(self, setup):
    #     self.url_browser(setup)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.check_login(get_config("CRED", "email"), get_config("CRED", "password"), "valid")
    #     self.levelPage = LevelPage(self.driver)
    #     self.levelPage.edit_level()
