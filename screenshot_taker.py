from bs4 import BeautifulSoup
from selenium import webdriver
import os

def get_restaurant_name(url):
    start_index = url.find('Reviews-') + len('Reviews-')
    end_index = url.find('-London')
    return url[start_index:end_index]

with open("restaurant_links.txt", "r") as file:
    urls = file.readlines()

# Instantiate the web driver outside the loop
driver = webdriver.Chrome()

for url in urls:
    url = url.strip()

    driver.get(url)

    page_source = driver.page_source

    restaurant_name = get_restaurant_name(url)
    screenshot_filename = f"{restaurant_name}.png"

    screenshot_path = os.path.join("screenshots", screenshot_filename)
    driver.save_screenshot(screenshot_path)

    soup = BeautifulSoup(page_source, "html.parser")


# --------------- SELENIUM --------------- #
# from selenium import webdriver
# import time

# URL = 'https://www.tripadvisor.com//Restaurant_Review-g186338-d1770199-Reviews-Ecco_Pizza-London_England.html'
# driver = webdriver.Chrome()
# driver.get(URL)
# time.sleep(5)
# driver.save_screenshot('image.png')
# driver.quit()



    

# --------------- PLAYWRIGHT --------------- #
# from playwright.sync_api import sync_playwright

# URL = 'https://www.tripadvisor.com//Restaurant_Review-g186338-d1770199-Reviews-Ecco_Pizza-London_England.html'

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     # Create a new page
#     page = browser.new_page()
#     # Navigate to the URL
#     page.goto(URL)
#     # Wait for some time (if needed)
#     page.wait_for_timeout(5000)
#     # Take a screenshot
#     page.screenshot(path='image.png')
#     # Close the browser
#     browser.close()
