import urllib
import json
import urllib.request
import re

default_url = 'https://api.github.com/repos/tensorflow/tensorflow/pulls'

def retrieve(url, params, action, first_page=True):
    '''retrieve takes three arguements.

    url - url of the target page
    params - additional information to encode in url
    action - action that needs to be taken on read data

    It recursively checks for any 'next' links being
    available in the file header and traverses them to
    perform the same action. '''
    if params:
        url += '?' + urllib.parse.urlencode(params)
    print('Retrieving:', url)
    connection = urllib.request.urlopen(url)
    headers = str(connection.info())
    data = connection.read().decode()
    action(data,first_page)
    #print(headers)
    links = re.findall(r'<(.+?)>', headers)
    pointers = re.findall(r'rel=\"(\S+)\"', headers)
    limit = re.findall(r'X-RateLimit-Remaining: (\d+)', headers)
    if limit:
        print('Limit Remaining:', limit[0])
        if(int(limit[0]) == 0):
            return
    #print(links)
    #print(pointers)
    for i in range(0, len(pointers)):
        if(pointers[i] == 'next'):
            url = links[i]
            return retrieve(url, {}, action,False)
