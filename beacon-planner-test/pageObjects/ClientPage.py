import random
import time
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage
from utilities.conftest import set_config, get_config


class ClientPage(BasePage):
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
        "site_name": (By.XPATH, '(.//div[@class="v-text-field__slot"])[1]/input'),
        "add_button": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "select_client": (By.XPATH, '(.//div[@class="v-list-item__content"])[6]'),
        "select_polygon": (By.XPATH, '(.//span[@class="v-btn__content"])[2]'),
        "email_label": (By.ID, "input-32"),
        "password_label": (By.ID, "input-36"),
        "login_label": (By.XPATH, './/span[text()=" Login "]'),
        "login_button": (By.XPATH, './/button[@type = "submit"]'),
        "recording": (By.XPATH, ".//div[@id='data-recordings']"),
        "recording_page": (By.XPATH, ".//div[@class='v-toolbar__title']"),
        "table_row": (By.XPATH, ".//tbody/tr"),
        "table_cols": (By.XPATH, ".//tbody/tr[2]/td"),
        "val": (By.XPATH, ".//tbody/tr[6]/td[4]"),
        "partner_identifier": (By.XPATH, ".//label[ contains(text(),'External Identifier')]/following-sibling::input"),
        "click_partner": (By.XPATH, ".//div[@class='v-input__icon v-input__icon--append']"),
        "select_partner": (
        By.XPATH, ".//div[@class='v-list-item__title' and contains(text(),'Example Partner 101627740503676')]"),
        "client_identifier": (By.XPATH, ".//label[ contains(text(),'External Identifier')]/following-sibling::input"),
        "click_add_client": (By.XPATH, ".//span[ contains(text(),'+ Client')]"),
        "site_identifier": (By.XPATH, ".//label[ contains(text(),'External Identifier')]/following-sibling::input")
    }
    client_name = "Client validation failed: name: Error, expected `name` to be unique. Value: `Test Client`"
    client_created = './/div[text()="Client created successfully!'

    def check_add_partner(self, partner_name):
        # waiting for client page
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(1)
        # clicking on partner button
        self.click_element(self.client_locators["add_partner_button"])
        # check partner label
        self.is_element_displayed(self.client_locators["add_partner_label"])
        time.sleep(1)
        # entering a name
        self.send_text_to_element(self.find_element(self.client_locators["name_field"]),
                                  partner_name + str(round(time.time() * 1000)))
        # Enter the external identifier
        identifier = random.randint(1, 999)
        self.send_text_to_element(self.find_element(self.client_locators["partner_identifier"]), identifier)
        # click save button
        self.click_element(self.client_locators["save_button"])
        # check success message
        self.wait_for_element_visible(self.client_locators["partner_success_message"], 10)
        success_message_partner = self.get_element_text(
            self.find_element(self.client_locators["partner_success_message"]))
        print(success_message_partner)
        if success_message_partner == "Partner created successfully!":
            old_partner = get_config("FORM", "partner_name")
            print("old_partner: " + old_partner)
            partner = old_partner.split(" ")
            partner.pop(2)
            number = old_partner.split(" ")[2]
            inc = int(number)
            inc = inc + 1
            partner.append(str(inc))
            separator = " "
            new_partner = separator.join(partner)
            print("new_partner: " + new_partner)
            set_config("FORM", "partner_name", new_partner)
            assert True, "Partner created successfully!"
        else:
            try:
                assert False, "User is not navigated to partner page"
            except AssertionError as err:
                print(err)

    def check_add_client(self, client_name):
        # waiting for client page
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(1)
        # click add client
        self.click_element(self.client_locators["click_add_client"])
        # entering client a name
        self.send_text_to_element(self.find_element(self.client_locators["name_field"]),
                                  client_name + str(round(time.time() * 1000)))
        # client identifier
        identifier1 = random.randint(1, 999)
        self.send_text_to_element(self.find_element(self.client_locators["client_identifier"]), identifier1)
        # click save button
        self.click_element(self.client_locators["save_button"])
        # check success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        client_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(client_success_message)
        if client_success_message == "Client created successfully!":
            old_client = get_config("FORM", "client_name")
            print("old_client: " + old_client)
            client = old_client.split(" ")
            client.pop(2)
            number = old_client.split(" ")[2]
            inc = int(number)
            inc = inc + 1
            client.append(str(inc))
            separator = " "
            new_client = separator.join(client)
            print("new_client: " + new_client)
            set_config("FORM", "client_name", new_client)
            assert True, "Client created Successfully"
        else:
            try:
                assert False, "User is not navigated to client page"
            except AssertionError as err:
                print(err)

    def update_client_random_partner(self, client_name):
        # waiting for client page
        self.is_element_displayed(self.client_locators["clients_label"])
        time.sleep(1)
        # clicking on client button
        self.click_element(self.client_locators["add_client_button"])
        # check client label
        self.is_element_displayed(self.client_locators["add_client_label"])
        time.sleep(1)
        # click partner
        self.click_element(self.client_locators["click_partner"])
        partner_nav = self.find_elements(self.client_locators["partner_list"])
        partner_nav_total = len(partner_nav) + 1
        num = random.randint(1, partner_nav_total)
        partner = '(.//div[@class="v-list-item__title"])[' + str(num) + ']'
        # select a partner
        time.sleep(2)
        self.click_element((By.XPATH, partner))
        # entering a name
        self.send_text_to_element(self.find_element(self.client_locators["name_field"]),
                                  client_name + str(round(time.time() * 1000)))
        # client identifier
        identifier1 = random.randint(1, 999)
        self.send_text_to_element(self.find_element(self.client_locators["client_identifier"]), identifier1)
        # click save button
        self.click_element(self.client_locators["save_button"])
        # check success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        client_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        print(client_success_message)
        if client_success_message == "Client created successfully!":
            old_client = get_config("FORM", "client_name")
            print("old_client: " + old_client)
            client = old_client.split(" ")
            client.pop(2)
            number = old_client.split(" ")[2]
            inc = int(number)
            inc = inc + 1
            client.append(str(inc))
            separator = " "
            new_client = separator.join(client)
            print("new_client: " + new_client)
            set_config("FORM", "client_name", new_client)
            assert True, "Client created Successfully"
        else:
            try:
                assert False, "User is not navigated to client page"
            except AssertionError as err:
                print(err)

    def recording(self, dict):
        # cliking on the recording
        self.click_element(self.client_locators["recording"])
        time.sleep(3)
        recording_page = self.get_element_text(self.find_element(self.client_locators["recording_page"]))
        if recording_page == "Data Recordings ":
            assert True, "This is Data Recording Page"
        rows = len(self.find_elements(self.client_locators["table_row"]))
        cols = len(self.find_elements(self.client_locators["table_cols"]))
        value = self.get_element_text(self.find_element(self.client_locators["val"]))
        if isinstance(value, str):
            assert True, "This is less than 100"
        list = []
        # Get all the values of the colom contain number of beacons
        for r in range(2, rows + 1):
            val = self.get_element_text(self.find_element((By.XPATH, ".//tbody/tr[" + str(r) + "]/td[4]")))
            list.append(val)
        # Check the number is less then 100
        for i in range(len(list)):
            number = list[i]
            if (isinstance(number, str)):
                integer = int(number)
                if integer < 100:
                    element = self.get_element_text(
                        self.find_element((By.XPATH, ".//tbody/tr[" + str(i + 2) + "]/td[4]/div[1]/div[2]/img")))
                    if len(element) > 0:
                        assert True, "Warning icon is there"
                        print(integer, "icon is there in the", i + 1, "th row of beacon columns")
                else:
                    print(integer)
