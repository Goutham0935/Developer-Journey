import datetime

time = datetime.datetime.now()
print(time)
print(time.year)
print(time.month)
print(time.hour)
print(time.day)
print(time.minute)
print(time.second)
print(time.microsecond)

print(time.strftime("%M"))

#modes of datetime
#%Y = Year, %m = month, %d = day, %H = hour, %M = minute, %S = Seconds, %p = AM/PM

birthday = datetime.datetime(1991, 6, 15)
age_days = time - birthday
age_year = time.year - birthday.year
print(age_days)
print(age_years)

print(time + datetime.timedelta)(days)