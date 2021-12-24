#Write a Python program to read a file line by line and store it into a list.
with open('python/lab3/test.txt') as f:
    content_list = f.readlines()
    print(content_list)