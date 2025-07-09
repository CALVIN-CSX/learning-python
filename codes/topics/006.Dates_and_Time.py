import datetime as dt
date=dt.date(2025,1,1)
today=dt.date.today()
print(date)
print(today)

time=dt.time(12,30,0)
print(time)
now=dt.datetime.now()#datetime module as an datetime class
print(now)
now=now.strftime("%H:%M:%S %d-%m-%Y")
print(now)
#simple program to check target if date has been met or not
target=dt.datetime(2026,1,1,12,00,00)
current_time=dt.datetime.now()
if current_time>target:
    print("Target has been passed")
else:
    print("Target has not been passed")