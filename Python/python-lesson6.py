number = input("Введите шестизначное число: ")
number_str = str(number)
if number.isdigit() and len(number) != 6:
    new_number = number_str[6] + number_str[2] + number_str[3] + number_str[4] + number_str[5] + number_str[1]
    print(f"Результат:")
