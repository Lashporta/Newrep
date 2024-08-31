# def greet():
#     print("Hello1 World!")
#     print("Hello2 World!")
# print("Hello3 World!")
#
# print(greet())

# Пример фкнкции с аргументами
# def greet(name = 'Guest'):
#     print(f"Hello , {name}!")
#
#
# list = ["Alena", "Serg", "Anton", "Elena", "Ilona"]
#
# for name in list:
#     greet(name)

# функция с параметрами по умолчанию
# def greet(name = 'Guest', lastname = ' '):
#     print(f'Hello {name}, welcome to my {lastname}!')
# greet()
# greet('Guest', '')


# Функция с возвращением значения
# def add(a,b):
#     sum=a+b
#     return sum
#
# result=add(1,2)
# print(result)

#Область видимости переменных

x = 10  # Глобальная переменная

# def print_value():
#     x = 5  # Локальная переменная
#     print(x)
#
# print_value()
# print(x)

# Ключевое слово global чтобы использовать глоб переменную внутри функции

# def change_value():
#     global x
#     x = 5
# change_value()
# print(x)

# list = ["Alena", "Serg", "Anton", "Elena", "Ilona"]
# list.append("")
# def greet(name = 'Guest'):
#     print(f"Hello , {name}!")
#
# for name in list:
#     if name != "":
#         greet(name)
#     else:
#         greet()
#         names_list = ["Alena", "Serg", "Anton", "Elena", "Ilona"]
#         names_list.append("")
#
#         count = 0
#
#
#         def greet(name='Guest'):
#             global count
#             count += 1
#             print(f"Hell")

















