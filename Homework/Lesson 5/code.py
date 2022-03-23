import time

from selenium import webdriver
from pymongo import MongoClient

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pymongo.errors import DuplicateKeyError


MAX_WAIT_TIME = 5000000000
MONGO_PORT = 27017
MONGO_IP = '127.0.0.1'
DB_NAME = 'Messages'
BASE_URL = 'https://account.mail.ru/login'
EMAIL_LOGIN = 'study.ai_172@mail.ru'
EMAIL_PASSWORD = 'NextPassword172#'

client = MongoClient(MONGO_IP, MONGO_PORT)
db = client[DB_NAME]
mailru = db.mailru
mailruhref = db.mailruhref

chrome_options = Options()
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
driver.get(BASE_URL)
driver.implicitly_wait(10)

elem = driver.find_element(By.NAME, 'username')
elem.send_keys(EMAIL_LOGIN)
elem.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
elem = driver.find_element(By.NAME, 'password')
elem.send_keys(EMAIL_PASSWORD)
elem.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

'''PARSING'''
# get frame for scrolling
frame = driver.find_element(By.XPATH, "//div[@aria-label='grid']")

# create collection in DB of messages '_id' and 'href'
while True:
    elements = driver.find_elements(By.XPATH, '//a[@data-uidl-id]')
    for elem in elements:
        item = {}
        item['_id'] = elem.get_attribute('data-uidl-id')
        item['href'] = elem.get_attribute('href')
        try:
            mailruhref.insert_one(item)
        except DuplicateKeyError:
            pass
    frame.send_keys(Keys.PAGE_DOWN)
    start_time = time.time_ns()
    while driver.find_elements(By.XPATH, '//a[@data-uidl-id]') == elements:
        time.time()
        if (time.time_ns() - start_time) > MAX_WAIT_TIME:
            break
    if elements == driver.find_elements(By.XPATH, '//a[@data-uidl-id]'):
        break

# a list of emails that are already in the database
db_message_list = []
for item in mailru.find():
    db_message_list.append(item['_id'])
db_message_list = tuple(db_message_list)

# links processing
item_add_count = 0
for item in mailruhref.find():
    if item['_id'] in db_message_list:  # checking for the presence of a message in DB
        continue
    message = {}
    message_url = item['href']
    driver.get(message_url)
    driver.implicitly_wait(10)
    message['_id'] = item['_id']
    message['title'] = driver.find_element(By.XPATH, '//h2[@class="thread-subject"]').text
    message['from_contact'] = driver.find_element(By.XPATH, '//span[@class="letter-contact"]').get_attribute('title')
    message['mes_date'] = driver.find_element(By.XPATH, '//div[@class="letter__date"]').text
    message['message_body'] = driver.find_element(By.XPATH, '//div[@class="letter__body"]').text
    mailru.insert_one(message)
    item_add_count += 1
print(item_add_count)
