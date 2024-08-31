# практ задание def square(number): эта функция принимает функцию и возвращает его в квадрат
# создать список из 5 чисел
# вызвать функцию def square для каждого числа из списка и вывести на экран
# def square(number):
#     return number ** 2
#
# spisok = [1, 2, 3, 4, 5]
#
# for number in spisok:
#     result = square(number)
#     print(result)

# numbers = [1, 2, 3, 4, 5]


# def ctn(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             print(f" {number} четное.")
#         else:
#             print(f" {number} нечетное.")
#         print(number)
# ctn(numbers)
# strings = ["Nuts", "Engine", "Dataaaaaaaaa", "Result", "Allow"]
#
#
# def string_length(s):
#     return len(s)
#
#
# for string1 in strings:
#     length = string_length(string1)
#     print(f"Длина строки '{string1}' равна {length}")

operation = input("Введите операцию: '+', '-', '*', '/':")

def calculate(a, b, simbol):
    simbols = ['+', '-', '*', '/']
    if simbol == '+':
        result = a + b
    elif simbol == '-':
        result = a - b
    elif simbol == '*':
        result = a * b
    else:
        result = a / b
    return result

a = float(input('Enter  number: '))
s = input('Enter symbol: ')
b = float(input('Enter  number: '))

calculate(a, b, s)
print(calculate(a, b, s))

