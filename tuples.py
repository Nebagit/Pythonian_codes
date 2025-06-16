dimensionofrectangle=(80, 200, 40, 900)
for i in dimensionofrectangle:
    print(i)
# Accessing elements in a tuple
# Tuples are immutable Lists...........
# we cannot change the elements of a tuple once it is created

tupltesting = ("test1", "test2", "test3", "test4", "test5")
print(tupltesting)
# inserting elements in the tuple is not possible, but we can create a new tuple with additional elements
tupltesting = tupltesting + ("test6APPENDED",)
print(tupltesting)
tupltesting= ("just one", "just two", "just three", "just four", "test5", "test6")
print(tupltesting)