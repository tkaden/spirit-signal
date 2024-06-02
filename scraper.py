from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_service = Service('/path/to/chromedriver')  # Update the path
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

def change_zip_code(driver, zip_code):
    driver.get('https://www.totalwine.com')
    time.sleep(3)
    pickup_at = driver.find_element(By.CSS_SELECTOR, 'element_for_pickup_dropdown')  # Replace with actual element
    pickup_at.click()
    time.sleep(2)
    zip_input = driver.find_element(By.CSS_SELECTOR, 'element_for_zip_input')  # Replace with actual element
    zip_input.send_keys(zip_code)
    zip_input.send_keys(Keys.ENTER)
    time.sleep(3)

def search_spirit(driver, spirit):
    search_bar = driver.find_element(By.CSS_SELECTOR, 'element_for_search_bar')  # Replace with actual element
    search_bar.send_keys(spirit)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)
    results = driver.find_elements(By.CSS_SELECTOR, 'element_for_results')  # Replace with actual element
    return results

def check_availability(driver, results):
    available_spirits = []
    for result in results:
        if 'Available' in result.text:  # Simplified condition
            available_spirits.append(result.text)
    return available_spirits

def scrape_spirits(spirits_data):
    driver = setup_driver()
    available_spirits = {}
    for _, row in spirits_data.iterrows():
        change_zip_code(driver, row['zipcode'])
        results = search_spirit(driver, row['spirit'])
        available = check_availability(driver, results)
        if available:
            if row['email'] in available_spirits:
                available_spirits[row['email']].extend(available)
            else:
                available_spirits[row['email']] = available
    driver.quit()
    return available_spirits

if __name__ == "__main__":
    from data import read_csv
    spirits_data = read_csv('spirits.csv')
    available_spirits = scrape_spirits(spirits_data)
    print(available_spirits)
