import urllib
import urllib.request
import json

print("hello")
url = "https://api.github.com/users/akash-07"
print('Retrieving:',url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
js = json.loads(data)
login = js['login']
name = js['name']
bio = js['bio']
print('Headers: \n', connection.info())
print('Login:',login)
print('name:',name)
print('bio:',bio)
