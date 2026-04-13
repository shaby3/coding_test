n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

weathers = []

for dt, d, w in zip(date, day, weather):
    if w == "Rain":
        weathers.append(Weather(dt, d, w))

weathers.sort(lambda x: x.date)

print(weathers[0].date, weathers[0].day, weathers[0].weather)