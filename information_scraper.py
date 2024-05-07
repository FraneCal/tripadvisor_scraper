import os
from bs4 import BeautifulSoup
import requests
import csv
import time

# Read URLs from the file
with open("restaurant_links.txt", "r") as file:
    urls = file.readlines()

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

csv_file = 'restaurant_data.csv'

# Open a CSV file in append mode
with open(csv_file, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Check if the file exists and is non-empty
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        # File is not empty, no need to write the header row
        write_header = False
    else:
        # File is empty, write the header row
        write_header = True
        writer.writerow(['URL', 'Name', 'Address', 'Number of Reviews', 'Tripadvisor_hashtag', 'Phone', 'Pricing', 'Cuisine Type', 'Open Hours'])

    counter = 0
    for url in urls:
        counter += 1
        print(f"Currently at link number {counter}.")
        # Strip any leading or trailing whitespaces from the URL
        url = url.strip()

        # Send request to the URL
        response = requests.get(url, headers=header)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            name = soup.find('h1', class_='biGQs _P egaXP rRtyp').getText()
        except AttributeError:
            name = "Name Not Found"

        try:
            address = soup.find('div', class_='biGQs _P pZUbB hmDzD').getText()
        except AttributeError:
            address = "Address Not Found"

        try:
            number_of_reviews = soup.find('span', class_='GPKsO').getText().split(' ')[0]
        except AttributeError:
            number_of_reviews = "Number of Reviews Not Found"

        try:
            hashtag = soup.find('span', class_='bTeln').find('span').getText()
        except AttributeError:
            hashtag = "Hashtag Not Found"

        try:
            phone = soup.find_all('span', class_='biGQs _P pZUbB hmDzD')[8].getText()
        except IndexError:
            phone = "Phone Not Found"

        try:
            pricing = soup.find('span', class_='HUMGB cPbcf').getText().split(',')[0]
        except AttributeError:
            pricing = "Pricing Not Found"

        try:
            cuisine_type = soup.find('span', class_='HUMGB cPbcf').getText().split(',')[1:]
        except AttributeError:
            cuisine_type = "Cuisine Type Not Found"

        try:
            open_hours = soup.find('span', class_='biGQs _P pZUbB egaXP hmDzD').getText()
        except AttributeError:
            open_hours = "Open Hours Not Found"

        # Write data to CSV
        writer.writerow([url, name, address, number_of_reviews, hashtag, phone, pricing, cuisine_type, open_hours])

        time.sleep(0.2)
