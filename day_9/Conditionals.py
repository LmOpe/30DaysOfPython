age = int(input("Enter you age: "))
if(age > 18  or age == 18):
    print("You are old enough to drive.")
else:
    print(f'You need {18 - age} more years to learn to drive.')

your_age = int(input("Enter your age: "))
my_age = 18
if(your_age > my_age):
    print(f'You are {your_age - my_age} year older than me') \
        if your_age - my_age == 1 else \
            print(f"Your are {your_age - my_age} years older than me")
elif(my_age > your_age):
        print(f'I am {my_age - your_age} year older than you') \
        if my_age - your_age == 1 else \
            print(f"I am {my_age - your_age} years older than you")
else:
    print("We are agemates")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if(a > b):
    print(f"{a} is greater than {b}")
elif(a < b):
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

score = int(input("Enter your score: "))
if(score == 80 or score > 80 and score < 101):
    print(f"Your grade is A")
elif(score == 70 or score > 70 and score < 79):
    print(f"Your grade is B")
elif(score == 60 or score > 60 and score < 69):
    print(f"Your grade is C")
elif(score == 50 or score > 50 and score < 59):
    print(f"Your grade is D")
elif(score == 0 or score > 0 and score < 49):
    print(f"Your grade is F")

autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input("Enter a month: ")
if(month in autumn):
    print("The season is Autumn")
elif(month in winter):
    print('Season is winter')
elif(month in spring):
    print("Season is Spring")
elif(month in summer):
    print("Season is Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter fruit's name: ")
if(fruit in fruits):
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(f"The modified list is: {fruits}")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if('skills' in person):
    print(person['skills'][2:3])
if('skills' in person):
    if("Python" in person['skills']):
        print("Python" in person['skills'])
if(person['skills'] == ['Javascript', 'React']):
    print('He is a front end developer')
elif(person['skills'] == ['Node', 'Python', 'MongoDB']):
    print('He is a backend developer')
elif('React' in person['skills'] and \
    'Node' in person['skills'] and 'MongoDB' in person['skills']):
    print('He is a fullstack developer')
else:
    print('unknown title')

if(person['is_marred'] == True and person['country'] == 'Finland'):
    print(f'{person["first_name"] + " " + person["last_name"] + " " + "lives in " + person["country"] + ". " + "He is married."}')