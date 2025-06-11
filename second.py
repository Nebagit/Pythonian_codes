# This script demonstrates the use of the continue statement in a loop.
# It will print only the odd numbers from 0 to 19.

for i in range(0, 21):
    if(i % 2 == 0):
        continue
    else:
        print(f"{i} is an odd number")

# a code that prints multiples of 3 from 0 to 30

for i in range(0, 31):
    if(i % 3 == 0):
        print(f"{i} is a multiple of 3")
    else:
        continue

# a code that prints the firt 10 numbers of third power

for i in range (0, 11):
    print (f"The third power of {i} is {i**3}")