#Write a Python program to get days between two dates. Go to the editor 
#Exampe: days between 28/02/2000 and  28/02/2001
from datetime import date
date1= date(2000,2,28)
date2= date(2001,2,28)
date3 = date2 - date1
print("days between 28/02/2000 and  28/02/2001 is ",abs(date3.days))