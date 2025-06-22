alien = []

for i in range(30):
    alien.append({"color": "green", "points": 5})

for i in alien[:5]:
    print(i)
print("...")
print(f"Total number of aliens: {len(alien)}")

# Change the first three aliens to yellow and 10 points
for aliens in alien[:3]:
    if aliens["color"] == "green":
        aliens['color'] = "yellow"
        aliens['points'] = 10

# Display the first five aliens after the change
for alien in alien[:5]:
    print(alien)
print("...")
print(f"Total number of aliens after change: {len(alien)}")


# store list inside a dictionary
favorite_languages = {
    'jen': ['python', 'java'],
    'sarah': ['c', 'c++'],
    'edward': ['ruby'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"{name.title()}'s favorite language is {languages[0].title()}")


# piza toppings list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(
    f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")
