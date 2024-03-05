#1
import datetime as dt
a = dt.datetime.now()
b = a - dt.timedelta(days=5)
print(b)
#2
t = dt.datetime.now()
y = t - dt.timedelta(days = 1)
tr = t + dt.timedelta(days = 1)
print(t,y,tr)
#3 
z = t.replace(microsecond = 0)
print(z)
#4
print('write first date year')
d1y = int(input())
print('write first date month')
d1m = int(input())
print('write first date day')
d1d = int(input())
print('write second date year')
d2y = int(input())
print('write second date month')
d2m = int(input())
print('write second date day')
d2d = int(input())
d1 = dt.datetime(d1y, d1m, d1d)
d2 = dt.datetime(d2y, d2m, d2d)
diff = (d1-d2).total_seconds()
print(diff)


