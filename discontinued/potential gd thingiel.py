import requests
a = "http://www.boomlings.com/database/downloadGJLevel22.php"
b = {"gameVersion" : "21", "binaryVersion" : "35", "gdw" : "0", "levelID" : "128", "inc" : "0", "extras" : "0", "secret" : "Wmfd2893gb7"}
response = requests.post(url = a, data = b)
print(response)