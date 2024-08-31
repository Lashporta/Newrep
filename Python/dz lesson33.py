def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# *****************************

def find_minimum(lst):
    return min(lst)

# *****************************

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(lst):
    count = 0
    for num in lst:
        if is_prime(num):
            count += 1
    return count

# ********************************

def remove_number(lst, number):
    original_length = len(lst)
    lst = [num for num in lst if num != number]
    removed_count = original_length - len(lst)
    return removed_count

# *********************************

def sum_lists(lst1, lst2):
    return lst1 + lst2

# **********************************

def raise_to_power(numbers, power):
    result = []
    for number in numbers:
        result.append(number ** power)
    return result

