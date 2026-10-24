import calendar


m, d, y = map(int, input().strip().split())
day_of_week = calendar.day_name[calendar.weekday(y, m, d)]

print(day_of_week.upper())
