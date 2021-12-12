#Write a python program to count repeated characters in a string.

def char_frequency(str):
    dict = {}
    count = 0
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] = dict[n] + 1
        else:
            dict[n] = 1
    for key in dict:
         if(dict[key] > 1):
             count += 1
    print("There are ",count," repeated characters")

str = input("Please enter the string:")
char_frequency(str)
