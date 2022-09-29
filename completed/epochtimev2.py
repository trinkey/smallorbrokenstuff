import time
import math
t = time.time()
y = math.floor((t / 31557600) + 1970)

if y > 2000:
    t += 86400
d = math.floor((t - (31557600 * (y - 1970))) / 86400)
h = math.floor((t - (31557600 * (y - 1970)) - (86400 * d)) / 3600)
m = math.floor((t - (31557600 * (y - 1970)) - (86400 * d) - (3600 * h)) / 60)
s = math.floor(t - (31557600 * (y - 1970)) - (86400 * d) - (3600 * h) - (60 * m))
ap = "AM"
if h > 12:
    ap = "PM"
    h = h - 12
l = 0
if h == 0:
    h = 12
if y % 4 == 0:
    l = 1

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days = [0,31 + l,28 + l,31 + l,30 + l,31 + l,30 + l,31 + l,30 + l,31 + l,30 + l,31 + l,30 + l]

month = 0
sum = 0
day = 0
for ds in days:
    sum += ds
    if d - sum < ds:
        day = d - sum
        break
    month += 1
if len(str(m)) == 1:
    m = "0" + str(m)

print(f"Today is {months[month]} {str(day)}, {str(y)}, at {str(h)}:{str(m)} {ap} and {str(s)} seconds. (UTC)")
