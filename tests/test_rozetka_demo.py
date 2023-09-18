import pytest

from common.test import Test
from pages.rozetka_home_page import RozetkaHomePage


@pytest.mark.usefixtures("class_setup")
@pytest.mark.test_data("00001")
class TestRozetkaDemo(Test):
    @pytest.fixture(autouse=True)
    def classSetup(self, class_setup):
        self.browser = class_setup["browser"]
        self.base_route = class_setup["base_route"]
        self.home_page = RozetkaHomePage(self.browser, self.base_route)
        yield

    @pytest.mark.parametrize("currency_symbol", ["₴", "\u20b4"])
    def test_sale_goods_currency(self, currency_symbol):
        self.home_page.navigate_to_base_route()
        symbols = self.home_page.get_sale_goods_currency()
        self.assert_all_elements_equal(symbols, currency_symbol)

    def test_fat_menu_positive(self):
        self.home_page.navigate_to_base_route()
        self.home_page.click_open_fat_menu()
        self.assert_true(
            self.home_page.element_to_be_visible(
                self.home_page.locate_element(
                    self.home_page.locators.FAT_MENU_CONTENT_SECTION.xpath)))

    def test_fat_menu_negative(self):
        self.home_page.navigate_to_base_route()
        self.assert_true(
            self.home_page.element_to_be_hidden(
                self.home_page.locate_element(
                    self.home_page.locators.FAT_MENU_CONTENT_SECTION.xpath)))

    @pytest.mark.parametrize("search_keyword", ["Samsu", "Leno"])
    def test_search(self, search_keyword):
        self.home_page.navigate_to_base_route()
        self.home_page.search_for(search_keyword)
        self.assert_true(
            self.home_page.element_to_be_visible(
                self.home_page.locate_element(
                    self.home_page.locators.SEARCH_RESULTS_POPUP.xpath)))
        self.assert_true(self.home_page.do_all_visible_result_items_start_with(search_keyword))
