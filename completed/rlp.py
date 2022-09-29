from random import randint as rand
from win10toast import ToastNotifier as notif

print("""New: make a new input
Stop: completely stop the code
Anything else: output again
Seperate each item in the list with a comma and a space.
""")

note = 1
toast = notif()
while True:
    stop = ""
    
    raw = input("Input: ")
    stringList = raw.split(", ")

    while stop != "stop" and stop != "new":
        output = stringList[rand(0,len(stringList) - 1)]
        print(output)
        if note == 1:
            toast.show_toast("Output", output + """
NOTE: There is a cooldown for these notifications but all inputs register.""")
            note = 0
        else:
            toast.show_toast("Output", output)
        stop = input().lower()

    if stop == "stop":
        break