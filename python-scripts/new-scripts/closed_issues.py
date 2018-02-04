import json
import recRetrieve as rec
import utilities as ut
import urllib
import csv

def action(data,first_page, filename = 'tensorflow-issues-closed1.csv'):
    js = json.loads(data)
    if not js:
        return 0
    keys = ['number', 'title', 'labels', 'body', 'assignees', 'milestone', 'comments', 'created_at', 'closed_at', 'author_association']
    rowdata = []
    N = 0
    for pull_req in js:
        try:
            N += 1
            url = pull_req['url']
            params = ut.getParams()
            if params:
                url += '?' + urllib.parse.urlencode(params)
            print('[{}] url for this issue: {}'.format(N, url))
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
            print('Working on the issue titled:', row_data['title'])
            url = pr['comments_url']
            params = ut.getParams()
            if params:
                url += '?' + urllib.parse.urlencode(params)
            print('Comments url :', url)
            print('Looking at comments of issue numbered', row_data['number'],'....')
            conn = urllib.request.urlopen(url)
            data = conn.read().decode()
            comments = json.loads(data)
            address_date = ''
            for comment in comments:
                author = comment['author_association']
                if(author == 'MEMBER' or author == 'CONTRIBUTOR'):
                    address_date = comment['created_at']
                    break
            if(address_date != ''):
                row_data['address_date'] = address_date
                rowdata.append(row_data)
        except:
            print('Caught an exception. Continuing now....')
            continue
#filename = js[0]['base']['repo']['name'] + '.csv'
    print('Storing data in', filename)
    csv_file = open(filename, "a+")
    writer = csv.DictWriter(csv_file, fieldnames=keys + ['address_date']) #,quoting = csv.QUOTE_NONNUMERIC)
    if first_page:
        writer.writeheader()
    for row in rowdata:
        try:
            writer.writerow(row)
        except:
            print('Caught an exception. Continuing now....')
            continue
    csv_file.close()
