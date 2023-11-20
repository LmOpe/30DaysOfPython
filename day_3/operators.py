# Day 3: 30 Days of python programming

import math

age = 20
height = 1.72
complex_num = 3 + 2j

# Area of a Triangle
base = input("Enter base: ")
height_triangle = input('Enter height: ')
area = 0.5 * int(base) * int(height_triangle)
print('The area of the triangle is', int(area))

# Perimeter of a triangle
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print('The perimeter of the triangle is', perimeter)

# Area and perimeter of a rectangle
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
perimeter = 2 * (length + width)
print(f'Area of the rectangle is: {area}, peimeter is: {perimeter}')

# Area of a circle
radius = float(input('Enter radius: '))
pi = 3.14
area = pi * (radius ** 2)
circumference = 2 * pi * radius
print(f'Area of the circle is: {area}, circumference is: {circumference}')

"""Calculating Slope"""
# Equation --> y = 2x - 2
# From y = mx + b
# Slope y = m = 2
# X-intercept --> if y = 0, x = 1 ==> (1, 0)
# Y-intercept --> if x = 0, y = -2 ==> (0, -2)

"""Calculating slope and Euclidean distance between two points"""
# Slope m = (y2 - y1)/(x2 - x1)
y_1 = 2
y_2 = 10
x_1 = 2
x_2 = 6

m = (y_2 - y_1)/(x_2 - x_1)

square_1 = (x_2 - x_1) ** 2
square_2 = (y_2 - y_1) ** 2

sum_of_squares = square_1 + square_2
distance = math.sqrt(sum_of_squares)

print(f'Slope is {m}, Distance is {distance}')


print(f'Slope in task 8 is {2}, slope in task 9 is {m}')

# Quadratic Equation
# y = (x**2) + 6(x) + 9
# y = (x**2 + 3x) + (3x + 9)
# y = x(x + 3) + 3(x + 3)
x_1, x_2, x_3 = -3, 0, 1
y_1 = (x_1**2) + 6*x_1 + 9
y_2 = (x_2**2) + 6*x_2 + 9
y_3 = (x_3**2) + 6*x_3 + 9
print(f'x1 = {x_1}, y1 = {y_1}, x2 = {x_2}, y2 = {y_2}, x3 = {x_3}, y3 = {y_3}')
print('y = is 0 when x = {x_1}')

"""Comparison"""
print(len('python') != len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon.')
print('on' not in 'python' and 'on' not in 'dragon')
length = len('python')
print(f'Length in float: {float(length)}, length in string: {str(length)}')

even, odd = 6, 9
is_even = (even % 2) == 0
is_odd = (odd % 2) != 0
print(f'{even} is even: {is_even}, {odd} is odd: {is_odd}')

is_equal = 7//3 == int(2.7)
print(f'7//3 is equal to int(2.7): {is_equal}')

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
pay = int(hours) * int(rate_per_hour)
print('Your weekly earning is', pay)

years = input('Enter number of years you have lived: ')
seconds_per_year = 31536000
print(f'You have lived for {int(years) * seconds_per_year} seconds.')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')