from collections import Counter

from countries import countries
from countries_data import data

for i in range(11):
    print(i)

i = 10
while i > 0 or i == 0:
    print(i)
    i-=1

for i in range(7):
    j = 0
    while j < i or j == i:
        print("#", end='')
        j+=1
    print("\n")
print("\n")
for i in range(8):
    for n in range(8):
        print("#", end=" ")
    print("\n")

for i in range(11):
    for n in range(1):
        print(f'{i} x {i} = {i * i}')

stack = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in stack:
    print(i)

for i in range(0, 101, 2):
    print(i)

for i in range(0, 101, 1):
    print(i)
    
sum = 0
for i in range(101):
    sum+=i
print(sum)

even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i
print(f"The sum of all evens is {even}. And the sum of all odds is {odd}.")

countries = countries
for i in countries:
    if "land" in i:
        print(i)

fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(2):
    if(i < (len(fruits)/2)):
        temp = fruits[len(fruits)-i-1]
        fruits[len(fruits)- i-1] = fruits[i]
        fruits[i] = temp
print(fruits)

languages = [language for country in data for language in country['languages']]

print(len(set(languages)))

counter = Counter(languages)

most_common = counter.most_common(10)

print(most_common)

sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)

top_10 = sorted_countries[:10]

for i, country in enumerate(top_10, start=1):
    print(f"{i}. {country['name']} - Population: {country['population']}")