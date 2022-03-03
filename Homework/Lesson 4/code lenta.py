import requests
from lxml import html
import re
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient('127.0.0.1', 27017)
db = client['News']
news = db.news

base_url = 'https://lenta.ru'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/98.0.4758.102 Safari/537.36'}
response = requests.get(base_url, headers=header)
dom = html.fromstring(response.text)
items = dom.xpath("//a[@class = 'card-mini _topnews']")

items_added = 0
items_not_added = 0
news_len = 0

for item in items:
    item_data = {}
    item_data['title'] = item.xpath(".//span/text()")[0]
    link = item.xpath('./@href')[0]
    item_data['date'] = item.xpath('.//time/text()')[0]
    if 'http' not in link:
        link = base_url + link
    item_data['source'] = re.search(r'/{2}[^/]{1,}/{1}',link)[0].replace('/','')
    item_data['_id'] = ''.join(re.findall(r'[a-z,0-9]{1,}', link))
    item_data['link'] = link

    try:
        news.insert_one(item_data)
        items_added += 1
    except DuplicateKeyError:
        items_not_added += 1

for vac in news.find({}):
    news_len += 1
print(f'In collection news {news_len} objects')
print(f'Added {items_added} objects')
print(f'Don\'t added {items_not_added} objects')
