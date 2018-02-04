import json
import recRetrieve as rec
import utilities as ut
import urllib
import csv

def action(data,first_page, filename = 'tensorflow-issues.csv'):
    js = json.loads(data)
    if not js:
        return 0
    keys = ['number', 'title', 'labels', 'body', 'assignees', 'milestone', 'comments', 'created_at', 'author_association']
    rowdata = []
    N = 0
    for pull_req in js:
        N += 1
        url = pull_req['url']
        params = ut.getParams()
        if params:
            url += '?' + urllib.parse.urlencode(params)
        print('[{}] url for this pull_req: {}'.format(N, url))
        conn = urllib.request.urlopen(url)
        data = conn.read().decode()
        pr = json.loads(data)
        row_data = {}
        for key in keys:
            if(key == 'labels'):
                string = ''
                for label in pr[key]:
                    string += label['name'] + ','
                string = string[:-1]
                row_data[key] = string
            else:
                if(key == 'assignees'):
                    row_data[key] = len(pr[key])
                else:
                    row_data[key] = pr[key]
        rowdata.append(row_data)
        print('Working on pull request titled:', row_data['title'])
        #break
    #filename = js[0]['base']['repo']['name'] + '.csv'
    print('Storing data in', filename)
    csv_file = open(filename, "a+")
    writer = csv.DictWriter(csv_file, fieldnames=keys) #,quoting = csv.QUOTE_NONNUMERIC)
    if first_page:
        writer.writeheader()
    for row in rowdata:
        try:
            writer.writerow(row)
        except:
            print('Caught an exception. Continuing now....')
            continue
    csv_file.close()
