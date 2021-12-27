# Write a Python program to get the file size of a plain file
import os
statinfo = os.stat("python/lab3/test.txt")
print("File size in bytes of a plain file: ",statinfo.st_size)
