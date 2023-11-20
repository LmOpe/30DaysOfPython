# Day 2: 30 Days of python programming

import math

"""Level 1"""

first_name = 'Muhammed'
last_name = 'Lawal'
full_name = 'Muhammed Lawal'
country = 'Nigeria'
city = 'Kwara'
age = 100
year = 2023
is_married = False
is_true = True
is_light_on = True
language, framework, database = 'Python', 'Django', 'Postgresql'


"""Level 2"""

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(language))
print(type(framework))
print(type(database))

print(len(first_name))

print(f'First_name: {len(first_name)}, Last_name: {len(last_name)}')

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = math.pi * (30 ** 2)
circum_of_circle = 2 * math.pi * 30
radius = input('Input the value of the radius: ')
area_of_circle = math.pi * (int(radius) ** 2)

first_name = input('Enter the first name: ')
last_name = input('Enter the last name: ')
country = input('Enter the country: ')
age = input('Enter the age: ')

print(help('keywords'))