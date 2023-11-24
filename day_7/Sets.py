# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'Length: {len(it_companies)}')

it_companies.add("Twitter")
it_companies.update(['Paypal', 'Stripe', 'Netflix'])
print(it_companies)

it_companies.remove('Netflix')
# If the specified element does exist in the set, 
# remove function returns error while discard does not

print(A.union(B))
print(A.intersection(B))
print(f'Is A subset of B: {A.issubset(B)}')
print(f'Are A and B disjoint sets: {A.isdisjoint(B)}')
print(f'Join A with B and B with A: {A.union(B)} and {B.union(A)}')
print(f'What is the symmetric difference between A and B: {A.symmetric_difference(B)}')
del A, B

print(f'Convert the ages to a set and compare\
 the length of the list and the set, which one is bigger?\
 ...Set: {len(set(age))}, List: {len(age)}')

 # String is a sequence of characters. It is created by adding double, 
 # single or triple quotes around a set of character
 # List is an ordered collection of items, 
 # the objects inside a list can be of any data type
 # Tuple is a collection of different items. 
 # A tuple is immutable unlike list.
 # Set is a collection of unodered distinct items

sentence = 'I am a teacher and I love to inspire and teach people'.split(' ')
unique_words = set(sentence)
print(f'Number of unique words: {len(unique_words)}')