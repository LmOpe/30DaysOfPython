numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_number = [i for i in numbers if i > 0]

print(filtered_number)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lists = [flat_list for row in list_of_lists for col in row for flat_list in col]

print(lists)

list_tuple = [(i, i**0, i**1, i**3, i**4, i**5) for i in range(10)]
print(list_tuple)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_list = [[i[0], i[0][:3], i[1]] for lists in countries for i in lists]

print(flattened_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_of_dict = [{'country': i[0].upper(), 'city': i[1].upper()} for lists in countries for i in lists]

print(list_of_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concat = [i[0] + ' ' + i[1] for lists in names for i in lists]

print(concat)

slope = lambda y1, y2, x1, x2: ((y2 - y1) / (x2 - x1))

print(slope(5, 2, 8, 3))