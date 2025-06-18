# If elif else statement trials

grade = 85

if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
else:
    print("You got a C")


result = 75

if result >= 90:
    grade = "A"
elif result >= 80:
    grade = "B"
elif result >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Your garde is {grade}")

# Exercise for if elif else statement

alien_color = ["green", "yellow", "red"]

for i in alien_color:
    if i == "green":
        print("You just earned 5 points")
    elif i == "yellow":
        print("You just earned 10 points")
    elif i == "red":
        print("You just earned 15 points")
# Exercise for if elif else statement with a different approach

age= 2

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elderly person")
        
## Exercise for if elif else statement with a different approach

favorite_fruits = ["apple", "banana", "orange"]

fruit="lemon"

for i in favorite_fruits:
    if i == fruit:
        print(f"I really like {fruit}")
    else:
        print(f"I don't like {fruit}")
