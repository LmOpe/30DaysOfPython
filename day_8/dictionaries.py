dog = {}
dog = {'name': 'Brian', 'color': 'Brown', 'breed': 'dog', 'legs': 4, 'age': '2 years'}
student = {'first_name': 'Muhammed', 'last_name': 'Lawal', 'gender': 'Male', 'age': 15,\
     'marital status': 'single', 'skills': ['Public speaking', 'Teaching'], 'country': 'Nigeria',\
        'city': 'Kwara', 'address': 'Tipper garage'}
print(f'student dictionary length: {len(student)}')
print(f'Skills: {student["skills"]}, "Type: {type(student["skills"])}"')
student['skills'].append('Computer literacy')
print(f'dictionary keys: {student.keys()}')
print(f'dictionary values: {student.values()}')
print(f'student list: {student.items()}')
student.pop('address')
del dog
print(f'Remaining student keys and values: {student}')