import os
import time
import logging

import utils.logger_utils as lu

logger = lu.custom_logger(logging.DEBUG)


class ABC:
    """
    a base class
    """

    def take_screenshot(self, page, result_message, file_extension="png"):
        """
        Take a screenshot of the current open web page using Playwright.
        """
        try:
            file_name = f"{result_message}.{round(time.time() * 1000)}.{file_extension}"
            if len(file_name) >= 200:
                file_name = f"{round(time.time() * 1000)}.{file_extension}"

            screenshot_directory = "../screenshots/"
            relative_file_name = os.path.join(screenshot_directory, file_name)

            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)

            page.screenshot(path=relative_file_name)

            # Get the absolute path of the saved screenshot
            absolute_file_path = os.path.abspath(relative_file_name)

            # You can also attach the screenshot to a test report if needed
            # allure.attach_file(relative_file_name, name=file_name, attachment_type=allure.attachment_type.PNG)
            logger.info(f"Screenshot saved to directory: {absolute_file_path}")

        except Exception as e:
            logger.error("### Exception Occurred when taking a screenshot:", str(e))
