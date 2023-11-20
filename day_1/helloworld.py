import sys
import math

"""Level 2"""

"""1"""
# Checking Python Version
print(sys.version)

"""2"""
# Basic Math Operations
print(3+4)
print(4-3)
print(4*3)
print(4%3)
print(4/3)
print(4**3)
print(4//3)

"""3"""
# Writing Strings
print('Muhammed')
print('Lawal')
print('Nigeria')

"""4"""
# Checking Data Types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Muhammed'))
print(type('Lawal'))
print(type('Nigeria'))



"""Level 3"""
"""1"""

3 # Integer
4.5 # Float
3-5j # Complex
'Lawal' # String
True # Boolean
[3, 5, 9] # List
(4, 9, 2) # Tuple
{2, 6, 1} # Set
{'Name': 'Muhammed', 'Country': 'Nigeria'} # Dictionary


"""2 --> Euclidean Distance"""

square1 = pow((10-2), 2)
square2 = pow((8-3), 2)

sumOfSquares = square1 + square2

distance = math.sqrt(sumOfSquares)

print(f'The Euclidian distance between (2, 3) and (10, 8) is {distance}')