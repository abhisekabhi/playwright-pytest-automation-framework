# Playwright Pytest Scraper Framework

## About Project

This project is developed using Python, Playwright and Pytest.

It automates web data extraction from websites Links and stores extracted data into CSV files.

The framework follows Page Object Model (POM) structure for better code maintenance and reusability.


## Tech Stack

- Python
- Playwright
- Pytest
- EasyOCR
- CSV


## Features

- Browser automation using Playwright
- Pytest framework integration
- Page Object Model (POM)
- Dynamic web page handling
- CAPTCHA image reading using EasyOCR
- Automatic CAPTCHA text extraction
- Data extraction from web pages
- CSV file generation
- Screenshot capture for debugging


## Project Structure
pages/
Page classes and web locators

tests/
Test execution files

utils/
CSV writing utilities

conftest.py
Browser setup and pytest fixtures



## How to Run

Install dependencies:


pip install -r requirements.txt


Install Playwright browsers:


playwright install



Run test:


pytest -v



## Output

- Extracted data is saved into CSV file
- Error screenshots are captured for debugging
- CAPTCHA handling flow implemented using EasyOCR


## Author

Abhisek Nayak
