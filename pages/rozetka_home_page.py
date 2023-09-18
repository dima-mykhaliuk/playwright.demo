import logging

from common.page import Page

import utils.logger_utils as lu
from locators.rozetka_home_page_locators import RozetkaHomePageLocators


class RozetkaHomePage(Page):
    log = lu.custom_logger(logging.DEBUG)

    def __init__(self, *args):
        super().__init__(*args)
        self.locators = RozetkaHomePageLocators

    def get_sale_goods_currency(self):
        prices = self.locate_elements(self.locators.SALE_GOODS_PRICE_CURRENCY.xpath)
        return self.get_elements_text(prices)

    def click_open_fat_menu(self):
        self.locate_click_element(self.locators.FAT_MENU_TOGGLE_BUTTON.xpath)

    def search_for(self, query):
        self.send_text_to_element(self.locators.SEARCH_INPUT.xpath, query)

    def do_all_visible_result_items_start_with(self, query) -> bool:
        search_items = self.locate_elements(self.locators.SEARCH_RESULTS_ITEMS_TEXT.xpath)
        search_items_text = self.get_elements_text(search_items)

        query = query.lower()

        for i in range(0, len(search_items_text), 2):
            if not search_items_text[i].lower().startswith(query):
                return False

        return True


