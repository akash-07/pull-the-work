import json
import urllib
import urllib.request

def getParams(forks, stars):
    string = "forks:>" + str(forks) + " stars:>" + str(stars)
    return {'q':string}

def writeItemInfo(item, outFile):
    outFile.write('name: ' + item['name'] + '\n')
    outFile.write(item['url'] + '\n')

url = "https://api.github.com/search/repositories?"
params = getParams(1000,300)
outFile = open("name-url-info.txt", "w")
for i in range(1,11):
    params['per_page'] = 100
    params['page'] = i
    url1 = url + urllib.parse.urlencode(params)
    print('Retrieving page ', i, '\n')
    connection = urllib.request.urlopen(url1)
    data = connection.read().decode()
    js = json.loads(data)
    for item in js['items']:
        writeItemInfo(item, outFile)
outFile.close()        
