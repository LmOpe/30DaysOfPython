import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = bs(content, 'html.parser')



with open('./day_22/bu_data.json', 'a', encoding='utf-8') as f:
    json.dump(dict(body = soup.body), f, ensure_ascii=False, indent=4)



url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url) # Error
content = response.content
soup = bs(content, 'html.parser')

print(soup.title)


url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content # we get all the content from the website
soup = bs(content, 'html.parser')
tables = soup.find_all('table')
table = tables[0]
rows = table.find('tbody').find_all('tr')
row_data = {}
counter = 0
for row in rows:
    if counter == 0:
        counter += 1
        continue
    data = row.find_all('td')
    number = row.find('th').text.strip()
    row_data[str(number)] = {'Name': data[1].text.strip(),\
        'Term': data[2].text.strip(), 'Party': data[4].text.strip(), \
        'Election': data[5].text.strip(), 'Vice President': data[6].text.strip()}
    counter += 1


with open('./day_22/US_presidents.json', 'a', encoding='utf-8') as f:
    json.dump(row_data, f, ensure_ascii=False, indent=4)