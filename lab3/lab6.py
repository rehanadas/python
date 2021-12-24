#Write a Python program to read a file line by line store it into a variable
with open ('python/lab3/test.txt', "r") as myfile:
    data=myfile.readlines()
    print(data)