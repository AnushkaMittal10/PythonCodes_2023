from datetime import datetime
year = int(input("Enter the year:"))
if year % 400 == 0:
    print ("Current year is a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print ("Current year is a leap year")
else:
    print(year, "is not a leap year")