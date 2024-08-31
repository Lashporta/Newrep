# целые числа int
# a = 1
# b = -5
# c = 0
# c плавающей точкой float
# x = 3.14
# y = -2.5
# z = 0.0
#
# a = 10
# b = 3
#
# # Сложение
# sum = a + b
#
# # вычетание
# difference = a - b
#
# # умножение
# product = a * b
#
# # деление
# quotient = a / b
#
# # целочисленное деление
# integer_division = a // b
#
# # остаок от деления
# remainder = a % b
#
# # возведение в степень
# power = a ** b
#
#
# print(sum, difference, product, quotient, integer_division, power, remainder)
# print(sum, difference, product, quotient, integer_division, remainder)
# name = 'ItStep'
# print('hello', name)
#
# # def- мы этим задаем название фкнкции
# def print_hi(login, password):
#     print(f'login {login}')
#     print(f'password: {password}')
#     print('-------------------------')
#
#
# print_hi('test', 'password')
# print_hi('1111', '22222')
# print_hi('222', '33333')

# # округление
# rounded = round(3.1423432, 2)
#
# # минимум и макcимум
# minimum = min(1, 2, 3, 4, 5)
# maximum = max(1, 2, 3, 4, 5)
#
# # сумма элементов
# total = sum([1, 11, 30])
# print(total)

# name = 'Alice'
# age = 30
#
# res = 'Hello ' + name + '!' + 'your age' + str(age)
# res2 = f'Hello, {name}! your age  {age}'
# print(res)
# print(res2)
#
# # Использование арифм выраж внутри f-строки
# a = 5
# b = 10
# result = f'Сумма {a} + {b} равна {a+b}'
# print(result)
#
# # Перенос на другую строку
# print('Использование\nарифм выраж\nвнутри f-строки')

a = 10
b = 20

sum = a + b
result = f'Сумма {a} + {b} = {a+b}'
print(result)

dif = a - b
difference = f'Вычетание {a} - {b} = {a-b}'
print(difference)

split = a / b
splitd = f'Деление {a} / {b} = {a/b}'
print(splitd)


value = float(input('Введите значение: '))
percentage = float(input('Введите процент: '))

result = (value * percentage) / 100

print(f'{percentage}% от {value} = {result}')



