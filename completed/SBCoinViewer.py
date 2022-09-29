import requests
def split(inp,out=None):
 h=inp.text.split(",")
 a=[]
 b=[]
 for i in range(len(h)):
  a.append(h[i].replace("{","").replace('"',"").split(":")[0])
  b.append(h[i].replace("}","").replace('"',"").split(":")[1])
 if out==1:
  return a
 else:
  return b
def balance(username,profile):
 test=requests.get(url="https://sky.shiiyu.moe/api/v2/coins/"+username.lower()+"/"+profile.lower())
 try:
  a=split(test, 1)
  b=split(test)
 except: print(" API broken or something")
 try:
  longdef=str("{:,}".format(round(float(b[2]))))
  if len(a) >= 3:
   if a[2]=="purse":
    print(" Purse balance: "+longdef)
    if len(a) >= 4:
     if a[3]=="bank":
      print(" Bank balance: "+str("{:,}".format(round(float(b[3]))))+"\n Total balance: "+str("{:,}".format(round(float(b[2]))+round(float(b[3])))))
     else:
      print(" Bank balance: 0\n Total balance: "+longdef)
    else:
     print(" Bank balance: 0\n Total balance: "+longdef)
   else:
    print(" Purse balance: 0")
    if a[2]=="bank":
     print(" Bank balance: "+longdef+"\n Total balance: "+longdef)
    else:
     print(" Bank balance: 0\n Total balance: 0")
  else:print(" Something went wrong, one of the following most likely happened:\n 1: that person has api off\n 2: bad username/profile")
 except:print(" Bad output")
print(" Who do you wanna spy on?")
while True:balance(input(" Username: "),input(" Profile: "))