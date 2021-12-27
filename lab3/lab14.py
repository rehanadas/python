#Write a Python program to combine each line from first file with the corresponding line in second file.
with open('python/lab3/test.txt') as fh1, open('python/lab3/test1.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
