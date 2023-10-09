# Задание 1
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Задание 2
def find_minimum(lst):
    if not lst:
        return None
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

# Задание 3
def count_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0
    for num in lst:
        if is_prime(num):
            count += 1
    return count

# Задание 4
def remove_number(lst, target):
    count_removed = lst.count(target)
    lst = [num for num in lst if num != target]
    return count_removed

# Задание 5
def merge_lists(list1, list2):
    return list1 + list2

# Задание 6
def calculate_powers(lst, power):
    return [num**power for num in lst]







