import random
import time
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage
from selenium.webdriver import ActionChains


class BeaconPage(BasePage):
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

    client_locators = {
        "clients_label": (By.XPATH, './/h3[text()= "Clients"]'),
        "add_partner_button": (By.XPATH, './/span[text()= "+ Partner"]'),
        "add_partner_label": (By.XPATH, './/h3[text()= "Add Partner"]'),
        "name_field": (By.XPATH, '(//div[@class="v-text-field__slot"]/input)[1]'),
        "name_partner": (By.XPATH, './/label[@class="v-label theme--light error--text"]'),
        "external_identifier_field": (By.XPATH, './/label[text()= "External Identifier"]'),
        "save_button": (By.XPATH, '(.//div[@class="d-flex justify-space-between my-3"])/button[2]'),
        "save": (By.XPATH, './/span[text()="Save"]'),
        "partner_success_message": (By.XPATH, './/div[@role="alert"]'),
        "add_client_button": (By.XPATH, './/span[text()="+ Client"]'),
        "add_client_label": (By.XPATH, './/h3[text()="Add Client"]'),
        "client_name_field": (By.XPATH, './/label[text()="Name"]'),
        "client_success_message": (By.XPATH, './/div[@role="alert"]'),
        "partner_list": (By.XPATH, '(.//div[@class="v-list-item__title"])'),
        "select_partner": (By.XPATH, './/div[@class="v-select__selections"] '),
        "search_placeholder": (By.XPATH, './/input[@placeholder = "Search"]'),
        "canvas": (By.XPATH, './/canvas[@class="mapboxgl-canvas"]'),
        "site_name": (By.XPATH, '(.//div[@class="v-text-field__slot"])[1]'),
        "add_button": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "select_client": (By.XPATH, '(.//div[@class="v-list-item__content"])[6]'),
        "select_polygon": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "add_becon": (By.XPATH, "(//div[@class='beacon-types'])[1]"),
        "click_client": (By.XPATH, ".//div [contains(text(), 'DA')]"),
        "click_site": (By.XPATH, ".//div [contains(text(), 'Dubai Airport')]"),
        "click_building": (By.XPATH, ".//div [contains(text(), 'Dubai Aiport T1')]"),
        "click_level": (By.XPATH, ".//div [contains(text(), '3 - t1-u')]"),
        "click_beacon": (By.XPATH, ".//span [contains(text(), 'RedBeacon')]"),
        "edit_beacon": (By.XPATH, ".//span [contains(text(), 'Edit Beacon Type')]"),
        "beacon_color": (By.XPATH, ".//div[@class='v-select__selections'][1]"),
        "add_beacon_color": (By.XPATH, ".//div[contains(text(), 'Gray')]"),
        "beacon_nickname": (By.XPATH, ".//div[@class='v-text-field__slot']"),
        "clear_all": (By.XPATH, ".//span [contains(text(), 'Clear all')]"),
        "confirm": (By.XPATH, ".//span [contains(text(), 'Confirm')]"),
        "beacon_2click": (By.XPATH, ".//div[@minor='03003']"),
        "log": (By.XPATH, ".//input[@role='switch']"),
        "delet": (By.XPATH, ".//span[contains(text(),'Delete')]"),
        "back": (By.XPATH, ".//div[@id='caret-left']"),
        "add_new_beacon_type": (By.XPATH, ".//span[contains(text(), '+')]"),
        "click_color": (By.XPATH, "(.//div[@class='v-input__append-inner'])[1]"),
        "get_color": (By.XPATH, ".//div[contains ( text(), 'Gray')]"),
        "nikname": (By.XPATH, ".//label[contains (text(),'Nickname')]/following-sibling::input"),
        "click_beacontype": (By.XPATH, "(.//div[@class='v-input__append-inner'])[2]"),
        "get_beacontype": (By.XPATH, ".//div[contains ( text(), 'USB beacon')]"),
        "click_attachment": (By.XPATH, "(.//div[@class='v-input__append-inner'])[3]"),
        "get_attachment": (By.XPATH, ".//div[contains ( text(), 'Magnet 2')]"),
        "click_mounting": (By.XPATH, "(.//div[@class='v-input__append-inner'])[4]"),
        "get_mounting": (By.XPATH, ".//div[contains ( text(), 'Side wall')]"),
        "click_make": (By.XPATH, "(.//div[@class='v-input__append-inner'])[5]"),
        "get_make": (By.XPATH, ".//div[contains ( text(), 'Confidex')]"),
        "click_model": (By.XPATH, "(.//div[@class='v-input__append-inner'])[6]"),
        "get_model": (By.XPATH, ".//div[contains ( text(), 'Viking')]"),
        "click_power": (By.XPATH, "(.//div[@class='v-input__append-inner'])[7]"),
        "get_power": (By.XPATH, ".//div[contains ( text(), '4 (-8 dBm)')]"),
        "positive_interval": (By.XPATH, ".//label[contains (text(),'Interval')]/following-sibling::input"),
        "negative_interval": (By.XPATH, ".//label[contains (text(),'rssi at 1 meter')]/following-sibling::input"),
        "save": (By.XPATH, ".//span[contains(text(),'Save')]"),

    }

    def add_beacon(self):
        # click client
        self.click_element(self.client_locators["click_client"])
        # client clicking
        self.click_element(self.client_locators["click_site"])
        # click building
        self.click_element(self.client_locators["click_building"])
        # click level
        self.click_element(self.client_locators["click_level"])
        # clear all
        self.click_element(self.client_locators["clear_all"])
        # confirm clear all
        self.click_element(self.client_locators["confirm"])
        # click the beacon
        self.click_element(self.client_locators["click_beacon"])
        # placing the beacons
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2 + 5),
                                                  int(int(canvas.size["height"]) / 2)).click().perform()
        time.sleep(2)
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        assert site_success_message == "Saved", "Issue in placing Beacon"
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2),
                                                  int(int(canvas.size["height"]) / 2 - 100)).click().perform()
        time.sleep(2)
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(site_success_message)
        assert site_success_message == "Saved", "Issue in placing Beacon"
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2 + 50),
                                                  int(int(canvas.size["height"]) / 2 - 100)).click().perform()
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(site_success_message)
        assert site_success_message == "Saved", "Issue in placing Beacon"
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2),
                                                  int(int(canvas.size["height"]) / 2 - 50)).click().perform()
        time.sleep(2)

    def add_new_beacontype(self):
        # click client
        self.click_element(self.client_locators["click_client"])
        # client clicking
        self.click_element(self.client_locators["click_site"])
        # click building
        self.click_element(self.client_locators["click_building"])
        # click level
        self.click_element(self.client_locators["click_level"])
        # Add beacon type
        time.sleep(10)
        self.click_element(self.client_locators["add_new_beacon_type"])
        # click color
        self.click_element(self.client_locators["click_color"])
        # get color
        self.click_element(self.client_locators["get_color"])
        # set nikname of beacon
        self.send_text_to_element(self.find_element(self.client_locators["nikname"]), "ZAB")
        # click beacon type
        self.click_element(self.client_locators["click_beacontype"])
        # get beacon type
        self.click_element(self.client_locators["get_beacontype"])
        # click attachment
        self.click_element(self.client_locators["click_attachment"])
        # get attachment
        self.click_element(self.client_locators["get_attachment"])
        # click mounting
        self.click_element(self.client_locators["click_mounting"])
        # get mounting
        self.click_element(self.client_locators["get_mounting"])
        # click make
        self.click_element(self.client_locators["click_make"])
        # get make
        self.click_element(self.client_locators["get_make"])
        # click model
        self.click_element(self.client_locators["click_model"])
        # get model
        self.click_element(self.client_locators["get_model"])
        # click power
        self.click_element(self.client_locators["click_power"])
        # get power
        self.click_element(self.client_locators["get_power"])
        # set +interval of beacon
        positive_interval = random.randint(51, 4999)
        self.send_text_to_element(self.find_element(self.client_locators["nikname"]), positive_interval)
        # set -interval of beacon
        negative_interval = random.randint(-127, -1)
        self.send_text_to_element(self.find_element(self.client_locators["nikname"]), negative_interval)
        # click save
        self.click_element(self.client_locators["save"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        assert site_success_message == "Beacon type created successfully!", "Beacon type is not created"

    def delet_beacon(self):
        # click client
        self.click_element(self.client_locators["click_client"])
        # client clicking
        self.click_element(self.client_locators["click_site"])
        # click building
        self.click_element(self.client_locators["click_building"])
        # click level
        self.click_element(self.client_locators["click_level"])
        # move
        time.sleep(10)
        self.click_element(self.client_locators["back"])
        # click level
        self.click_element(self.client_locators["click_level"])
        # log click
        self.click_element(self.client_locators["log"])
        # beacon 2click
        source = self.find_element(self.client_locators["beacon_2click"])
        action_chains = ActionChains(self.driver)
        action_chains.double_click(source).perform()
        # delet beacon
        self.click_element(self.client_locators["delet"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        assert site_success_message == "Beacon removed successfully!", "Beacon is not removed"
