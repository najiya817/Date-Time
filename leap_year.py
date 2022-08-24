def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return True
    if y % 4 == 0:
        return True
    else:
        return False
y=int(input("enter yaer:"))
print(leap_year(y))

#print(leap_year(2004))
#print(leap_year(2022))