"""
This module contains DuckDuckGoResultPage,
The page object for the DuckDuckGo Result Page.
"""
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def search_link_titles(self):
        # TODO
        return []

    def search_input_values(self):
        # TODO
        return ""

    def title(self):
        # TODO
        return ""