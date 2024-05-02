from bs4 import BeautifulSoup
import requests

URL = "https://www.tripadvisor.com/Restaurants-g186338-London_England.html"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
response.raise_for_status()

web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

# GETTING THE LINKS FROM THE FIRST PAGE
boxes = soup.find_all('div', class_='biGQs _P fiohW alXOW NwcxK GzNcM ytVPx UTQMg RnEEZ ngXxk')
links = ['https://www.tripadvisor.com/'+ box.find('a').get('href') for box in boxes]

with open("tripadvisor_links.txt", "a") as file:
    for link in links:
        file.write(link + "\n")


# GETTING THE LINKS FROM REST OF THE PAGES
for i in range(30, 120, 30):
    URL = f"Https://www.tripadvisor.com/Restaurants-g186338-oa{i}-London_England.html"
    print(f"Curenctly at {i}.")

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(URL, headers=header)
    response.raise_for_status()

    web_page = response.text
    soup = BeautifulSoup(web_page, 'html.parser')

    boxes = soup.find_all('div', class_='biGQs _P fiohW alXOW NwcxK GzNcM ytVPx UTQMg RnEEZ ngXxk')
    links = []
    for box in boxes:
        links.append('https://www.tripadvisor.com/' + box.find('a').get('href'))

    with open("tripadvisor_links.txt", "a") as file:
        for link in links:
            file.write(link + "\n")
    print("Links have been writen.")
