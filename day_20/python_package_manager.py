import requests
import numpy as np
from bs4 import BeautifulSoup

# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# response = requests.get(romeo_and_juliet) # Error 404
# # words = response.json()
# print(response)

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)
result = response.json()

def statistics(weight):        
    class_marks = []
    frequencies = []
    for key, frequency in weight.items():
        lower, upper = map(int, key.split(' - '))
        class_marks.append((lower + upper) / 2)
        frequencies.append(frequency)

    mean = np.average(class_marks, weights=frequencies)

    cumulative_freq = np.cumsum(frequencies)
    total_freq = np.sum(frequencies)

    midpoint = (total_freq + 1) / 2

    index = np.argmax(cumulative_freq >= midpoint)

    if total_freq % 2 != 0:
        median = class_marks[index]
    else:
        lower_index = index - 1
        upper_index = index
        median = np.average(class_marks[lower_index:upper_index + 1], weights=frequencies[lower_index:upper_index + 1])

    std_dev = np.sqrt(np.average((class_marks - mean)**2, weights=frequencies))
    min_value = np.min(class_marks)
    max_value = np.max(class_marks)

    return mean, median, std_dev, min_value, max_value 


"""For Cats' Weight"""
weight = {}
for i in result:
    key =  i['weight']['metric']
    if key in weight:
        weight[key] += 1
    else:
        weight[key] = 1

mean, median, std_dev, min_value, max_value = statistics(weight) 
print(f'Weight; Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}\
, Min: {min_value}, Max: {max_value}')



"""Life Span """
weight = {}
for i in result:
    key =  i['life_span']
    if key in weight:
        weight[key] += 1
    else:
        weight[key] = 1

mean, median, std_dev, min_value, max_value = statistics(weight) 
print(f'Life_Span; Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}\
, Min: {min_value}, Max: {max_value}')



"""Country"""
country = {}
for i in result:
    key =  i['origin']
    if key in country:
        country[key] += 1
    else:
        country[key] = 1


"""Breed"""
breed = {}
for i in result:
    key =  i['name']
    if key in breed:
        breed[key] += 1
    else:
        breed[key] = 1

#print('{"Country": %s, "Breed": %s}'%(country, breed))


# countries_api = 'https://restcountries.eu/rest/v2/all'

# response = requests.get(countries_api) #Error
# result = response.json()

# print(result)

dataset = 'https://archive.ics.uci.edu/datasets'
response = requests.get(dataset)
content = getattr(response, 'content')
soup = BeautifulSoup(content, 'html.parser')

title = soup.title.string

print(title, soup.get_text())