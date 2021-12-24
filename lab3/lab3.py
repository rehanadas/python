#Write a Python program to append text to a file and display the text.
f = open('python/lab3/test.txt', 'a')  # append mode
f.write("\nPython\n")
f.close()