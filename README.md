# Real Estate Web Scraper

This Python script automates the extraction of project details from the [Himachal Pradesh Real Estate Regulatory Authority (HP RERA)](https://hprera.nic.in/PublicDashboard), extracting details such as GSTIN Number (Goods and Services Tax Identification Number), PAN Number (Permanent Account Number), Project Name, and Permanent Address.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Output](#output)
- [Additional Notes](#additional-notes)

## Introduction

This project aims to automate the extraction of project data from the Himachal Pradesh Real Estate Regulatory Authority (HP RERA) Public Dashboard. It leverages web scraping techniques implemented using Python and Selenium WebDriver to efficiently gather specific project details.

## Features

- Scrapes project details such as Name, PAN No, GSTIN No, and Permanent Address.
- Stores extracted data in a CSV file for further analysis.

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium WebDriver](https://img.shields.io/badge/-selenium_web_driver-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Techniques Used

- Web Scraping: Automated extraction of data from web pages.
- Data Parsing: Extracting specific fields from HTML elements.
- Error Handling: Handling potential exceptions during scraping.

## Prerequisites

### Before running this project locally, ensure you have the following installed:

- Python: You can download it from the official website at [https://www.python.org/downloads/](https://www.python.org/downloads/).
- An IDE such as Visual Studio Code: You can download it from [https://code.visualstudio.com/](https://code.visualstudio.com/).
- Chrome browser (for Selenium automation): You can download it from [https://www.google.com/chrome/](https://www.google.com/chrome/).

## Setup

### 1. Clone the repository

- Clone the repository using the following command:

  ```cmd
  git clone https://github.com/mohdimrandev/Real-Estate-Web-Scraper.git
  ```

### 2. Navigate to the project directory

- Change to the project directory using the following command:

  ```cmd
  cd Real-Estate-Web-Scraper
  ```

### 3. Install dependencies

- Run the following command in the project directory to install the required dependencies from `requirements.txt`.

  ```cmd
  pip install -r requirements.txt
  ```

## Running the Project

- Start the scraper using Python:

  ```cmd
  python real_estate_web_scraper.py
  ```

## Output

- The scraped project details will be saved in a CSV file named `project_details.csv`.

## Additional Notes

- Ensure ChromeDriver is compatible with your Chrome browser version. `webdriver-manager` is used to handle this automatically.
