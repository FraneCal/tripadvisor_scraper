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

box = soup.find('div', class_='biGQs')
link = box.find('a')

print(box)




# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementNotInteractableException
# from fake_useragent import UserAgent
# import time
# import base64
# from solver import PuzleSolver


# def solve_captcha_slider(driver):
#     try:
#         background_image_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="captcha__puzzle"]/canvas[1]'))
#         )
#         slice_image_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="captcha__puzzle"]/canvas[2]'))
#         )

#         background_image_data = driver.execute_script(
#             "return arguments[0].toDataURL('image/png').substring(21);",
#             background_image_element
#         )
#         slice_image_data = driver.execute_script(
#             "return arguments[0].toDataURL('image/png').substring(21);",
#             slice_image_element
#         )

#         # Decode the Base64-encoded image data into bytes
#         background_image_bytes = base64.b64decode(background_image_data)
#         slice_image_bytes = base64.b64decode(slice_image_data)

#         # Save the images to files
#         with open('background.png', 'wb') as background_file:
#             background_file.write(background_image_bytes)

#         with open('piece.png', 'wb') as piece_file:
#             piece_file.write(slice_image_bytes)

#         solver = PuzleSolver("piece.png", "background.png")
#         solution = solver.get_position()

#         slider = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button'))
#         )
#         actions.move_to_element(slider).click_and_hold().move_by_offset(solution, 0).release().perform()

#         while True:
#             try:
#                 slider = driver.find_element(By.CLASS_NAME, 'geetest_slider_button')
#                 actions.move_to_element(slider).click_and_hold().move_by_offset(solution, 0).release().perform()
#                 try:
#                     try_again_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_reset_tip_content')))
#                     try_again_button.click()
#                 except TimeoutException:
#                     print('No button "Try again" found.')
#                     break
#             except TimeoutException:
#                 print('No slider found. Continuing with the code.')
#                 break

#     except NoSuchElementException:
#         print("Slider elements not found. Continuing on.")
#     except TimeoutException:
#         print("Timeout occurred while waiting for slider elements.")

# URL = "https://www.tripadvisor.com/Restaurants-g186338-London_England.html"

# # Generate fake user agents
# options = Options()
# ua = UserAgent()
# user_agent = ua.random

# options.add_argument(f'--user-agent={user_agent}')
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")

# driver = webdriver.Chrome(options=options)
# actions = ActionChains(driver)
# driver.get(URL)
# time.sleep(100)

# try: 
#     solve_captcha_slider(driver)
# except:
#     print("No slider found.")

# time.sleep(2)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# page_source = driver.page_source

# driver.quit()

# soup = BeautifulSoup(page_source, "html.parser")

# box = soup.find('div', class_='biGQs')
# link = box.find('a')

# print(box)
