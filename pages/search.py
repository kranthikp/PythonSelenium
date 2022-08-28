"""
This module contains DuckDuckGoSearchPage,
The page object for the DuckDuckGo Search Page.
"""
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID,'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # TODO
        pass

    def search(self, phrase):
        # TODO
        pass
