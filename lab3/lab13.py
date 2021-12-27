# Write a Python program to copy the contents of a file to another file .
# open both files
with open('python/lab3/test.txt', 'r') as firstfile, open('python/lab3/test1.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # append content to second file
        secondfile.write(line)

content = open('python/lab3/test1.txt')
print(content.read())
    
