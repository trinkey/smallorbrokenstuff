from random import *
l="abcdefghijklmnopqrstuvwxyzABCdEFGHIJKLMNOPQRSTUVWXYZ0123456789!#?><:',./;'[]"
c=[char for char in l]
while True:
 m,p=int(input("Length of randomly generated password: ")),""
 for i in range(m):p+=c[randint(0,len(c))-1]
 print("Your password is",p)
