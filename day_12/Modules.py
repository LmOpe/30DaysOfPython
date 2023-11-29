from random import  choice, choices, randrange, shuffle
from string import ascii_letters, digits, ascii_lowercase

chars = f'{ascii_letters}{digits}'


def random_user_id(n):
    return ''.join(choices(chars, k=n))
print(random_user_id(9))

def user_id_gen_by_user():
    num_of_chars = int(input())
    num_of_id = int(input())

    ids = []
    for i in range(num_of_id):
        ids.append(random_user_id(num_of_chars))

    return ids

# print(user_id_gen_by_user())

def rgb_color_gen():
    r = int(randrange(0, 255))
    g = int(randrange(0, 255))
    b = int(randrange(0, 255))

    return f'rgb{r,g,b}'

print(rgb_color_gen())

def list_of_hexa_colors(n):
    colors = []
    hexa = f'{ascii_lowercase[:6]}{digits}'
    for i in range(n):
        color = ''.join(choices(hexa, k=6))
        colors.append(f'#{color}')

    return colors
print(list_of_hexa_colors(5))

def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        colors.append(rgb_color_gen())

    return colors

print(list_of_rgb_colors(4))

def generate_colors(type, number):
    if(type == 'hexa'):
        return list_of_hexa_colors(number)
    elif(type == 'rgb'):
        return list_of_rgb_colors(number)

print(generate_colors('hexa', 1))

def shuffle_list(lists):
    shuffle(lists)
    return lists

print(shuffle_list(['hello', 4, '9281cdad', 92, 'H']))

def array_of_rand():
    numbers = []

    while(True):
        rand = int(choice(digits))
        if len(numbers) == 7:
            return numbers
        else:
            if not (rand in numbers):
                numbers.append(rand)

    return numbers
print(array_of_rand())