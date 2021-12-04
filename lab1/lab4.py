# method to print the divisors
def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print(i)
        i = i + 1
          
number = int(input("Enter a number: "))
printDivisors(number)