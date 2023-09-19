# Use a base image (e.g., Python with Playwright pre-installed)
FROM mcr.microsoft.com/playwright/python:v1.37.0-jammy

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Create directories for results and screenshots
RUN mkdir /app/results
RUN mkdir /app/screenshots

# Copy the test code and data into the container
COPY . /app

ENV PYTHONPATH /app:$PYTHONPATH


CMD ["pytest"]