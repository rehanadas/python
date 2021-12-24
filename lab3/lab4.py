# Write a Python program to read last n lines of a file.
def LastNlines(fname, N):
	with open(fname) as file:
	    for line in (file.readlines()[:N]):
		    print(line, end='')

fname = 'python/lab3/test.txt'
N = 3
try:
	LastNlines(fname, N)
except:
	print('File not found')
