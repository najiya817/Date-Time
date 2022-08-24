import datetime
print("current date and time: ",datetime.datetime.now())
print("current year: ",datetime.date.today().strftime("%Y"))                #strf=stringformat
print("Month  of the year : ",datetime.date.today().strftime("%B"))
print("Week number of the year: ",datetime.date.today().strftime("%W"))
print("weekday of the week: ",datetime.date.today().strftime("%w"))
print("Day of the year: ",datetime.date.today().strftime("%j"))
print("Day of the month: ",datetime.date.today().strftime("%d"))
print("Day of the week: ",datetime.date.today().strftime("%A"))
