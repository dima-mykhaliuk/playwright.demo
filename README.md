# Playwright Demo Framework

## Setup

To set up the suite, follow these steps:

1. Install Playwright by running the following command: `playwright install`

## Running Tests

You can run the tests in multiple ways:

1. **Via Test Runners:**
- Use `runners/my_invoker.py` to run the suite programmatically.

2. **Directly Running the Test Suite or Methods:**
- Execute the test suite or specific test methods by running the Python script.

3. **Via Command Line:**
- Run the tests from the terminal using the following command:
  ```
  python -m pytest
  ```

- If you want to generate an HTML report after each test run, uncomment the following line in your pytest configuration (pytest.ini):
  ```
  # --html=results/report.html
  ```

## Test Configuration

- Test configurations are specified in `data/test_data.json`.
- You can set `test_id` above the test class to run test cases (class methods) in a specific configuration from `test_data.json`.

## Logs

- Test logs are stored in `results/automation.log`.
- HTML reports (if enabled in pytest.ini) are generated in the `results/` directory.
