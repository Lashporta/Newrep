# try:
# 	x = 10
# 	y = 0
# 	result = x / y
# except ZeroDivisionError:
# 	print('Деление на ноль')
# finally:
# 	print('Всегда выовдить эту строку')
from re import split
from symbol import yield_arg

# try:
#     file = open('./TXT/txt1.txt')
#     content = file.read()
#     print(content)
# except FileNotFoundError as peremennaya:
#     print(f'Файл не найден {peremennaya}')
# finally:
#     try:
#         file.close()
#         print('Файл закрыт')
#     except NameError :
#         print('Файл не был открыт и работа завершена')

# def check_positive(number):
#     if number < 0:
#         raise ValueError("Число отрицательное")
#
#
# try:
#     check_positive(-10)
# except ValueError as e:
#     print(e)

def check_positive(number):
    if number == 0:
        raise ZeroDivisionError('У нас ноль')

a = 10 / 0
try:
    # check_positive(0)
    a = 10 / 0
except ZeroDivisionError as nasheSoobshenie:
    print(f'Возникла ошибка {nasheSoobshenie}')


