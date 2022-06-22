import time
import allure
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage
class LoginPage(BasePage):
    login_locators = {
        "login_header_label": (By.XPATH, './/h1[text() = "Login"]'),
        "email_label": (By.ID, "input-32"),
        "password_label": (By.ID, "input-36"),
        "login_label": (By.XPATH, './/span[text()=" Login "]'),
        "login_button": (By.XPATH, './/button[@type = "submit"]'),
        "email_required": (By.XPATH, './/div[text() = "Email required"]'),
        "password_required": (By.XPATH, './/div[text() = "Password required"]'),
        "primary_nav": (By.XPATH, './/h3[text() = "Clients"]'),
        "error_alert": (By.XPATH, './/p[text() = "Please check your email or password and try again"]'),
        "signup": (By.XPATH, './/span[text()= "Don’t have an account?"]'),
        "forgot_password": (By.XPATH, './/span[text()= "Forgot password?"]'),
        "reset_page": (By.XPATH, './/h1[text()="Reset"]'),
        "new_account_page": (By.XPATH, './/h1[text()="New Account"]'),
        "email_placeholder": (By.XPATH, "//div[@class='v-text-field__slot']/label[text() = 'Email']"),
        "password_placeholder": (By.XPATH, "//div[@class='v-text-field__slot']/label[text() = 'Password']")
    }
    def check_login_header_label(self):
        title = self.driver.title
        if title == "beacon-planner":
            self.is_element_displayed(self.login_locators["login_header_label"])
            self.is_element_displayed(self.login_locators["email_label"])
            self.is_element_displayed(self.login_locators["password_label"])
            self.is_element_displayed(self.login_locators["login_label"])
            time.sleep(2)
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_verify_login_header_label.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                          attachment_type=allure.attachment_type.PNG)
            assert False, "The user is not able to find label ."

    def check_login_mandatory_fields(self):
        title = self.driver.title
        if title == "beacon-planner":
            self.click_element(self.login_locators["login_button"])
            self.is_element_displayed((self.login_locators["email_required"]))
            self.is_element_displayed(self.login_locators["password_required"])
            time.sleep(2)
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_verify_mandatory_fields.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                          attachment_type=allure.attachment_type.PNG)
            assert False, "The user is not able to verify mandatory field."

    def check_login(self, email, password, test):
        self.send_text_to_element(self.find_element(self.login_locators["email_label"]), email)
        self.send_text_to_element(self.find_element(self.login_locators["password_label"]), password)
        self.click_element(self.login_locators["login_button"])
        time.sleep(5)
        if test == "valid":
            title = self.driver.title
            if title == "beacon-planner":
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshot\\" + "test_valid_email_valid_password.png")
                allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                              attachment_type=allure.attachment_type.PNG)
                assert False, "The user is not navigated to homepage."
        else:
            print(self.get_element_text(self.find_element(self.login_locators["error_alert"])))
            if self.find_element(self.login_locators["error_alert"]):
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshot\\" + "test_valid_email_valid_password.png")
                allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                              attachment_type=allure.attachment_type.PNG)
                assert False, "The Error message for invalid username or password not appear."

    def check_signup_link(self):
        self.click_element(self.login_locators["signup"])
        signup = self.get_element_text(self.find_element(self.login_locators["new_account_page"]))
        if signup == "New Account":
            assert True
            time.sleep(3)
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_forgot_password_link.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                          attachment_type=allure.attachment_type.PNG)
            assert False, "The User is not navigated to signup page."

    def check_forgot_password_link(self):
        self.click_element(self.login_locators["forgot_password"])
        forgot_password = self.get_element_text(self.find_element(self.login_locators["reset_page"]))
        if forgot_password == "Reset":
            assert True
            time.sleep(3)
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_forgot_password_link.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                          attachment_type=allure.attachment_type.PNG)
            assert False, "The User is not navigated to forgot password page."

    # test the placeholder
    def check_placeholder(self, dict):
        email_placeholder = self.get_element_text(self.find_element(self.login_locators["email_placeholder"]))
        password_placeholder =self.get_element_text(self.find_element(self.login_locators["password_placeholder"]))
        assert email_placeholder == dict["email_placeholder"] and password_placeholder == dict["password_placeholder"]