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
if y % 4 == 0:
    l = 1
if d <= 31:
    month = "Janurary"
elif d <= 59 + l:
    month = "Feburary"
    d = d - 31 - l
elif d <= 90 + l:
    month = "March"
    d = d - 59 - l
elif d <= 120 + l:
    month = "April"
    d = d - 90 - l
elif d <= 151 + l:
    month = "May"
    d = d - 120 - l
elif d <= 181 + l:
    month = "June"
    d = d - 151 - l
elif d <= 212 + l:
    month = "July"
    d = d - 181 - l
elif d <= 243 + l:
    month = "August"
    d = d - 212 - l
elif d <= 273 + l:
    month = "September"
    d = d - 243 - l
elif d <= 304 + l:
    month = "October"
    d = d - 273 - l
elif d <= 334 + l:
    month = "November"
    d = d - 304 - l
elif d <= 365 + l:
    month = "December"
    d = d - 334 - l
if len(str(m)) == 1:
    m = "0" + str(m)
print("Today is " + month + " " + str(d) + ", " + str(y) + ", at " + str(h) + ":" + str(m) + " " + ap + " and " + str(s) + " seconds. (UTC)")
