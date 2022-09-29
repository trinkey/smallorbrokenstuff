a = int(input("input a number and I will output a number between 1 and it - "))
import random
while not a == 0:
  print(" " + str(random.randint(1,a)))
  a = int(input())
