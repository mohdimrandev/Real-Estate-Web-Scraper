import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    NoSuchWindowException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    driver_service = ChromeService(executable_path=ChromeDriverManager().install())

    # Initialize the WebDriver using ChromeService
    driver = webdriver.Chrome(service=driver_service)

    try:
        # Open the website
        driver.get("https://hprera.nic.in/PublicDashboard")

        # Wait for the content to load
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".form-row .shadow.py-3.px-3.font-sm.radius-3.mb-2")
            )
        )

        # Find all nested <div> elements to get project details
        project_divs = driver.find_elements(
            By.CSS_SELECTOR, ".form-row .shadow.py-3.px-3.font-sm.radius-3.mb-2"
        )

        project_details = []

        # Iterate through the first 6 project <div> elements
        for div_element in project_divs[:6]:
            project_info = {}

            try:
                rera_code_link = div_element.find_element(By.TAG_NAME, "a")

                # Click on the <a> tag to open the details modal dialog
                rera_code_link.click()

                # Wait for the modal dialog to appear
                WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".modal-dialog.modal-xl")
                    )
                )

                time.sleep(3)

                # Find and extract specific fields from the modal content
                fields = driver.find_elements(
                    By.CSS_SELECTOR,
                    ".table.table-borderless.table-sm.table-responsive-lg.table-striped.font-sm tbody tr",
                )

                for field in fields:
                    label = field.find_element(
                        By.CSS_SELECTOR, "td:nth-child(1)"
                    ).text.strip()
                    value_element = field.find_element(
                        By.CSS_SELECTOR, "td:nth-child(2)"
                    )

                    # Extract text from <span> elements and avoid <a> elements
                    span_elements = value_element.find_elements(By.CSS_SELECTOR, "span")
                    value = ""
                    for span in span_elements:
                        if span.text.strip() and not span.find_elements(
                            By.TAG_NAME, "a"
                        ):
                            value += span.text.strip() + " "

                    value = value.strip()

                    # Assign value to project_info based on label
                    if label == "PAN No.":
                        project_info["PAN"] = value
                    elif label == "GSTIN No.":
                        project_info["GSTIN"] = value
                    elif label == "Permanent Address":
                        project_info["Permanent Address"] = value
                    elif label == "Name":
                        value = value_element.text.strip()
                        project_info["Name"] = value

                project_details.append(project_info)

                # Close the modal dialog
                close_button = driver.find_element(
                    By.CSS_SELECTOR, ".modal-content button.close"
                )
                close_button.click()

                time.sleep(1)

            except NoSuchElementException as e:
                print(f"Element not found: {e}")

            except NoSuchWindowException as e:
                print(f"Window closed prematurely: {e}")
                break

        # Print the extracted project details
        for idx, project in enumerate(project_details, start=1):
            print(f"Project {idx}:")
            print(f"Name : {project.get('Name', 'Not available')}")
            print(f"PAN No.: {project.get('PAN', 'Not available')}")
            print(f"GSTIN No.: {project.get('GSTIN', 'Not available')}")
            print(
                f"Permanent Address: {project.get('Permanent Address', 'Not available')}"
            )
            print()

        df = pd.DataFrame(project_details)

        # Write DataFrame to CSV file
        csv_file = "real_estate_details.csv"
        df.to_csv(csv_file, index=False, encoding="utf-8")

        print(f"Real estate details written to {csv_file}")

    except TimeoutException as e:
        print(f"Timeout waiting for page to load: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

finally:
    driver.quit()
