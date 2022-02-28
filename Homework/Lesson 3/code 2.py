from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['Vacancies']
hhru = db.hhru
salary = input('Enter minimum salary: ')

def sal_g(coll, sal):
    for vac in coll.find({'$or': [{'salary_from': {'$gte': 100000}}, {'salary_from': {'$lt': 100000}, 'salary_to': {'$gte': 100000}}]}):
        pprint(vac)
# Не получалось передать переменную в запрос, не понял как
sal_g(hhru, salary)
