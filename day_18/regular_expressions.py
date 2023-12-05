import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'[ .]'
matches = re.split(regex_pattern, paragraph)
# print(matches)

words_count = Counter(matches)
print(f'Most frequent word is {words_count.most_common(1)[0][0]}')

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
regex_pattern = r'-?\d+'
numbers = [int(num) for num in re.findall(regex_pattern, ' '.join(points))]
distance = max(numbers) - min(numbers)
print(distance)

def is_valid_variable(var):
    regex_pattern = r'^[A-Za-z_]\w*$'
    return bool(re.match(regex_pattern, var))

print(is_valid_variable('3firstname'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering 
peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = re.sub(r'[@%$&#;]', '',sentence)
regex_pattern = r'[ .,\n!?]'
cleaned_text_words = re.split(regex_pattern, cleaned_text)
most_frequent_words = Counter(list(filter(lambda x: x != '', \
    cleaned_text_words))).most_common(3)
print(most_frequent_words)