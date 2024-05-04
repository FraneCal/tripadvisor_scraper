import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re

# Function to extract restaurant name from URL
def extract_restaurant_name(url):
    match = re.search(r'Reviews-(.*?)-London', url)
    if match:
        return match.group(1)
    else:
        return "Unknown"

# Read URLs from the CSV file
urls = []
with open("links_for_screenshots.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        urls.append(row[0])

# Initialize Chrome webdriver
driver = webdriver.Chrome()
actions = ActionChains(driver)

for url in urls:
    # Open URL
    driver.get(url)

    # Wait for some time (if needed)
    time.sleep(5)

    try:
        slider_container = driver.find_element(By.CSS_SELECTOR, 'div.sliderContainer')
        slider = driver.find_element(By.CLASS_NAME, 'div.sliderContainer > div.slider')

        for x in range(10000):
            actions.move_to_element(slider).click_and_hold().move_by_offset(x, 0).release().perform()
            time.sleep(0.1)
    except NoSuchElementException:
        print("No slider found.")

    time.sleep(3)

    # Extract restaurant name
    restaurant_name = extract_restaurant_name(url)

    # Take screenshot
    driver.save_screenshot(f'{restaurant_name}.png')

# Quit webdriver
driver.quit()





# ------------------------ PLAYWRIGHT ------------------------ #
# import csv
# from playwright.sync_api import sync_playwright

# # Read URLs from the CSV file
# urls = []
# with open("links_for_screenshots.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         urls.append(row[0])

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)

#     for url in urls:
#         # Create a new page
#         page = browser.new_page()

#         # Navigate to the URL
#         page.goto(url)

#         # Wait for some time (if needed)
#         page.wait_for_timeout(5000)

#         # Take a screenshot
#         page.screenshot(path=f'{url.replace("/", "_").replace(":", "_")}.png')

#         # Close the page
#         page.close()

#     # Close the browser
#     browser.close()
