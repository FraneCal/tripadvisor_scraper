import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

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
        slider_container = driver.find_element(By.XPATH, '//*[@id="captcha__frame__bottom"]/div[2]')
        slider = driver.find_element(By.XPATH, '//*[@id="captcha__frame__bottom"]/div[2]/div[2]')

        for x in range(10000):
            actions.move_to_element(slider).click_and_hold().move_by_offset(x, 0).release().perform()
            time.sleep(0.1)
    except NoSuchElementException:
        print("No slider found.")

    time.sleep(3)

    # Take screenshot
    driver.save_screenshot(f'{url.replace("/", "_").replace(":", "_")}.png')

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
