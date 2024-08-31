def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_char(s):
    return len(s)

from string_utils import string_operations, string_analysis

user_input = input("Введите строку: ")

reversed_string = string_operations.reverse_string(user_input)
capitalized_string = string_operations.capitalize_words(user_input)
vowels_count = string_analysis.count_vowels(user_input)
char_count = string_analysis.count_char(user_input)

print("Перевёрнутая строка:", reversed_string)
print("Строка с заглавными буквами:", capitalized_string)
print("Количество гласных букв:", vowels_count)
print("Общее количество символов:", char_count)