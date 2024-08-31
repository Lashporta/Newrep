number = input("Введите двухзначное число: ")
if len(number) == 2 and number.isdigit():
    print(number[0])
    print(number[1])
else:
    print("неправильный ввод, введите двузначное число.")


number = input("Введите трехзначное число: ")
if len(number) == 3 and number.isdigit():
    print(number[0])
    print(number[1])
    print(number[2])
    print(int(number[0]) + int(number[1]) + int(number[2]))
else:
    print("неправильный ввод,введите трехзначное число.")


first = input("Введите первую цифру: ")
second = input("Введите вторую цифру: ")
if first.isdigit() and second.isdigit():
    print(int(first + second))
else:
    print("неправильный ввод, введите цифровое значение.")


cels = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = (celsius * 9/5) + 32
print("Temp fahr.:", fahrenheit)