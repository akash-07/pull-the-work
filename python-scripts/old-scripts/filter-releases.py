import json
import urllib
import urllib.request
import re

inFile = open('name-url-info.txt', 'r')
for line in inFile:
    name = line[line.find(' ')+1:].rstrip()
    url = inFile.readline().rstrip()
    url += '/releases?'
    params = {'access_token':'26e3f7340239e28acf3a2a1b79736f6f5d81ee9a','per_page':'100'}
    url += urllib.parse.urlencode(params)
    print('Working on:', name)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    header = connection.info()
    limit = re.findall(r'X-RateLimit-Remaining: (\d+)', str(header))
    print('Limit Remaining:', limit[0], '\n')
    js = json.loads(data)
    if js:
        outFile = open('./release-dates/' + name + '.txt', 'w')
        for item in js:
            date = item['published_at'][:10]
            outFile.write(date + '\t')
            outFile.write(item['tag_name'] + '\n')
        outFile.close()
