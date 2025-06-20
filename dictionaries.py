# dictionaries in Python are mutable, unrdered collections  of key-value pairs
# they are defined using curly braces {} or the dict() constructor

nebiyu = {"name": "Nebiyu", "school": "Addis Ababa University", "age": 22, "experience": 2}
print(nebiyu)

# updating the value of the key "age"

nebiyu["age"] = 23  
print(nebiyu)

nebiyu["skills"] = ["Python", "JavaScript", "C++"]  # adding a new key-value pair
print(nebiyu)


dawit = {"first_name": "Dawit", "last_name": "Abreham", "age": 25, "city": "Addis Ababa"}
# print(dawit)

print(f"First Name: {dawit['first_name']}")
print(f"Last Name: {dawit['last_name']}")
print(f"Age: {dawit['age']}")
print(f"City: {dawit['city']}")

favorite_numbers = {
    "Dawit": 12,
    "Melaku": 19,
    "Yekoye": 21,
    "Nebiyu": 7,
}

print(f"Dawit's favorite number is {favorite_numbers['Dawit']}")
print(f"Melaku's favorite number is {favorite_numbers['Melaku']}")
print(f"Yekoye's favorite number is {favorite_numbers['Yekoye']}")
print(f"Nebiyu's favorite number is {favorite_numbers['Nebiyu']}")