import json
import recRetrieve as rec
import utilities as ut
import urllib
import csv

def action(data,first_page):
    js = json.loads(data)
    if not js:
        return 0
    keys = ['title', 'commits', 'additions','deletions','changed_files','author_association']
    rowdata = []
    for pull_req in js:
        url = pull_req['url']
        params = ut.getParams()
        if params:
            url += '?' + urllib.parse.urlencode(params)
        print('url for this pull_req:', url)
        conn = urllib.request.urlopen(url)
        data = conn.read().decode()
        pr = json.loads(data)
        row_data = {}
        for key in keys:
            row_data[key] = pr[key]
        rowdata.append(row_data)
        print('Working on pull request titled:', row_data['title'])
    filename = js[0]['base']['repo']['name'] + '.csv'
    print('Storing data in', filename)
    csv_file = open(filename, "a+")
    writer = csv.DictWriter(csv_file, fieldnames=keys,quoting = csv.QUOTE_NONNUMERIC)
    if first_page:
        writer.writeheader()
    for row in rowdata:
        writer.writerow(row)
    csv_file.close()
