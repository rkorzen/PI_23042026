import datetime

print(dir(datetime))

d = datetime.datetime.now()
delta = datetime.timedelta(hours=1)

d2 = (d + delta)

print(d2 - d)

print(d2 > d)

d3 = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)

print(d3)

print(d3 > d2)
