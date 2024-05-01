from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

URL = "https://www.tripadvisor.com/Restaurants-g186338-London_England.html"

options = Options()
ua = UserAgent()
user_agent = ua.random

options.add_argument(f'--user-agent={user_agent}')
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.get(URL)

time.sleep(5)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

print(soup)
