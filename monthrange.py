from calendar import monthrange
year=2022
month=2
print(monthrange(year,month)[1])
print("--------------------------------------------")

from calendar import monthrange
year=int(input("enter the year: "))
month=int(input("enter the month: "))
print(monthrange(year,month)[1])
