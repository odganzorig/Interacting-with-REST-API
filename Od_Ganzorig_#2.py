#!/usr/bin/python3
import requests
import json

def printContent(request):
  print(json.dumps(r.json(), indent=3))

r = requests.get("http://127.0.0.1:5000/")
r.status_code           # Should be 200
r.json()                # The json body of the request as a Python dictionary
printContent(r)         # Prints the json body of the request
r.headers               # A dictionary of the provided headers

## Write your code in what follows. You can include comments describing what you are doing.

#1
def printUser(request):
  print(request.json()["first"] + " " + request.json()["last"])

users = requests.get("http://127.0.0.1:5000/user")
users.json()["users"][0]["link"]
scientist = requests.get("http://127.0.0.1:5000" + users.json()["users"][0]["link"])
printUser(scientist)

#2
s = requests.post('http://127.0.0.1:5000/user', json = {'first': 'Benedict', 'last': 'Cumberbatch'})
s2 = requests.get(s.headers["Location"])
s2.json()
printUser(s2)

#3
n = requests.post(s.headers["Location"] + '/message', 
  json = {'recipient': users.json()["users"][0]["username"], 'text': "The Imitation Game"})
n.json()









         
    