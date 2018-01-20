import json
import recRetrieve as rec
import utilities as ut
import urllib
import csv

def action(data):
    js = json.loads(data)
    #print(js[0])
    #for item in js:
    #    print(item)
    if js:
        print('I am inside')
        filename = js[0]['head']['repo']['name'] + '.csv'
        print('Filename:', filename)
        #filename = 'tsflow1.csv'
        csv_file = open(filename, "a+")
        writer = csv.writer(csv_file, quoting = csv.QUOTE_NONNUMERIC)
        row = ['title',
            '#commits',
            'additions',
            'deletions',
            'changed_files',
            'author_association']
        writer.writerow(row)
    for pull_req in js:
        url = pull_req['url']
        conn = urllib.request.urlopen(url)
        data = conn.read().decode()
        pr = json.loads(data)
        title = pr['title']
        commits = pr['commits']
        additions = pr['additions']
        deletions = pr['deletions']
        changed_files = pr['changed_files']
        author_assoc = pr['author_association']
        row = [title,
            commits,
            additions,
            deletions,
            changed_files,
            author_assoc]
        writer.writerow(row)
        print(title, changed_files)
        break
    csv_file.close()
