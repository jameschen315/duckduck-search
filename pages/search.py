from config.config import TestData
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DuckDuckGoSearchPage():
    """
    Initializes the Search object.

    Args:
    driver (WebDriver): The WebDriver instance.
    """
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, '#searchbox_input')
        self.search_button = (By.CSS_SELECTOR, '.searchbox_searchButton__F5Bwq')

    def click_search_input(self):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input))
        search_input.click()

    def enter_search_phase(self, search_phrase):
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_input))
        search_input.send_keys(search_phrase)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button))
        search_button.click()

    def search(self, search_phase):
        self.click_search_input()
        self.enter_search_phase(search_phase)
        self.click_search_button()

