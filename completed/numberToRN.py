# Customizable, but why?
n = ["I", "V", "X", "L", "C", "D", "M"]

d = ["", n[0], n[0] + n[0], n[0] + n[0] + n[0], n[0] + n[1], n[1], n[1] + n[0], n[1] + n[0] + n[0], n[1] + n[0] + n[0] + n[0], n[0] + n[2]]
e = ["", n[2], n[2] + n[2], n[2] + n[2] + n[2], n[2] + n[3], n[3], n[3] + n[2], n[3] + n[2] + n[2], n[3] + n[2] + n[2] + n[2], n[2] + n[4]]
f = ["", n[4], n[4] + n[4], n[4] + n[4] + n[4], n[4] + n[5], n[5], n[5] + n[4], n[5] + n[4] + n[4], n[5] + n[4] + n[4] + n[4], n[4] + n[6]]
g = ["", n[6], n[6] + n[6], n[6] + n[6] + n[6]]
while True:
    try:
        a = str(round(float(input("What number? (1 to 3999)\n"))))
        b = [char for char in a]
        if int(a) >= 1 and int(a) <= 3999:
            c = len(a)
            if c == 1:
                h = d[int(b[0])]
            elif c == 2:
                h = e[int(b[0])] + d[int(b[1])]
            elif c == 3:
                h = f[int(b[0])] + e[int(b[1])] + d[int(b[2])]
            elif c == 4:
                h = g[int(b[0])] + f[int(b[1])] + e[int(b[2])] + d[int(b[3])]
            print(h)
        else:
            if int(a) < 1:
                print("number too small, minimum 1")
            else:
                print("number too large, maximum 3999")
        
    except:
        print("bad input, try again")