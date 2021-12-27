#Write a Python program to write a list to a file.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('python/lab3/test1.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('python/lab3/test1.txt')
print(content.read())