import random
import pandas as pd
import os
import time
import unittest
from glob import glob
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.common.BasePage import BasePage
from selenium.webdriver import ActionChains
from utilities.conftest import set_config, get_config


class LevelPage(BasePage):

    client_locators = {
        "clients_label": (By.XPATH, './/h3[text()= "Clients"]'),
        "add_partner_button": (By.XPATH, './/span[text()= "+ Partner"]'),
        "add_partner_label": (By.XPATH, './/h3[text()= "Add Partner"]'),
        "name_field": (By.XPATH, '(//div[@class="v-text-field__slot"]/input)[1]'),
        "name_partner": (By.XPATH, './/label[@class="v-label theme--light error--text"]'),
        "external_identifier_field": (By.XPATH, './/label[text()= "External Identifier"]'),
        "save_button": (By. XPATH, '(.//div[@class="d-flex justify-space-between my-3"])/button[2]'),
        "save": (By.XPATH, './/span[text()="Save"]'),
        "partner_success_message": (By.XPATH, './/div[@role="alert"]'),
        "add_client_button":(By.XPATH, './/span[text()="+ Client"]'),
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
        "select_site": (By.XPATH, ".//div [contains(text(), 'DUBAI-3')]"),
        "select_building": (By.XPATH, "(.//div[@class='v-list-item__content'])[1]"),
        "click_edit_level": (By.XPATH, "(.//span[@class='v-btn__content'])[3]"),
        "level_index": (By.XPATH, "(.//div[@class='v-text-field__slot'])[1]/input"),
        "level_long_name": (By.XPATH, "(.//div[@class='v-text-field__slot'])[2]/input"),
        "level_short_name": (By.XPATH, "(.//div[@class='v-text-field__slot'])[3]/input"),
        "level_identefier": (By.XPATH, "(.//div[@class='v-text-field__slot'])[4]/input"),
        "level_file": (By.XPATH, "(.//div[@class='v-text-field__slot'])[5]/input"),
        "save_level": (By.XPATH, ".//span[contains (text(),'Save')]"),
        "Download_CSV":(By.XPATH,".//span[contains(text(),'CSV')]")

    }

    def add_level(self):
        # select the client
        self.click_element(self.client_locators["select_client"])
        time.sleep(2)
        # select the site
        self.click_element(self.client_locators["select_site"])
        time.sleep(2)
        # select the Building
        self.click_element(self.client_locators["select_building"])
        time.sleep(2)
        # click Add button
        self.click_element(self.client_locators["add_button"])
        time.sleep(2)
        #  level index
        index = random.randint(-20, 79)
        self.click_element(self.client_locators["level_index"])
        self.send_text_to_element(self.find_element(self.client_locators["level_index"]), index)
        time.sleep(2)
        #  level long name
        self.click_element(self.client_locators["level_long_name"])
        self.send_text_to_element(self.find_element(self.client_locators["level_long_name"]), "ZAL")
        time.sleep(2)
        #  level short name
        self.click_element(self.client_locators["level_short_name"])
        self.send_text_to_element(self.find_element(self.client_locators["level_short_name"]), "zal")
        time.sleep(2)
        #  level identefier name
        self.click_element(self.client_locators["level_identefier"])
        self.send_text_to_element(self.find_element(self.client_locators["level_identefier"]), "123")
        time.sleep(2)

    def edit_level(self):
        # select the client
        self.click_element(self.client_locators["select_client"])
        time.sleep(2)
        # select the site
        self.click_element(self.client_locators["select_site"])
        time.sleep(2)
        # select the Building
        self.click_element(self.client_locators["select_building"])
        time.sleep(2)
        # click edit level
        self.click_element(self.client_locators["click_edit_level"])
        time.sleep(2)
        #  level index
        index= random.randint(-20, 79)
        self.click_element(self.client_locators["level_index"])
        self.send_text_to_element(self.find_element(self.client_locators["level_index"]), index)
        time.sleep(2)
        #  level long name
        self.click_element(self.client_locators["level_long_name"])
        self.send_text_to_element(self.find_element(self.client_locators["level_long_name"]), "edit")
        time.sleep(2)
        #  level short name
        self.click_element(self.client_locators["level_short_name"])
        self.send_text_to_element(self.find_element(self.client_locators["level_short_name"]), "EDIT")
        time.sleep(2)
        #  level identefier name
        identifier= random.randint(1,99)
        self.click_element(self.client_locators["level_identefier"])
        self.send_text_to_element(self.find_element(self.client_locators["level_identefier"]), identifier)
        time.sleep(2)
        # save level
        self.click_element(self.client_locators["save_level"])
        time.sleep(5)
        # check the success message
        self.wait_for_element_visible(self.client_locators["client_success_message"], 10)
        site_success_message = self.get_element_text(
            self.find_element(self.client_locators["client_success_message"]))
        assert site_success_message == "Level updated successfully!", "Issue in Level update!"

    def csv_file_columns(self):
        # select the client
        self.click_element(self.client_locators["select_client"])
        time.sleep(2)
        # select the site
        self.click_element(self.client_locators["select_site"])
        time.sleep(2)
        # select the Building
        self.click_element(self.client_locators["select_building"])
        time.sleep(2)
        # remove file from the downloads
        file_path = os.getcwd()+"/Downloads"
        file_list = os.listdir(file_path)
        for file in file_list:
            os.remove(file_path+"/"+file)
        # Download CSV
        self.click_element(self.client_locators["Download_CSV"])
        time.sleep(5)
        #Read downloaded CSV file
        file_list = os.listdir(file_path)
        data = pd.read_csv(file_path+"/"+file_list[0], index_col=False)
        column_names = list(data.columns)
        #Desire columns name of the CSV file
        Columns_Name_list = ["level", "uuid", "major", "minor", "color", "powerLevel", "interval", "rssi"]
        #Column length of the downloaded file
        length = len(column_names)
        #required length
        length1 = len(Columns_Name_list)
        if(length == length1):
            for i in range(0, length1):
                if Columns_Name_list[i] == column_names[i]:
                    assert True, "Columns name are match"
                else:
                    try:
                        assert False, "Colum name is not match"
                    except AssertionError as err:
                        print(err)
        else:
            assert False, " Number of columns are not match"