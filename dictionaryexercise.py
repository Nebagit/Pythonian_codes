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