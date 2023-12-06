import re
import json
from collections import Counter
from operator import itemgetter

def line_and_word_count(file):
    text = file.read()
    regex_pattern = r'[ .]'
    words = re.split(regex_pattern, text)
    word_list = list(filter(lambda x: x != '', \
    words))
    word_count = len(word_list)

    lines = text.splitlines()
    line_count = len(lines)

    return word_count, line_count

def file_reader(name):
    with open(f'./day_19/data/{name}.txt') as f:
        num_of_word, num_of_lines = line_and_word_count(f)
        print(f'Number of lines in {name} is: {num_of_lines}, \
Number of words in {name} is {num_of_word}.')

file_reader('obama_speech')
file_reader('michelle_obama_speech')
file_reader('donald_speech')



def most_spoken_languages(filename, number):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        languages = [lang for country in data for lang in country['languages']]
        language_count = Counter(languages)

        most_spoken_languages = language_count.most_common(number)

    return most_spoken_languages

print(most_spoken_languages('./day_19/data/countries_data.json', 3))

def most_populated_countries(filename, number):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        most_populated_countries = sorted(data, key=itemgetter('population'), reverse=True)[:number]
        countries_list = []
        for i in most_populated_countries:
            countries_list.append({'country': i['name'], 'population': i['population']})

        return countries_list

print(most_populated_countries('./day_19/data/countries_data.json', 3))


with open('./day_19/data/email_exchanges_big.txt') as f:
    data = f.read()
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    addresses = re.findall(email_pattern, data)
    print(addresses[:5])

def find_most_common_words(file, number):
    data = file.read()
    regex_pattern = r'[ .,\n!?]'
    words = re.split(regex_pattern, data)
    most_common_words = Counter(list(filter(lambda x: x != '', \
        words))).most_common(number)

    return most_common_words

def most_common_words_reader(filename, number):
    with open(f'./day_19/data/{filename}.txt') as f:
        print(find_most_common_words(f, number))

most_common_words_reader('obama_speech', 10)
most_common_words_reader('michelle_obama_speech', 10)
most_common_words_reader('donald_speech', 10)
most_common_words_reader('melina_trump_speech', 10)

most_common_words_reader('romeo_and_juliet', 10)

with open('./day_19/data/hacker_news.csv') as f:
    data = f.read().splitlines()

    # For Python
    counter = 0
    for i in data:
        matches = re.sub(',', ' ', i)
        if bool(re.search(r'\bpython\b', matches, re.I)):
            counter+=1
    
    print(f'The number of lines containing python or Python is {counter}')


    # For Javascrit
    counter = 0
    for i in data:
        js_matches = re.sub(',', ' ', i)
        if bool(re.search(r'\bjavascript\b', js_matches, re.I)):
            counter+=1
    
    print(f'The number of lines containing  JavaScript, \
javascript or Javascript is {counter}')


    # For Java
    counter = 0
    for i in data:
        java_matches = re.sub(',', ' ', i)
        if bool(re.search(r'\bJava\b', java_matches)):
            counter+=1
    
    print(f'The number of lines containing Java is {counter}')