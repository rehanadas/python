#Write a Python program to convert a list of characters into a string.
def convertStr(lst):
    new = ""
    for x in lst:
        new += x 
    return new

lst = ['p', 'y', 't', 'h', 'o', 'n']
print("The list of characters is: ", lst)
print("The string is: ", convertStr(lst))