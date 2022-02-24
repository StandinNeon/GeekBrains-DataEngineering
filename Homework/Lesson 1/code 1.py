import requests
import json
url = "https://api.github.com/users/standinneon/repos" # Ссылка на API со списком репозиториев

response = requests.get(url) # Получение ответа от сервера
name = response.content # Запрос части, где содержится информация о репозиториях
jname = json.loads(name) # Приводим информация из типа bytes к JSON

for i in range(0, len(jname), 1): # Так как репозиторий не один, перебираем список из словарей
    print (jname[i].get("name")) # Выводим только имена репозиториев

# Запись JSON объекта в файл
'''
with open('repos.json', 'w') as outfile: 
    json.dump(jname, outfile)
'''