a = True
b = False

print(a and b)
print(a or b)
print(not a)

username = 'user'
password = 'pass'

input_username = input('Enter login: ')
input_password = input('Enter password: ')

is_username_correct = input_username == username
is_password_correct = input_password == password

if is_username_correct and is_password_correct:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

age = int(input("Введите Ваш возраст: "))

if age < 18:
    print('Вы несовершеннолетний')
elif age < 65:
    print('Вы совершеннолетний')
else:
    print('Вы старпер')

score = int(input("Введите ваш счет: "))

if score >= 100:
    print('Вы выиграли')
else:
    print('Попробуйте еще')

a = 10
b = 3

user_input = input("Пожалуйста, введите целое число: ")

if user_input:
    number = int(user_input)
    print(f"Спасибо, вы ввели число {number}")
else:
    print("Вы ввели некорректное значение. .")

a = float(input("Введите первое число: "))

b = float(input("Введите второе число: "))

operation = input("Введите операцию: '+', '-', '*', '/':")

if operation == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print('На ноль делить нельзя')
else:
    print("Невозможно выполнить.")

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")

    year = int(input("Пожалуйста, введите год: "))

    if year % 4 != 0:
        print(f"{year} не является високосным годом.")
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} является високосным годом.")
            else:
                print(f"{year} не является високосным годом.")
        else:
            print(f"{year} является високосным годом.")


cislo1 = float(input("Введите первое число: "))
cislo2 = float(input("Введите второе число: "))

maximum = max(cislo1, cislo2)

print(f"Максимум из двух чисел: {maximum}")