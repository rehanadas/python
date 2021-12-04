from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))
remaing_years= 100 - age
current_year = date.today().year
print("Hello ",name,". You will be 100 years old in ", current_year+remaing_years)
