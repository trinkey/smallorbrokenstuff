import math
hexNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
while True:
    try:
        n = int(round(float(input("Number to convert to Hexadecimal - "))))
        output = ""
        while True:
            q = n % 16
            output = hexNum[q] + output
            n = math.floor(n / 16)
            if n < 1:
                break
        print(output)
    except:
        print("Bad input")