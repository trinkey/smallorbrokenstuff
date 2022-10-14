from math import log
while True:
    try: print(log(float(input("Enter the number: "))) / log(int(input("Enter the root: "))))
    except ValueError: print("Bad input, try again.")
    except ZeroDivisionError: print("Root can't be one")
