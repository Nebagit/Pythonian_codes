alien = []

for i in range(30):
    alien.append({"color": "green", "points": 5})

for i in alien[:5]:
    print(i)
print("...")
print(f"Total number of aliens: {len(alien)}")
