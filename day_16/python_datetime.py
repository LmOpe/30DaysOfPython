from datetime import datetime, date

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

now_format = now.strftime("%m/%d/%Y, %H:%M:%S")

print(now_format)

date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

today = date(year=2023, month=12, day=3)

new_year = date(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today

print('Time left for new year: ', time_left_for_newyear)

epoch = date(year=1970, month=1, day=1)
diff = today - epoch
print(diff)