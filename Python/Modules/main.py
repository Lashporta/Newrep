# import python_module

# python_module.greet('1')

# from python_module import greet_1
# greet_1('man')

# Если модуль нахолится в другой папке то мы обращаемся к нему так foldername.module

# import random
# import datetime
#
# random_number = random.randint(1, 100)
# print(random_number)
#
# current_datetime = datetime.datetime.now()
# print(f"Текущая дата и время {current_datetime}")

import python_module

# from python_module import summ, minus, umn
#
# print(summ(23, 2))
# print(minus(56, 2))
# print(umn(15, 2))

import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Информация о пользователе GitHub")
    print(f"Логин: {data['login']}")
    print(f"ID: {data['id']}")
    print(f"blog: {data['blog']}")
    print(f"URL профиля: {data['html_url']}")
    print(f"Количество публичных репозиториев: {data['public_repos']}")
else:
    print(f"Ошибка при получении данных: {response.status_code}")




