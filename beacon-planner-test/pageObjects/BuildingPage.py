import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sys import platform
from pageObjects.common.BasePage import BasePage
from selenium.webdriver import ActionChains


class BuildingPage(BasePage):
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
        "select_client": (By.XPATH, './/div [contains(text(), "DA")]'),
        "select_polygon": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "select_building": (By.XPATH, "(.//div[@class='v-list-item__content'])[1]"),
        "click_edit_building": (By.XPATH, "(.//span[@class='v-btn__content'])[3]"),
        "building_new_name": (By.XPATH, "(.//div[@class='v-text-field__slot'])/input"),
        "save1": (By.XPATH, "(.//span[@class='v-btn__content'])[3]"),
        "select_site": (By.XPATH, ".//div [contains(text(), 'Dubai Airport')]"),
        "building_name": (By.XPATH, "(.//div[@class='v-text-field__slot'])[1]/input"),
        "building_index": (By.XPATH, "(.//div[@class='v-text-field__slot'])[2]/input"),
        "building_identifier": (By.XPATH, "(.//div[@class='v-text-field__slot'])[3]/input"),
        "save_Building_button": (By.XPATH, ".//span[contains(text(),'Save')]"),

    }

    def add_building(self):
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(5)
        # select the client
        self.click_element(self.client_locators["select_client"])
        time.sleep(2)
        # select the site
        self.click_element(self.client_locators["select_site"])
        time.sleep(2)
        # click on the add building
        self.click_element(self.client_locators["add_button"])
        time.sleep(2)
        # add the name of the Building
        self.click_element(self.client_locators["building_name"])
        building_name = "ZAB" + str(round(time.time() * 1000))
        self.send_text_to_element(self.find_element(self.client_locators["building_name"]), building_name)
        # add building index
        indx = random.randint(1, 999)
        self.click_element(self.client_locators["building_index"])
        self.send_text_to_element(self.find_element(self.client_locators["building_index"]), indx)
        identifier = random.randint(1, 999)
        # add building identifer
        self.click_element(self.client_locators["building_identifier"])
        self.send_text_to_element(self.find_element(self.client_locators["building_identifier"]), identifier)
        # using polygon
        self.click_element(self.client_locators["select_polygon"])
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2),
                                                  int(int(canvas.size["height"]) / 2)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2) + 100,
                                                  int(int(canvas.size["height"]) / 2)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2) + 100,
                                                  int(int(canvas.size["height"]) / 2 - 100)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2),
                                                  int(int(canvas.size["height"]) / 2) - 100).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / 2),
                                                  int(int(canvas.size["height"]) / 2) - 100).click().perform()
        time.sleep(2)
        # click save button
        self.click_element(self.client_locators["save_Building_button"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(site_success_message)
        if site_success_message == "Building created successfully!":
            assert True, "Building created successfully!"
        else:
            try:
                assert False, "User is not able to navigated to Building Page"
            except AssertionError as err:
                print(err)

    def edit_building(self):
        # waiting for client page
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(5)
        # select the client
        self.click_element(self.client_locators["select_client"])
        time.sleep(2)
        # select the site
        self.click_element(self.client_locators["select_site"])
        time.sleep(2)
        # click on edit building
        self.click_element(self.client_locators["click_edit_building"])
        time.sleep(5)
        # adding new name of the site
        element = self.find_element(self.client_locators["building_new_name"])
        if platform == "win32" or platform == "win64":
            element.send_keys(Keys.CONTROL, 'a')
        elif platform == "linux" or platform == "linux2":
            element.send_keys(Keys.COMMAND, 'a')
        elif platform == "darwin":
            element.send_keys(Keys.COMMAND, 'a')
        self.send_text_to_element(self.find_element(self.client_locators["building_new_name"]), "Edit")
        # click save button
        self.click_element(self.client_locators["save1"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        assert site_success_message == "Building updated successfully!", "Building updated successfully!"