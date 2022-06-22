import random
import time, string
import allure
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sys import platform
from pageObjects.common.BasePage import BasePage
from selenium.webdriver import ActionChains


class SitePage(BasePage):
    client_locators = {
        "clients_label": (By.XPATH, './/h3[text()= "Clients"]'),
        "add_partner_button": (By.XPATH, './/span[text()= "+ Partner"]'),
        "add_partner_label": (By.XPATH, './/h3[text()= "Add Partner"]'),
        "name_field": (By.XPATH, '(//div[@class="v-text-field__slot"]/input)[1]'),
        "name_partner": (By.XPATH, './/label[@class="v-label theme--light error--text"]'),
        "external_identifier_field": (By.XPATH, './/label[text()= "External Identifier"]'),
        "save_button": (By.XPATH, ".//span[contains(text(),'Save')]"),
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
        "edit_site_identifier": (By.XPATH, "((.//div[@class='v-text-field__slot'])/input)[1]"),
        "add_button": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "select_client": (By.XPATH, './/div [contains(text(), "DA")]'),
        "select_polygon": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "edit_site": (By.XPATH, "(.//div[@class='v-list-item__action'])[1]/button"),
        "site_identifier": (By.XPATH, ".//label[ contains(text(),'External Identifier')]/following-sibling::input"),
        "client_list": (By.XPATH, './/div[@class="v-list-item__content"]'),
        "site_name": (By.XPATH, '(.//div[@class="v-text-field__slot"]/input)[1]'),
        "edit_site_name": (By.XPATH, "((.//div[@class='v-text-field__slot'])/input)[1]"),
        "edit_site_identifier": (By.XPATH, "((.//div[@class='v-text-field__slot'])/input)[2]"),
        "clear_site_rectangle": (By.XPATH, ".//span[contains(text(),' Clear Rectangle ')]"),
        "save_site": (By.XPATH, ".//span[contains(text(),'Save')]"),
    }

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def add_site(self):
        # waiting for the client page
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(5)
        # select the client
        Client_nav = self.find_elements(self.client_locators["client_list"])
        Client_nav_total = len(Client_nav) + 1
        num = random.randint(1, Client_nav_total)
        Client = '(.//div[@class="v-list-item__content"])[' + str(num) + ']'
        self.click_element((By.XPATH, Client))
        # time.sleep(2)
        # click on the add site
        self.click_element(self.client_locators["add_button"])
        time.sleep(2)
        # add the name of the site
        self.send_text_to_element(self.find_element(self.client_locators["site_name"]),
                                  "Example Site 6" + str(round(time.time() * 1000)))
        time.sleep(2)
        # add external identifier
        identifier = random.randint(0, 999)
        self.send_text_to_element(self.find_element(self.client_locators["site_identifier"]), identifier)
        # using polygon
        self.click_element(self.client_locators["select_polygon"])
        time.sleep(1)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        number = random.uniform(2.0, 2.9)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number) + 100,
                                                  int(int(canvas.size["height"]) / number)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number) + 100,
                                                  int(int(canvas.size["height"]) / number - 100)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number) - 100).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number) - 100).click().perform()
        time.sleep(2)
        # click save button
        self.click_element(self.client_locators["save_button"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))

        assert site_success_message == "Site created successfully!", "Site creation failed!"

    def edit_site(self):
        # waiting for client page
        self.is_element_displayed(self.client_locators["clients_label"])
        # select the client
        self.click_element(self.client_locators["select_client"])
        # click on edit button
        self.click_element(self.client_locators["edit_site"])
        element = self.find_element(self.client_locators["edit_site_name"])
        if platform == "win32" or platform == "win64":
            element.send_keys(Keys.CONTROL, 'a')
        elif platform == "linux" or platform == "linux2":
            element.send_keys(Keys.COMMAND, 'a')
        elif platform == "darwin":
            element.send_keys(Keys.COMMAND, 'a')
        self.send_text_to_element(self.find_element(self.client_locators["edit_site_name"]),
                                  "Airport"+self.id_generator())
        # adding new identifier of the site
        self.click_element(self.client_locators["edit_site_identifier"])
        element = self.find_element(self.client_locators["edit_site_identifier"])
        if platform == "win32" or platform == "win64":
            element.send_keys(Keys.CONTROL, 'a')
        elif platform == "linux" or platform == "linux2":
            element.send_keys(Keys.COMMAND, 'a')
        elif platform == "darwin":
            element.send_keys(Keys.COMMAND, 'a')
        self.send_text_to_element(self.find_element(self.client_locators["edit_site_identifier"]),
                                  "Airport"+self.id_generator())
        # clear rectangle
        self.click_element(self.client_locators["clear_site_rectangle"])
        time.sleep(4)
        # select polygon
        self.click_element(self.client_locators["select_polygon"])
        # draw new rectangle
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        number = random.uniform(2.0, 2.9)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number) + 100,
                                                  int(int(canvas.size["height"]) / number)).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number) + 100,
                                                  int(int(canvas.size["height"]) / number) - 100).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number) - 100).click().perform()
        time.sleep(2)
        canvas = self.find_element(self.client_locators["canvas"])
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element_with_offset(canvas, int(int(canvas.size["width"]) / number),
                                                  int(int(canvas.size["height"]) / number) - 100).click().perform()
        time.sleep(2)
        # click save button
        self.click_element(self.client_locators["save_site"])
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(site_success_message)
        assert site_success_message == "Site updated successfully!", "Issue in updating the site"