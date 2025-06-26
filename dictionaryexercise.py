dawit_dictionary = {'first_name': 'Dawit', 'last_name': 'Abreham', 'age': 25, 'city': 'Addis Ababa'}
melaku_dictionary = {'first_name': 'Melaku', 'last_name': 'Fetene', 'age': 25, 'city': 'Addis Ababa'}

person = [dawit_dictionary, melaku_dictionary]

for person_info in person:
    print(f"First Name: {person_info['first_name']}")
    print(f"Last Name: {person_info['last_name']}")
    print(f"Age: {person_info['age']}")
    print(f"City: {person_info['city']}")
    print()  # Print a newline for better readability

# Pets dictionary
dog = {'pet_type': 'dog', 'owner': 'Dawit', 'name': 'Rex', 'age': 3}
cat = {'pet_type': 'cat', 'owner': 'Melaku', 'name': 'Whiskers', 'age': 2}
pets = [dog, cat]

for pet in pets:
    print(f"Pet Type: {pet['pet_type']}")
    print(f"Owner: {pet['owner']}")
    print(f"Name: {pet['name']}")
    print(f"Age: {pet['age']}")
    print()  # Print a newline for better readability

# Favorite places dictionary
favorite_places = {
    'Dawit': ['Addis Ababa', 'Bahir Dar', 'Wollo'],
    'Melaku': ['Addis Ababa', 'Debre Tabor'],
    'Yekoye': ['Debre Tabor', 'Lalibela']
}

for favoriteofperson in favorite_places:
    print(f"{favorite_places[favoriteofperson]} are the Favorite Place {favoriteofperson} want to see")


favorite_numbers = {
'Dawit': [1,2,3],
'Melaku': [3,4,5,6],
'Yekoye': [12,23,34,45]
}

for favnum in favorite_numbers:
    print(f"{favorite_numbers[favnum]} are the Numbers {favnum} Likes")


cities={
'Addis Ababa': {'Country': 'Ethiopia', 'Admin': 'Adancch', 'Population': '10000000', 'Fact': 'Very busy, and much diversities'},
'Bahrar': {'Country': 'Ethiopia', 'Admin': 'Melaku', 'Population': '1234567890', 'Fact': 'Very smart, and interesting peoples'}
}

for city in cities:
    print(f"City Name: {city}\n The details of the city: {cities[city]}")