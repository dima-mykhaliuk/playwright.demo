import logging
import utils.logger_utils as lu
from playwright.sync_api import ElementHandle, Locator

from common.ABC import ABC
from common.wait import Wait


class Page(ABC):
    log = lu.custom_logger(logging.DEBUG)

    def __init__(self, browser, base_route):
        self.browser = browser
        self.base_route = base_route
        self.page = self.browser.new_page()
        self.wait = Wait(self.page)

    def _log_and_ss(self, error_message):
        self.log.error(error_message)
        self.take_screenshot(self.page, error_message)

    def locate_element(self, selector) -> Locator:
        try:
            element = self.page.locator(selector)
            self.log.info(f"Located element using selector: {selector}")
            return element
        except Exception as e:
            self._log_and_ss(f"Error locating element using selector: {selector}. Error: {str(e)}")

    def locate_elements(self, selector) -> list[Locator]:
        try:
            elements = self.page.locator(selector).element_handles()
            self.log.info(f"Located {len(elements)} elements using selector: {selector}")
            return elements
        except Exception as e:
            self._log_and_ss(f"Error locating elements using selector: {selector}. Error: {str(e)}")

    def get_element_text(self, element):
        try:
            return element.text_content()
        except Exception as e:
            self._log_and_ss(f"Error getting element text. Error: {str(e)}")

    def get_elements_text(self, elements):
        try:
            return [element.text_content() for element in elements]
        except Exception as e:
            self._log_and_ss(f"Error getting elements text. Error: {str(e)}")

    def send_text_to_element(self, selector, query):
        try:
            locator = self.locate_element(selector)
            locator.fill(query)
            self.log.info(f"Sent text '{query}' to element using selector: {selector}")
        except Exception as e:
            self._log_and_ss(f"Error sending text {query} to element using selector: {selector}. Error:"
                                      f" {str(e)}")

    def locate_click_element(self, selector):
        try:
            element = self.locate_element(selector)
            element.click()
            self.log.info(f"Clicked element using selector: {selector}")
        except Exception as e:
            self._log_and_ss(f"Error clicking element using selector: {selector}. Error: {str(e)}")

    def assert_element_text(self, selector, expected_text):
        try:
            element = self.locate_element(selector)
            actual_text = element.inner_text()
            assert actual_text == expected_text
            self.log.info(f"Asserted element text for selector: {selector}. Expected: {expected_text}, Actual:"
                          f" {actual_text}")
        except Exception as e:
            self._log_and_ss(f"Error asserting element text for selector: {selector}. Error: {str(e)}")

    def add_event_listener(self, event_type, callback):
        try:
            self.page.on(event_type, callback)
            self.log.info(f"Added event listener for event type: {event_type}")
        except Exception as e:
            self._log_and_ss(f"Error adding event listener for event type: {event_type}. Error: {str(e)}")

    def navigate_to(self, url):
        try:
            self.page.goto(url)
            self.log.info(f"Navigated to: {url}")
            return self.page
        except Exception as e:
            self._log_and_ss(f"Error navigating to URL: {url}. Error: {str(e)}")

    def navigate_to_base_route(self):
        try:
            self.page.goto(self.base_route)
            self.log.info(f"Navigated to: {self.base_route}")
            return self.page
        except Exception as e:
            self._log_and_ss(f"Error navigating to base route. Error: {str(e)}")

    def element_to_be_checked(self, element: ElementHandle) -> bool:
        try:
            result = element.is_checked()
            if result:
                self.log.info(f"Element is checked")
            else:
                self._log_and_ss(f"Element is not checked")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is checked. Error: {str(e)}")

    def element_to_be_disabled(self, element: ElementHandle) -> bool:
        try:
            result = element.is_disabled()
            if result:
                self.log.info(f"Element is disabled")
            else:
                self._log_and_ss(f"Element is not disabled")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is disabled. Error: {str(e)}")

    def element_to_be_editable(self, element: ElementHandle) -> bool:
        try:
            result = element.is_enabled()  # You can use isEnabled to check if an element is editable.
            if result:
                self.log.info(f"Element is editable")
            else:
                self._log_and_ss(f"Element is not editable")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is editable. Error: {str(e)}")

    def element_to_be_empty(self, element: ElementHandle) -> bool:
        try:
            result = not element.text_content().strip()  # Check if element's text is empty
            if result:
                self.log.info(f"Element is empty")
            else:
                self._log_and_ss(f"Element is not empty")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is empty. Error: {str(e)}")

    def element_to_be_enabled(self, element: ElementHandle) -> bool:
        try:
            result = element.is_enabled()
            if result:
                self.log.info(f"Element is enabled")
            else:
                self._log_and_ss(f"Element is not enabled")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is enabled. Error: {str(e)}")

    def element_to_be_hidden(self, element: Locator) -> bool:
        try:
            result = element.is_hidden()
            if result:
                self.log.info(f"Element is hidden")
            else:
                self._log_and_ss(f"Element is not hidden")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is hidden. Error: {str(e)}")

    def element_to_be_visible(self, element: Locator) -> bool:
        try:
            self.wait.wait_for_element_to_be_visible(element)
            result = element.is_visible()
            if result:
                self.log.info(f"Element is visible")
            else:
                self._log_and_ss(f"Element is not visible")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element is visible. Error: {str(e)}")

    def elements_to_be_visible(self, elements: list[Locator]) -> bool:
        try:
            all_visible = True
            for element in elements:
                if not element.is_visible():
                    all_visible = False
                    self._log_and_ss(f"Element is not visible")
                    break

            if all_visible:
                self.log.info(f"All elements are visible")
            return all_visible
        except Exception as e:
            self._log_and_ss(f"Error checking if elements are visible. Error: {str(e)}")

    def element_to_contain_text(self, element: ElementHandle, expected_text: str) -> bool:
        try:
            actual_text = element.text_content()
            result = expected_text in actual_text
            if result:
                self.log.info(f"Element contains the expected text")
            else:
                self._log_and_ss(f"Element does not contain the expected text")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element contains text. Error: {str(e)}")

    def element_to_have_attribute(self, element: ElementHandle, attribute_name: str) -> bool:
        try:
            result = element.get_attribute(attribute_name) is not None
            if result:
                self.log.info(f"Element has the attribute")
            else:
                self._log_and_ss(f"Element does not have the attribute")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has an attribute. Error: {str(e)}")

    def element_to_have_class(self, element: ElementHandle, class_name: str) -> bool:
        try:
            classes = element.get_attribute("class")
            result = class_name in (classes or "")
            if result:
                self.log.info(f"Element has the class")
            else:
                self._log_and_ss(f"Element does not have the class")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has a class. Error: {str(e)}")

    def element_to_have_count(self, elements: list[ElementHandle], expected_count: int) -> bool:
        try:
            result = len(elements) == expected_count
            if result:
                self.log.info(f"Element count is as expected")
            else:
                self._log_and_ss(f"Element count is not as expected")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element count is as expected. Error: {str(e)}")

    def element_to_have_css(self, element: ElementHandle, css_property: str, expected_value: str) -> bool:
        try:
            actual_value = element.get_property("style")[css_property]
            result = actual_value == expected_value
            if result:
                self.log.info(f"Element has the expected CSS property")
            else:
                self._log_and_ss(f"Element does not have the expected CSS property")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has a CSS property. Error: {str(e)}")

    def element_to_have_id(self, element: ElementHandle, expected_id: str) -> bool:
        try:
            element_id = element.get_attribute("id")
            result = element_id == expected_id
            if result:
                self.log.info(f"Element has the expected ID")
            else:
                self._log_and_ss(f"Element does not have the expected ID")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has an ID. Error: {str(e)}")

    def element_to_have_js_property(self, element: ElementHandle, property_name: str, expected_value: str) -> bool:
        try:
            actual_value = element.get_property(property_name)
            result = actual_value == expected_value
            if result:
                self.log.info(f"Element has the expected JavaScript property")
            else:
                self._log_and_ss(f"Element does not have the expected JavaScript property")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has a JavaScript property. Error: {str(e)}")

    def element_to_have_text(self, element: ElementHandle, expected_text: str) -> bool:
        try:
            actual_text = element.text_content()
            result = actual_text == expected_text
            if result:
                self.log.info(f"Element has the expected text")
            else:
                self._log_and_ss(f"Element does not have the expected text")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has text. Error: {str(e)}")

    def element_to_have_value(self, element: ElementHandle, expected_value: str) -> bool:
        try:
            actual_value = element.get_attribute("value")
            result = actual_value == expected_value
            if result:
                self.log.info(f"Element has the expected value")
            else:
                self._log_and_ss(f"Element does not have the expected value")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if element has a value. Error: {str(e)}")

    def element_to_have_values(self, element: ElementHandle, expected_values: list[str]) -> bool:
        try:
            actual_values = element.select_option().selected_values()
            result = actual_values == expected_values
            if result:
                self.log.info(f"Select element has the expected values")
            else:
                self._log_and_ss(f"Select element does not have the expected values")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if select element has expected values. Error: {str(e)}")

    def page_to_have_title(self, expected_title: str) -> bool:
        try:
            actual_title = self.page.title()
            result = actual_title == expected_title
            if result:
                self.log.info(f"Page has the expected title")
            else:
                self._log_and_ss(f"Page does not have the expected title")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if page has a title. Error: {str(e)}")

    def page_to_have_url(self, expected_url: str) -> bool:
        try:
            actual_url = self.page.url
            result = actual_url == expected_url
            if result:
                self.log.info(f"Page has the expected URL")
            else:
                self._log_and_ss(f"Page does not have the expected URL")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if page has a URL. Error: {str(e)}")

    def response_to_be_ok(self, response) -> bool:
        try:
            result = response.ok()
            if result:
                self.log.info(f"Response is OK")
            else:
                self._log_and_ss(f"Response is not OK")
            return result
        except Exception as e:
            self._log_and_ss(f"Error checking if response is OK. Error: {str(e)}")
