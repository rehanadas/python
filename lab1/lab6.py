str = input("Enter a string: ")
reverse_str = str[::-1]
if str == reverse_str:
    print("The string is palindrome")
else:
    print("The string is not palindrome")