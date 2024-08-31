# Константы пишутся с большой буквы
# PI = 3.14
# GRAVITY = 9.81
# MAX_CONNECTIONS = 100


# Использование констант в функциях и выражениях
# def calculate_circle_area(radius):
#     return PI * (radius ** 2)
#
#
# def calculate_free_fall_time(height):
#     return (2 * height / GRAVITY) ** 0.5
#
#
# print('Circle area with radius 5:', calculate_circle_area(5))
# print('Time to fall from height 20m:', calculate_free_fall_time(20))
# print('Maximum allowed connections:', MAX_CONNECTIONS)


# strings = {10: 'apple', 2: 'pear', 3: 'banana', 4: 'grape', 5: 'strawberry'}
#
# print(strings[10])
# print(strings[3])
#
# # добавление элементов
#
# strings[6] = "fig"
# # используется remove при работе со списками а del при работе со словарем
# del strings[4]
# print(strings)

# fruits = ["apple", "banana", "cherry", "strawberry"]
# Перебор элементов списка

# for fruit in fruits:
#     print(fruit)

# Исходный словарь
# fruit_inventory = {10: 'apple', 20: 'banana', 15: 'grape', 5: 'strawberry', 8: 'mango'}

# Перебор элементов словаря
# for key,fruit in fruit_inventory.items():
#     print(f'There are {key} {fruit}')
#
# print(fruit_inventory)

# for fruit in fruit_inventory.values():
#     print(fruit)
#
# frut_list = list(fruit_inventory.values())
# print(frut_list)
#
# for key in fruit_inventory.keys():
#     print(key)

# как обращаться к файлу!!!!!!!!!!!!!!!!!!!!!!!

# Просто чтение файла
# with open('./TXT/test.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
# # добавление текста с удалением существующего текста в файле
# with open('./TXT/test.txt', 'w') as file:
#     file.write('Hello World')
#
# # добавление текста в конец файла
# with open('./TXT/test.txt', 'a') as file:
#     file.write(' ' 'Appending text.')
#
# # - чтение с добавлением
# with open('./TXT/test.txt', 'r+') as file:
#     file.write(' ' 'Add text')

import json

fruit_inventory = {'apple': 10, 'banana': 20, 'cherry': 15, 'date': 5, 'orange': 8}

# Преобразование словаря в json строку
# fruit_inventory_json = json.dumps(fruit_inventory, indent=4)
# print(fruit_inventory_json)

# Запись json строки в файл
# with open('./TXT/fruit_inventory.json', 'w') as json_file:
#     json.dump(fruit_inventory, json_file, indent=4)

# Чтение из файла json
# with open('./TXT/fruit_inventory.json', 'r') as json_file:
#     loaded_fruit_inventory = json.load(json_file)
# print(loaded_fruit_inventory)
