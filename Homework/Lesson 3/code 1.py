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

while True:
    for item in items:
        item_data ={}
        link_title = item.find('a',{'data-qa': 'vacancy-serp__vacancy-title'})
        link = link_title['href']
        title = link_title.getText()
        company = ((item.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})).getText()).replace('\xa0', ' ')
        location = (item.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})).getText()
        compensation = item.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
        if type(compensation) == type(link_title):
            salary = (compensation.getText()).replace('\u202f', '')
            salary_keyword = ''
            if 'от ' in salary:
                salary_keyword = 'от '
            elif 'до ' in salary:
                salary_keyword = 'до '
            else:
                salary_keyword = None

            salary_from = ''
            while True:
                if salary[0].isdigit() == True:
                    salary_from = salary_from + salary[0]
                    salary = salary[1:]
                else:
                    salary = salary[1:]
                if salary_from != '' and salary[0].isdigit() == False:
                    break
            salary_from = int(salary_from)

            salary_to = ''
            while True:
                for char in salary:
                    if char.isdigit() == True:
                        salary_to = salary_to + char
                break
            if salary_to != '':
                salary_to = int(salary_to)
            else:
                salary_to = None

            salary_currency = ''
            if 'руб.' in salary:
                salary_currency = 'руб.'
            elif 'USD' in salary:
                salary_currency = 'USD'
            elif 'EUR' in salary:
                salary_currency = 'EUR'
            else:
                salary_currency = None
        else:
            salary_keyword = None
            salary_from = None
            salary_to = None
            salary_currency = None
        snippet = item.find('div', {'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
        if snippet != None:
            snippet = snippet.getText()
        else:
            snippet = None
        site = base_url

        item_data['link'] = link
        item_data['_id'] = int((re.search(r'\d{7,10}', item_data['link'])).group()) # Формирует id вакансии
        item_data['title'] = title
        item_data['company'] = company
        item_data['location'] = location
        item_data['salary_keyword'] = salary_keyword
        item_data['salary_from'] = salary_from
        item_data['salary_to'] = salary_to
        item_data['salary_currency'] = salary_currency
        item_data['snippet'] = snippet
        item_data['site'] = site
        try:
            hhru.insert_one(item_data)
        except DuplicateKeyError:
            print('Document is already exist')

    next_page_url = dom.find('a', {'data-qa': 'pager-next'})
    if next_page_url == None:
        break
    next_page_url = next_page_url['href']
    url = f'{base_url}{next_page_url}'
    response = requests.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    items = dom.find_all('div', {'class': 'vacancy-serp-item vacancy-serp-item_redesigned'})

for vac in hhru.find({}):
    pprint(vac)

