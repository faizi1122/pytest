from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage


class AdminPage(BasePage):
    admin_locators = {
        "admin_page_label": (By.XPATH, './/div[text()=" Admin Page "]'),
    }

    def check_admin_page(self):
        self.is_element_displayed(self.find_element(self.admin_locators["admin_page_label"]))
        admin = self.get_element_text(self.find_element(self.admin_locators["admin_page_label"]))
        if admin == "Admin Page":
            assert True, "The user is navigated to Admin Page"
        else:
            assert False, "The user is not navigated to Admin Page"

    def check_role(self):
        pass
