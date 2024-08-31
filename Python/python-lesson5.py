# # isdigit()
#
# string1 = '12345'
# string2 = '123a45'
# string3 = '456467'
# string4 = '235 325'
#
# print('string1', string1.isdigit())
# print('string2', string2.isdigit())
# print('string3', string3.isdigit())
# print('string4', string4.isdigit())

#
# inNumber = input("Введите данные")
#
# if inNumber.isdigit():
#     number = int(inNumber)
#     print(f'You eneter number, {number}' )
# else:
#     print('Enter correct number')
#
# number = 12345
#
# number_str = str(number)
#
# first_digit = number_str[0]
#
# print(first_digit)
#
# last_digit = number_str[-1]
#
# print(last_digit)

number = '0123456789'


number_str = str(number)

numbers_str = input('Введите 10 значное число')

if len(numbers_str) == 10 and number_str.isdigit():
    print('Введено 10 значное число.')
    for number in numbers_str:
        print(number)
else:
    print('Некорректный ввод')











