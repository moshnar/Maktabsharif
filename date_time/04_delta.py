from datetime import date, timedelta

start_date = date(2020, 10, 19)
end_date = date(2020, 11, 7)

delta = end_date - start_date

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    print(day)
