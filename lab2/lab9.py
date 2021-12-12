#Write a Python program to find the index of an item of a tuple

tup = (1, 'a', 'b', 'c', 4, 'k', 1)
print("tuple is: ", tup)
print("Index of the element k is: ", tup.index('k'))
print("Index of the element 1 is: ", tup.index(1))
# index of 1 after 1st index
print("Index of the element 1 after 1st index is: ", tup.index(1, 1))
