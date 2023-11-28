import math
import cmath  


def add_two(a, b):
    return a+b

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    sum = 0
    for arg in args:
        if(isinstance(arg, int)):
            sum += arg
        else:
            print("Please enter numbers only")
    return sum

print(add_all_nums(5, 8, 9, 3))

def convert_celsius_to_fahrenheit(c):
    return (c* (9/5)) + 32

def check_season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']

    if(month in autumn):
        return 'Autumn'
    elif(month in winter):
        return 'Winter'
    elif(month in spring):
        return 'Spring'
    elif(month in summer):
        return 'Summer'

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("The x-coordinates must be different to calculate slope.")
    slope = (y2 - y1) / (x2 - x1)
    return slope

def solve_quadratic_eqn(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        root1 = (-b + (discriminant ** 0.5)) / (2 * a)
        root2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        complex_root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        complex_root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return complex_root1, complex_root2

print(solve_quadratic_eqn(1, -3, 2))

def print_list(a):
    [print(item) for item in a]

print_list([2, 8, 6, 4, 9])

def reverse_list(lists):
    for i in range(len(lists)):
        if(i < (len(lists)/2)):
            temp = lists[len(lists)-i-1]
            lists[len(lists)- i-1] = lists[i]
            lists[i] = temp

    return lists

print(reverse_list([1, 2, 3, 4, 5, 6]))

def capitalize_list(a):
    for i in range(len(a)):
        a[i] = a[i].capitalize()
    return a

print(capitalize_list(["muhammed", 'opeyemi', 'lawal']))

def add_item(lists, item):
    lists.append(item)
    return lists

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

def remove_item(lists, item):
    lists.remove(item)
    return lists

print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))

def sum_of_numbers(num):
    if num == 1:
        return 1
    else:
        return sum_of_numbers(num - 1) + num

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odd(num):
    sum = 0
    for i in range(num + 1):
        if not i % 2 == 0:
            sum += i
    return sum

def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_of_odd(5), sum_of_even(5))

def evens_and_odds(num):
    if(num % 2 == 0):
        print(f"The number of odds are {int(num / 2)}")
        print(f"The number of evens are {int((num / 2) + 1)}")
    else:
        print(f"The number of odds are {int(num / 2) + 1}")
        print(f"The number of evens are {int((num / 2))}")

evens_and_odds(100)

def factorial(num):
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num

print(factorial(4))

def is_empty(a):
    if not a:
        return True
    else:
        return False


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[n // 2]


def calculate_mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes if modes else None  # Return None if there is no mode


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diff) / len(numbers)


def calculate_std(numbers):
    import math
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

print(calculate_variance([5,9,8, 6, 7]))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(5))

def unique(lists):
    return len(lists) == len(set(lists))

print(unique([5, 3, 4, 8]))

def same_datatype(lists):
    for i in range(len(lists)):
        if type(lists[i]) != type(lists[0]):
            return False
    return True

print(same_datatype([5, 3, 4, 8, 'Hi']))

def valid_variable(var):
    if var.isidentifier():
        return True
    return False

print(valid_variable('helle'))

from countries_data import data
from collections import Counter

def most_spoken_languages():
    languages = [language for country in data for language in country['languages']]
    counter = Counter(languages)
    most_common = counter.most_common(20)
    most_common.reverse()
    return most_common

print(most_spoken_languages())

def most_populated_countries():
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    top_10 = sorted_countries[:10]
    reversed_countries = []

    for i, country in enumerate(top_10, start=1):
        reversed_countries.append(country['name'])
    reversed_countries.reverse()

    return reversed_countries

print(most_populated_countries())