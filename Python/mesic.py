
month = input("Введите номер месяца 1-12: ")

if month.isdigit():
    month_number = int(month)
    if 1 <= month_number <= 12:
        if month_number in [1, 2, 12]:
            print('Winter')
        elif month_number in [3, 4, 5]:
            print('Spring')
        elif month_number in [6, 7, 8]:
            print('Summer')
        elif month_number in [9, 10, 11]:
            print('Autumn')
    else:
        print('Введите правильный номер месяца от 1-12')
else:
    print('Введите правильный номер месяца')