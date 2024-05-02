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
