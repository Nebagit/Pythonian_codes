testlist=["test1", "test2", "test3", "test4", "test5"]
# inserting elements in the list with append, and insert methods
print(testlist)
testlist.append("test6APPENDED")
print(testlist)
testlist.insert(2, "test7INSERTED")
print(testlist)

# removing element from the list with remove and pop methods
del testlist[2]
print(testlist)
popped1 = testlist.pop()
print(f"Popped element: {popped1}")
print(testlist)
popped2 = testlist.pop(1)
print(f"Popped element at index 1: {popped2}")
testlist.remove("test4")
print(testlist)






# sorting the list in ascending and descending order

myfavoriteplaces = ["Greece", "Israel", "Jerusalem", "Turkey", "Alexandria", "Cairo", "Egypt", "Italy", "Rome", "Venice", "Florence"]
print(myfavoriteplaces)
print("\nHere is the original list of my favorite places:", myfavoriteplaces)
print("\nHere is the sorted list of my favorite places:", sorted(myfavoriteplaces))
print("\nHere is the  original list of my favorite places again:", myfavoriteplaces)


myfavoriteplaces.sort()
print("\n\n Sorted in ascending order:", myfavoriteplaces)
myfavoriteplaces.sort(reverse=True)
print("\n\nSorted in descending order:", myfavoriteplaces)
