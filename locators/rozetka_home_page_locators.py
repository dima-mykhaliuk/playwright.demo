from enum import Enum


class RozetkaHomePageLocators(Enum):

    @property
    def css(self):
        return self.value['css']

    @property
    def xpath(self):
        return self.value['xpath']

    SALE_GOODS_PRICE_CURRENCY = {
        'css': '',
        'xpath': "//h2[contains(.,' Акційні пропозиції ')]/following-sibling::ul/li//span["
                 "@class='tile__price-currency currency']"
    }
    FAT_MENU_TOGGLE_BUTTON = {
        'css': '',
        'xpath': "(//button[contains(.,' Каталог ')])[1]"
    }
    FAT_MENU_CONTENT_SECTION = {
        'css': '',
        'xpath': "(//div[@class='menu__hidden-content ng-star-inserted'])[1]"
    }
    SEARCH_INPUT = {
        'css': '',
        'xpath': "//input[@name='search']"
    }
    SEARCH_RESULTS_POPUP = {
        'css': '',
        'xpath': "//div[@class='search-suggest ng-star-inserted']"
    }

    SEARCH_RESULTS_ITEMS_TEXT = {
        'css': '',
        'xpath': "//a[@class='search-suggest__item-content search-suggest__item-text']/span/span"
    }
