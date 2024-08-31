def den(day_number):
    nedel = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    if 1 <= day_number <= 7:
        print(nedel[day_number - 1])
    else:
        print("число от 1 до 7.")


user_input = int(input("Введите номер дня недели (1-7): "))
den(user_input)


# **************************************

# Задание 2
def mesic(month_number):
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']

    if 1 <= month_number <= 12:
        print(months[month_number - 1])
    else:
        print("Введите число от 1 до 12.")


user_input = int(input("Введите номер месяца (1-12): "))
mesic(user_input)


# ***************************************************
def numb(number):
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")


user_input = float(input("Введите число: "))
numb(user_input)


# ****************************************

def sravnenie(numb1, numb2):
    if numb1 == numb2:
        print("Числа равны.")
    else:
        else_numbers = sorted([numb1, numb2])
        print("Числа в порядке возрастания:", *else_numbers)


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sravnenie(num1, num2)


# ********************

def lucky_number(number):
    if len(str(number)) != 6:
        print("Введите шестизначное число.")

        
