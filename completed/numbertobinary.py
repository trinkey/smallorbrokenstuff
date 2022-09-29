len = 0 # Amount of bits - 0 is as many as needed to get the full number
while True:
    try:
        x = int(round(float(input("Number to get turned into binary: "))))
        n = 0
        if len == 0:
            while 2 ** n <= x: n += 1
        else: n = len
        output = ""
        for i in range(n):
            if x >= 2 ** (n - i - 1): output += "1"; x -= 2 ** (n - i - 1)
            else: output += "0"
        print(output)
    except: print("Bad input")