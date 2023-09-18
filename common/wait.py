import logging

from playwright.sync_api import ElementHandle, Page, Locator
from utils.logger_utils import custom_logger

logger = custom_logger(logging.DEBUG)


class Wait:
    def __init__(self, page: Page):
        self.page = page
        self.log = logger

    def wait_for_selector_to_appear(self, selector: str):
        self.page.wait_for_selector(selector)
        self.log.info(f"Selector '{selector}' has appeared")

    def wait_for_selector_to_disappear(self, selector: str):
        self.page.wait_for_selector(selector, state='hidden')
        self.log.info(f"Selector '{selector}' has disappeared")

    def wait_for_function_to_return_true(self, js_function: str):
        self.page.wait_for_function(js_function)
        self.log.info(f"Function '{js_function}' has returned true")

    def wait_for_element_to_be_hidden(self, locator: Locator):
        locator.wait_for(state='hidden')
        self.log.info(f"Element {locator} is hidden")

    def wait_for_element_to_be_attached(self, locator: Locator):
        locator.wait_for(state='attached')
        self.log.info(f"Element {locator} is enabled")

    def wait_for_element_to_be_detached(self, locator: Locator):
        locator.wait_for(state='detached')
        self.log.info(f"Element {locator} is disabled")

    def wait_for_element_to_be_visible(self, locator: Locator):
        try:
            locator.wait_for(state='visible')
            self.log.info(f"Element {locator} is visible")
            return True
        except Exception as e:
            self.log.error(f"Error checking if element {locator} is visible. Error: {str(e)}")
            return False
