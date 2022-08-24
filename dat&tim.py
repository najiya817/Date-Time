from datetime import date,timedelta

def all_sundays(year):
    #jan 1 of the given year
    dt = date(year,1,1)
    #frst snday of the given year
    print(dt.weekday())
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt + timedelta(days=7)

for s in all_sundays(2020):
    print(s)