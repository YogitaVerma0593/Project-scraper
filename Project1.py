from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://rera.odisha.gov.in/projects/project-list")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "project-card"))
)

data = []

for i in range(6): 
    try:
        print(f"--- Attempting to process project {i+1} ---")
        cards = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "project-card"))
        )

        current_card = cards[i]
        driver.execute_script("arguments[0].scrollIntoView(true);", current_card)
        time.sleep(0.5)

        view_details_button = WebDriverWait(current_card, 15).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[contains(text(), 'View Details')]"))
        )
        view_details_button.click()

        project_name_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Project Name']/following-sibling::strong"))
        )
        project_name = project_name_element.text.strip() if project_name_element.text.strip() else "N/A"
        rera_number_element = driver.find_element(By.XPATH, "//label[contains(text(), 'RERA Regd. No.')]/following-sibling::strong")
        rera_number = rera_number_element.text.strip() if rera_number_element.text.strip() else "N/A"
        print(f"Project Name: {project_name}, RERA No: {rera_number}")

        promoter_tab = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Promoter Details')]"))
        )
        promoter_tab.click()
        promoter_name_element = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH, "//label[text()='Company Name']/following-sibling::strong")
            if driver.find_element(By.XPATH, "//label[text()='Company Name']/following-sibling::strong").text.strip() not in ["", "--"]
            else False
        )
        promoter_name = promoter_name_element.text.strip() if promoter_name_element else "N/A" 

        promoter_address_element = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH, "//label[contains(text(), 'Registered Office Address')]/following-sibling::strong")
            if driver.find_element(By.XPATH, "//label[contains(text(), 'Registered Office Address')]/following-sibling::strong").text.strip() not in ["", "--"]
            else False
        )
        promoter_address = promoter_address_element.text.strip() if promoter_address_element else "N/A"

        gst_number_element = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH, "//label[contains(text(), 'GST No.')]/following-sibling::strong")
            if driver.find_element(By.XPATH, "//label[contains(text(), 'GST No.')]/following-sibling::strong").text.strip() not in ["", "--"]
            else False
        )
        gst_number = gst_number_element.text.strip() if gst_number_element else "N/A"

        print(f"Promoter Name: {promoter_name}, Address: {promoter_address}, GST: {gst_number}")
        data.append({
            "Project Name": project_name,
            "RERA Regd. No.": rera_number,
            "Promoters Name": promoter_name,
            "Promoters Address": promoter_address,
            "GST No.": gst_number
        })
        driver.back()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "project-card"))
        )

    except Exception as e:
        print(f"Error processing project {i+1}: {e}")
        try:
            driver.back()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "project-card"))
            )
        except Exception as back_error:
            print(f"Failed to navigate back after error: {back_error}. Exiting loop.")
            break 

df = pd.DataFrame(data)
df.to_csv("first_6_projects.tsv", sep='\t', index=False)
print("\nScraping complete. Data saved to 'first_6_projects.csv'")
driver.quit()