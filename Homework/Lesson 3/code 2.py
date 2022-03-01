from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['Vacancies']
hhru = db.hhru
salary = int(input('Enter minimum salary: '))

def sal_g(coll, sal):
    for vac in coll.find({'$or': [{'salary_from': {'$gte': sal}}, {'salary_from': {'$lt': sal},
                                                                    'salary_to': {'$gte': sal}}]}):
        pprint(vac)
sal_g(hhru, salary)
