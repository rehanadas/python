#Write a Python program to sum all the items in a list.
total = 0
lst = [11, 22, 33, 14, 20]
print("List is: ", lst)
for ele in range(0, len(lst)):
    total = total + lst[ele]
print("Sum of all elements in given list: ", total)