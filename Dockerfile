# Use a base image (e.g., Python with Playwright pre-installed)
FROM mcr.microsoft.com/playwright/python:v1.37.0-jammy

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Create directories for results and screenshots
RUN mkdir -p /results /screenshots

# Copy the test code and data into the container
COPY . /app

# Set environment variables (optional)
ENV RESULTS_DIRECTORY /results
ENV SCREENSHOTS_DIRECTORY /screenshots

# Entry point for running tests
CMD ["pytest"]
