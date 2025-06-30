car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

Restaurantseating = input("How many people are in your dinner group? ")
if int(Restaurantseating) > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")

number = input("Enter a number: ")
if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


pizza = input("What toppings would you like on your pizza? (Enter 'quit' to finish) ")
while pizza.lower() != 'quit':
    print(f"Adding {pizza} to your pizza.")
    pizza = input("What other toppings would you like? (Enter 'quit' to finish) ")  

while True:
    age = input("How old are you? (Enter 'quit' to exit) ")
    if age.lower() == 'quit':
        break
    elif age.isdigit():
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    else:
        print("Please enter a valid age or 'quit' to exit.")
