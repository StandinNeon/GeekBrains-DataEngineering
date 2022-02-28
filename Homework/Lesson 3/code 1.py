import requests
import json
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError

client = MongoClient('127.0.0.1', 27017)

db = client['Vacancies']
hhru = db.hhru

base_url = "https://hh.ru"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
params = {'area': 1, 'search_field': 'description', 'text': 'data engineer', 'hhtmFrom': 'vacancy_search_list', 'items_on_page': 20, 'only_with_salary': True}
url = f'{base_url}/search/vacancy'
response = requests.get(url, headers=headers, params = params)

dom = BeautifulSoup(response.text, 'html.parser')
items = dom.find_all('div', {'class': 'vacancy-serp-item vacancy-serp-item_redesigned'})

items_added = 0
items_not_added = 0
vac_len = 0

while True:
    for item in items:
        item_data ={}
        link_title = item.find('a',{'data-qa': 'vacancy-serp__vacancy-title'})
        item_data['link'] = link_title['href']
        item_data['title'] = link_title.getText()
        item_data['company'] = ((item.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})).getText()).replace('\xa0', ' ')
        item_data['location'] = (item.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})).getText()
        compensation = item.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
        if type(compensation) == type(link_title):
            salary = (compensation.getText()).replace('\u202f', '')
            item_data['salary_keyword'] = ''
            if 'от ' in salary:
                item_data['salary_keyword'] = 'от '
            elif 'до ' in salary:
                item_data['salary_keyword'] = 'до '
            else:
                item_data['salary_keyword'] = None

            item_data['salary_from'] = ''
            while True:
                if salary[0].isdigit() == True:
                    item_data['salary_from'] = item_data['salary_from'] + salary[0]
                    salary = salary[1:]
                else:
                    salary = salary[1:]
                if item_data['salary_from'] != '' and salary[0].isdigit() == False:
                    break
            item_data['salary_from'] = int(item_data['salary_from'])

            item_data['salary_to'] = ''
            while True:
                for char in salary:
                    if char.isdigit() == True:
                        item_data['salary_to'] = item_data['salary_to'] + char
                break
            if item_data['salary_to'] != '':
                item_data['salary_to'] = int(item_data['salary_to'])
            else:
                item_data['salary_to'] = None

            if 'руб.' in salary:
                item_data['salary_currency'] = 'руб.'
            elif 'USD' in salary:
                item_data['salary_currency'] = 'USD'
            elif 'EUR' in salary:
                item_data['salary_currency'] = 'EUR'
            else:
                item_data['salary_currency'] = None
        else:
            salary_keyword = None
            salary_from = None
            item_data['salary_to'] = None
            item_data['salary_currency'] = None
        snippet = item.find('div', {'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
        if snippet != None:
            item_data['snippet'] = snippet.getText()
        else:
            item_data['snippet'] = None
        item_data['site'] = base_url
        item_data['_id'] = int((re.search(r'\d{7,10}', item_data['link'])).group()) # Формирует id вакансии

        try:
            hhru.insert_one(item_data)
            items_added += 1
        except DuplicateKeyError:
            items_not_added += 1

    next_page_url = dom.find('a', {'data-qa': 'pager-next'})
    if next_page_url == None:
        break
    next_page_url = next_page_url['href']
    url = f'{base_url}{next_page_url}'
    response = requests.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    items = dom.find_all('div', {'class': 'vacancy-serp-item vacancy-serp-item_redesigned'})

for vac in hhru.find({}):
    vac_len += 1
print(f'In collection hhru {vac_len} objects')
print(f'Added {items_added} objects')
print(f'Don\'t added {items_not_added} objects')
