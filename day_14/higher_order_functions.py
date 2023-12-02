from functools import reduce
from collections import Counter
from operator import itemgetter

from countries import countries as countries_list
from countries_data import data

# The map function takes in a list and a function,
# it uses each item in the list or iterable to call the function
# and returns a list of values from each call.

# Filter function also takes in a function which returns a boolean value
# and an iterable as arguments, it calls the function with each item in the 
# iterable and returns only the items which when the function is called with
# it returns true.

# Reduce function takes also a function and an iterable but uses the function
# to reduce the list into a single value.

# A higher order function is a function that takes
# another function as argument

# Closure is a concept in Python in which a child function
# have access to it parent's outer scope

# Decorator is a design pattern that allows users to change the behaviour
# of a function

def map_func(func, iterable):
    new_lists = []
    for i in iterable:
        new_lists.append(func(i))
    return new_lists

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map_func(int, numbers_str)
print(list(numbers_int))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

def change_to_upper(country):
    return country.upper()

countries_upper = map(change_to_upper, countries)
print(list(countries_upper))

def square(number):
    return number ** 2

squared_number = map(square, numbers)

print(list(squared_number))

names_upper = map(change_to_upper, names)

print(list(names_upper))

countries_with_land = filter(lambda x: 'land' in x, countries)
print(list(countries_with_land))

countries_with_six_chars = filter(lambda x: len(x) == 6, countries)

print(list(countries_with_six_chars))

countries_with_six_chars_and_more = filter(lambda x: len(x) >= 6, countries)

print(list(countries_with_six_chars_and_more))

countries_with_e = filter(lambda x: x.startswith('E'), countries)

print(list(countries_with_e))

squared_number_less_than_81 = filter(lambda x: x < 81, map(square, numbers))

print(list(squared_number_less_than_81))

def get_string_lists(lists):
    strings = filter(lambda x: isinstance(x, str), lists)
    return strings

lists = [6, 1, 'HI', 'Get']

print(list(get_string_lists(lists)))

def add_two_numbers(x, y):
    return x + y

numbers_sum = reduce(add_two_numbers, numbers)

print(numbers_sum)

def concat(str1, str2):
    return f'{str1}, {str2}'

concatenated_str = reduce(concat, countries)

print(concatenated_str)

def categorize_countries(countries_list):
    countries_ = [country for country in countries_list if 'land' in country]
    return countries_

print(categorize_countries(countries_list))

def country_dict(country_list):
    initial_counts = Counter(country[0].upper() for country in country_list)
    return initial_counts

print(country_dict(countries_list))

def get_first_ten_countries(countries_list):
    return countries_list[:10]
    
print(get_first_ten_countries(countries_list))

def get_last_ten_countries(countries_list):
    return countries_list[-10:]

print(get_last_ten_countries(countries_list))

'''Sort by name'''
countries_by_name = sorted(data, key=itemgetter('name'))

'''Sort by capital'''
countries_by_capital = sorted(data, key=itemgetter('capital'))

'''Sort by population'''
countries_by_population = sorted(data, key=itemgetter('population'), reverse=True)



languages = [lang for country in data for lang in country['languages']]
language_count = Counter(languages)

most_spoken_languages = language_count.most_common(10)

sorted_countries_by_location = sorted(most_spoken_languages, key=lambda x: x[0])



most_populated_countries = sorted(data, key=itemgetter('population'), reverse=True)[:10]

print(most_populated_countries)