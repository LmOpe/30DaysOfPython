""" Exercise 1"""
empty_tuple = ()
brothers = ('Ibraheem', 'Ismaheel')
sisters = ('Hadizah', 'Khodijah', 'Ahleesah')
siblings = brothers + sisters
print(f"Number of siblings: {len(siblings)}")
family_members = siblings + ('Muhammed', 'Sofiyah')


"""Exercise 2"""
mother, father, *siblings = reversed(family_members)
fruits = ('Mango', 'Apple', 'Guava')
vegetables = ('Lettuce', 'Waterleaf')
animal_products = ('Milk', 'Hide')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
mid_index = len(food_stuff_tp)//2
mid = food_stuff_tp[mid_index:mid_index+1]
print(mid)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[:-4:-1]
print(first_three, last_three)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'Check if "Estonia" is a nordic country: {"Estonia" in nordic_countries}')
print(f'Check if "Iceland" is a nordic country: {"Iceland" in nordic_countries}')