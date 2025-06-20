# dictionaries in Python are mutable, unrdered collections  of key-value pairs
# they are defined using curly braces {} or the dict() constructor

nebiyu = {"name": "Nebiyu", "school": "Addis Ababa University", "age": 22, "experience": 2}
print(nebiyu)

# updating the value of the key "age"

nebiyu["age"] = 23  
print(nebiyu)

nebiyu["skills"] = ["Python", "JavaScript", "C++"]  # adding a new key-value pair
print(nebiyu)
