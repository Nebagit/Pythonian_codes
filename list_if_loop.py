available_toppings = ['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']

requisted_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requisted_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")

# exercise for advanced List , If statement and For loop concepts
# 

usernames = ['admin', 'john', 'jane', 'doe', 'alice']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.") 

# Exercise 2 for advanced List , If statement and For loop concepts with a different approach
# This code checks if the list is empty or not 'if (list_name):' check the list whether it is empty or not
# If it is not empty, it checks if the username is 'admin' or not
# and prints a message accordingly
usernames = ['admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("\nHello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Exercise 3 for advanced List , If statement and For loop concepts with a different approach

current_users = ['alice', 'bob', 'charlie', 'dave', 'eve']
new_users = ['Alice', 'Bob', 'Frank', 'Grace', 'Heidi']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"{new_user} has already been used. Please choose a different username.")
    else:
        print(f"{new_user} is available for use.")

