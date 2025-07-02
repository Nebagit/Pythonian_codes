unconfirmed_users = ['alice', 'bob', 'charlie', 'dave']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'goldfish', 'rabbit', 'hamster', 'cat', 'cat', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')

print("\nUpdated list of pets:")
for pet in pets:
    print(pet.title())