responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? (Type 'quit' to exit): ")
    if name.lower() == 'quit':
        polling_active = False
    else:
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")