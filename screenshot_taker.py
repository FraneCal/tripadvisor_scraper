import csv
from playwright.sync_api import sync_playwright

# Read URLs from the CSV file
urls = []
with open("links_for_screenshots.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        urls.append(row[0])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    for url in urls:
        # Create a new page
        page = browser.new_page()

        # Navigate to the URL
        page.goto(url)

        # Wait for some time (if needed)
        page.wait_for_timeout(5000)

        # Take a screenshot
        page.screenshot(path=f'{url.replace("/", "_").replace(":", "_")}.png')

        # Close the page
        page.close()

    # Close the browser
    browser.close()
