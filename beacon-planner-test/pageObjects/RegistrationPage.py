import time
import allure
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage
class RegistrationPage(BasePage):

    register_locator = {

        "name_label": (By.XPATH, './/label[text()="Name"]'),
        "email_label": (By.XPATH, './/label[text()="Email"]'),
        "password_label": (By.XPATH, './/label[text()="Password"]'),
        "name_field": (By.ID, "input-54"),
        "email_field": (By.ID, "input-58"),
        "password_field": (By.ID, "input-62"),
        "signup_button": (By.XPATH, '. // button[ @ type = "submit"]'),
        "signup_page": (By.XPATH, './/span[text()= "Don’t have an account?"]'),
        "new_account_page": (By.XPATH, './/h1[@class = "login-form-title"]'),
        "name_required": (By.XPATH, './/div[text()="Name is required"]'),
        "email_required": (By.XPATH, './/div[text()="Email is required"]'),
        "password_required": (By.XPATH, './/div[text()="Password is required"]'),
        "duplicate_email_message": (By.CLASS_NAME, 'explanation'),
        "back_to_login": (By.XPATH, './/button[@type="button"]'),
        "login_header_label": (By.XPATH, './/h1[text() = "Login"]'),
        "try_again_button": (By.XPATH, './/button[@type="button"]'),
        "signup_message": (By.XPATH, './/p[@class="explanation"]'),
    }
    def check_all_valid_fields(self):
        self.click_element(self.register_locator["signup_page"])
        self.is_element_displayed(self.register_locator["new_account_page"])
        signup_title = self.get_element_text(self.find_element(self.register_locator["new_account_page"]))
        if signup_title == "New Account":
            self.click_element(self.register_locator["name_field"])
            self.click_element(self.register_locator["email_field"])
            self.click_element(self.register_locator["password_field"])
            self.click_element(self.register_locator["email_field"])
            name_required = self.get_element_text(self.find_element(self.register_locator["name_required"]))
            email_required = self.get_element_text(self.find_element(self.register_locator["email_required"]))
            password_required = self.get_element_text(self.find_element(self.register_locator["password_required"]))
            if name_required == "Name is required" and email_required == "Email is required" and password_required == "Password is required":
                assert True, "All require valid fields"
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_verify_all_valid_fields.png")
            allure.attach(self.driver.get_screenshot_as_png(), name=type(self).__name__,
                          attachment_type=allure.attachment_type.PNG)
            assert False, "There are no valid fields"
        time.sleep(2)
    def register_user(self, name, email, password):
        self.click_element(self.register_locator["signup_page"])
        self.send_text_to_element(self.find_element(self.register_locator["name_field"]), name)
        self.send_text_to_element(self.find_element(self.register_locator["email_field"]), email)
        self.send_text_to_element(self.find_element(self.register_locator["password_field"]), password)
        self.click_element(self.register_locator["signup_button"])
        time.sleep(3)
    def check_duplicate_email(self, name, email, password):
        self.click_element(self.register_locator["signup_page"])
        self.is_element_displayed(self.register_locator["new_account_page"])
        signup_title = self.get_element_text(self.find_element(self.register_locator["new_account_page"]))
        if signup_title == "New Account":
            self.send_text_to_element(self.find_element(self.register_locator["name_field"]), name)
            self.send_text_to_element(self.find_element(self.register_locator["email_field"]), email)
            self.send_text_to_element(self.find_element(self.register_locator["password_field"]), password)
            self.click_element(self.register_locator["signup_button"])
            time.sleep(3)
            duplicate_email = self.get_element_text(self.find_element(self.register_locator["duplicate_email_message"]))
            if duplicate_email == "Failed to create user":
                assert True, "Email already Exist"
            else:
                assert False
        else:
            try:
                assert False, "The user is not navigated to Sign Up page"
            except AssertionError as err:
                print(err)
    def check_back_to_login(self):
        self.click_element(self.register_locator["try_again_button"])
        self.click_element(self.register_locator["back_to_login"])
        time.sleep(2)
        login_label = self.get_element_text(self.find_element(self.register_locator["login_header_label"]))
        if login_label == "Login":
            assert True, "The user is able to log in to Beacons Planner"
        else:
            try:
                assert False, "The user is not able navigated to Login Page"
            except AssertionError as err:
                print(err)
    def check_signup(self):
        signup = self.get_element_text(self.find_element(self.register_locator["signup_message"]))
        if signup == "You will get an email once your account is approved.":
            assert True, "Signup Completed"
        else:
            try:
                assert False, "The user is not able to sign up"
            except AssertionError as err:
                print(err)
    def check_invalid_email(self):
        invalid = self.get_element_text(self.find_element(self.register_locator["duplicate_email_message"]))
        if invalid == "Failed to create user":
            assert True, "Email is not valid"
        else:
            try:
                assert False, "The user is not navigated to Sign up page"
            except AssertionError as err:
                print(err)
    def check_signup_email(self, setup):
        pass



