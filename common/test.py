import logging

from common.ABC import ABC
from utils.logger_utils import custom_logger

logger = custom_logger(log_level=logging.DEBUG)


class Test(ABC):

    def _log_and_raise_error(self, error_message):
        try:
            logger.error(error_message)
            raise RuntimeError(error_message)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            raise e

    def assert_equal(self, actual, expected, message=None):
        try:
            assert actual == expected, f"Assertion Failed: {message or ''}Expected {expected}, but got {actual}"
            logger.info(f"Assertion Successful: {message or ''}Expected '{expected}' and got '{actual}'")
        except AssertionError as e:
            self._log_and_raise_error(f"Assertion Failed: {message or ''}Expected {expected}, but got {actual}")

    def assert_not_equal(self, actual, not_expected, message=None):
        try:
            assert actual != not_expected, f"Assertion Failed: {message or ''}Did not expect {not_expected}, but got {actual}"
            logger.info(f"Assertion Successful: {message or ''}Did not expect '{not_expected}' and got '{actual}'")
        except AssertionError as e:
            self._log_and_raise_error(f"Assertion Failed: {message or ''}Did not expect {not_expected}, but got {actual}")

    def assert_all_elements_equal(self, elements, expected_element, message=None):
        try:
            for element in elements:
                assert element == expected_element, f"Assertion Failed: {message or ''}Element '{element}' does not match '{expected_element}'"

            logger.info(f"Assertion Successful: {message or ''}All elements match '{expected_element}'")
        except AssertionError as e:
            self._log_and_raise_error(
                f"Assertion Failed: {message or ''}One or more elements do not match '{expected_element}'")

    def assert_all_elements_dont_equal(self, elements, not_expected_element, message=None):
        try:
            for element in elements:
                assert element != not_expected_element, f"Assertion Failed: {message or ''}Element '{element}' should not equal '{not_expected_element}'"

            logger.info(f"Assertion Successful: {message or ''}None of the elements equal '{not_expected_element}'")
        except AssertionError as e:
            self._log_and_raise_error(
                f"Assertion Failed: {message or ''}One or more elements equal '{not_expected_element}'")

    def assert_true(self, condition, message=None):
        try:
            assert condition is True, f"Assertion Failed: {message or ''}Expected True, but got {condition}"
            logger.info(f"Assertion Successful: {message or ''}Condition is True")
        except AssertionError as e:
            self._log_and_raise_error(f"Assertion Failed: {message or ''}Expected True, but got {condition}")

    def assert_false(self, condition, message=None):
        try:
            assert condition is False, f"Assertion Failed: {message or ''}Expected False, but got {condition}"
            logger.info(f"Assertion Successful: {message or ''}Condition is False")
        except AssertionError as e:
            self._log_and_raise_error(f"Assertion Failed: {message or ''}Expected False, but got {condition}")