from countries import countries
# Level 1

empty_list = []
lists = [3, 9, 'a', 'd', 6, 'hello', 'f']
print(len(lists))
print(lists[0], lists[3], lists[-1])
mixed_data_types = ['Muhammed', 15, 1.75, 'single', 'Tanke, Ilorin']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies[-2] = "ORACLE"
print(it_companies)
it_companies.append('Netflix')
it_companies.insert(4, 'HP')
it_companies[0] = 'FACEBOOK'
print('#'.join(it_companies))
print('Amazon' in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[:-4:-1])
print(it_companies[-5:-6:-1])
it_companies.pop()
del it_companies[3:5]
it_companies.pop(-1)
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(-3, 'Python')
full_stack.insert(-3, 'SQL')
print(full_stack)

# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print(ages)
median = 0
medians = []
if(len(ages) % 2 == 0):
    medians.append(ages[(len(ages) // 2) - 1])
    medians.append(ages[len(ages) // 2])
    median = sum(medians) // 2
else:
    median = ages[(len(ages) // 2) - 1]

print(median)

average = sum(ages) // len(ages)
print(average)

range = max(ages) - min(ages)

print(f'(min - average): {abs(min(ages) - average)}, (max - average): {abs(max(ages) - average)}')

print(countries[len(countries) // 2])

first_half_countries = countries[:97]
second_half_countries = countries[97:]

print(first_half_countries)
print(second_half_countries)

china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic)