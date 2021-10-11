#1 Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ), получите текущий курс валют и запишите его в TXT-файл в таком формате:

import requests
url = 'https://bank.gov.ua/NBU_Exchange/exchange?json?valcode=UAH&date=12.10.2005'
response = requests.request('GET', url)

if 200 >= response.status_code < 300:
    with open('course.txt', 'wt') as file:
        file.write(response.text)