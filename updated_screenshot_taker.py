import csv
import re
import time
from http.cookies import SimpleCookie

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Function to extract restaurant name from URL
def extract_restaurant_name(url):
    match = re.search(r'Reviews-(.*?)-London', url)
    if match:
        return match.group(1)
    else:
        return "Unknown"

# Read URLs from the CSV file
with open("links_for_screenshot.csv", "r") as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

# Read cookies from cookie file
with open("cookie.txt") as fp:
    cookie = SimpleCookie()
    cookie.load(fp.read())

# Set the path to the Firefox binary
firefox_path = 'C:\Program Files\Mozilla Firefox\firefox.exe'

# Initialize Firefox webdriver with binary path
driver = webdriver.Firefox(executable_path=firefox_path)
driver.maximize_window()

# Set Cookie
driver.get("https://www.tripadvisor.com/static/decodeKey.txt")
for name, morsel in cookie.items():
    driver.add_cookie({"name": name, "value": morsel.value})

counter = 0
for url in urls:
    # Open URL
    counter += 1
    print(f"Currently at link number {counter}.")
    driver.get(url)

    # Wait for some time (if needed)
    time.sleep(3)

    # Take screenshot
    try:
        driver.find_element(By.CSS_SELECTOR, "#lithium-root")
        restaurant_name = extract_restaurant_name(url)
        driver.save_screenshot(f"screenshots/{restaurant_name}.png")
    except NoSuchElementException:
        print("You may have been blocked")
        break

driver.quit()
