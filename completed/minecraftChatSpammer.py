from keyboard import is_pressed
from pynput.keyboard import Key, Controller
from time import sleep

k = Controller()

while True:
    if is_pressed("home"):
        k.press("t")
        k.release("t")
        k.press(Key.up)
        k.release(Key.up)
        k.press(Key.enter)
        k.release(Key.enter)
        sleep(1/20)