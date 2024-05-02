from bs4 import BeautifulSoup
import requests

URL = 'https://www.tripadvisor.com//Restaurant_Review-g186338-d1770199-Reviews-Ecco_Pizza-London_England.html'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
response.raise_for_status()

web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

title = soup.find('h1', class_='biGQs _P egaXP rRtyp').getText()
print(title)
