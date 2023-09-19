import os
import pytest
from playwright.sync_api import sync_playwright

from utils.logger_utils import custom_logger
from utils.json_utils import read_json
import logging

logger = custom_logger(logging.DEBUG)


@pytest.fixture(scope="class")
def class_setup(request):
    test_data_id = request.node.get_closest_marker("test_data").args[0]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "../data/test_data.json")
    test_data = read_json(json_file_path)
    test_config = next((config for config in test_data if config["id"] == test_data_id), None)

    if test_config is None:
        raise ValueError(f"Test configuration not found for ID: {test_data_id}")

    logger.info(f"----------- Test {test_data_id} started -----------")

    with sync_playwright() as p:
        browser = None
        browser_type = test_config.get("browser")
        launch_options = {
            "headless": True
        }

        try:
            if browser_type == "chromium":
                browser = p.chromium.launch(**launch_options)
            elif browser_type == "firefox":
                browser = p.firefox.launch(**launch_options)
            elif browser_type == "webkit":
                browser = p.webkit.launch(**launch_options)
            else:
                raise ValueError(f"Invalid browser type: {browser_type}")

            test_config["browser"] = browser

            yield test_config
        except Exception as e:
            print(e)
        finally:
            if browser:
                browser.close()

    logger.info(f"----------- Test {test_data_id} ended -----------")
