string = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string)

string = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(string)

company = 'Coding For All'

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])

print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

print('Python for Everyone'.replace('Everyone', 'All'))

print(company.split(' '))

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

print(company[0])

print(len(company) - 1)

print(company[10])

abbr = [word[0] for word in company.split(' ')]
print(''.join(abbr))

print(company.index('C'))

print(company.index('F'))

print(company.rfind('l'))

print('You cannot end a sentence with because because because is a conjunction'.index('because'))

print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

print('You cannot end a sentence with because because because is a conjunction'[31:54])

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print('You cannot end a sentence with because because because is a conjunction'[31:54])

print(company.startswith('Coding'))

print(company.endswith('coding'))

print('   Coding For All      ' .strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

print(('# ').join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print('I am enjoying this challenge. \nI just wonder what is next.')

print(f'Name\t\tage\tCountry\t\tCity\nAsabeneh\t{250}\tFinland\t\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

print('{} + {} = {}'.format(8, 6, 8+6))
print('{} - {} = {}'.format(8, 6, 8-6))
print('{} * {} = {}'.format(8, 6, 8*6))
print('{} / {} = {:.2f}'.format(8, 6, 8/6))
print('{} % {} = {}'.format(8, 6, 8%6))
print('{} // {} = {}'.format(8, 6, 8//6))
print('{} ** {} = {}'.format(8, 6, 8**6))