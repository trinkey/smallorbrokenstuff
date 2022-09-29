from math import floor as f
while True:
 h=int(input(""))
 if f(h/64)==1:
  print(str(f(h/64)),"stack and",str(h%64))
 else:
  print(str(f(h/64)),"stacks and",str(h%64))