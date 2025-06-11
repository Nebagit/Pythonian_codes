myfamily = ["Dad", "Mom", "Brother", "Sister"]
print (myfamily)
myfamily.append("Me")
print(myfamily)
myfamily.insert(4, "Someone")
print(myfamily)
del myfamily[4]
print(myfamily)
myfamily.remove("Brother")
print(myfamily)

for i in myfamily:
 print(i)

for i in myfamily:
 print( f"Hello {i.title()}, That was a greate trick" )
total = 0
for i in range(1, 1000000):
   total=total + i 
print(f"The sum of the first 1000000 numbers is {total}")

if (total == (sum(range(1, 1000000)))):
   print("The total is correct")
else:
   print("The total is incorrect")