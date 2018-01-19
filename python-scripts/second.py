import urllib
import urllib.request
import json

def getParams(forks, stars):
    string = "forks:>" + str(forks) + " stars:>" + str(stars)
    return {'q':string}
url = "https://api.github.com/search/repositories?"
params = getParams(1000,300)
url += urllib.parse.urlencode(params)
print('Retrieving:',url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
js = json.loads(data)
print('Count = ', js['total_count'])
print(len(js['items']))
i = 0

'''
for item in js['items']:
    i = i + 1
    print(i,item['full_name'])
#print(js)
'''
for key in js['items'][0].keys():
    print(key)
release_url = js['items'][1]['releases_url'][:-5]
print('Printing release url:', release_url)
connection = urllib.request.urlopen(release_url)
data = connection.read().decode()
print(data)
