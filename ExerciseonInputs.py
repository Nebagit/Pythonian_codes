car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")

Restaurantseating = input("How many people are in your dinner group? ")
if int(Restaurantseating) > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")