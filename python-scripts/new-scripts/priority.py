import numpy as np
import pandas as pd
from collections import Counter
from operator import attrgetter
# data analysis:
# 1. age
# 2. comments
# 3. author_association
# 4. assignees
# Steps:
# A. Write scripts for each one of them.
# B. We then weigh them in some fashion.
# C. Find final priority.

def readFromCSV(filename):
    '''returns a dataframe with data from the input csv file'''
    return pd.read_csv(filename, encoding = 'latin-1')

class Issue:
    def __init__(self, number, title, comments, assignees, created_at, author_assoc):
        self.comments = comments
        self.assignees = assignees
        self.created_at = created_at
        if(author_assoc == 'MEMBER'):
            self.author_assoc = 1
        elif(author_assoc == 'CONTRIBUTOR'):
            self.author_assoc = 2
        else:
            self.author_assoc = 3
        self.title = title
        self.number = number

    def to_dict(self):
        if(self.author_assoc == 3):
            author = 'NONE'
        elif(self.author_assoc == 2):
            author = 'CONTRIBUTOR'
        else:
            author = 'MEMBER'
        return {
            'title': self.title,
            'number': self.number,
            'author_association': author,
            'comments': self.comments,
            'assignees': self.assignees,
            'created_at': self.created_at
        }

def get_issue_list(df):
    length = df.shape[0]
    issue_list = np.array([])
    for i in range(length):
        series = df.iloc[i,:]
        title = series['title']
        comments = series['comments']
        assignees = series['assignees']
        created_at = series['created_at']
        author = series['author_association']
        number = series['number']
        issue = Issue(number, title, comments, assignees, created_at, author)
        issue_list = np.append(issue_list, issue)
    return issue_list

def getPriorityOrder():
    print('Specify Priority order as: ')
    print('1. author association')
    print('2. date created')
    print('3. assignees')
    print('4. comments')
    priority = input('Enter 4 space separated intergers: ')
    priority = list(map(int, priority.split(' ')))
    if(Counter(priority) == Counter([1,2,3,4])):
        return list(reversed(priority))
    else:
        raise Exception('Incorrect priority order input')

def sortIssues(priority, issue_list):
    priority_map = {1: 'author_assoc', 2: 'created_at',
                3: 'assignees', 4: 'comments'}
    key = priority[0]
    rev = False
    if(key == 3 or key == 4):
        rev = True
    sorted_list = sorted(issue_list, key = attrgetter(priority_map[key]), reverse = rev)
    for key in priority[1:]:
        rev = False
        if(key == 3 or key == 4):
            rev = True
        sorted_list.sort(key = attrgetter(priority_map[key]), reverse = rev)
    return sorted_list

def getDataFrame(sorted_issues):
    df = pd.DataFrame.from_records([issue.to_dict() for issue in sorted_issues])
    return df.set_index('number')

def runTool():
    print('[1] Welcome to Issue Prioritizer')
    filename = input('Enter csv filename to read issues')
    print('[2] Reading issues from csv file...')
    df = readFromCSV(filename)
    print('[3] Data frame created.')
    print('[4] Converting data frame to issue list...')
    issues = get_issue_list(df)
    print('[5] Issue list created.')
    print('[6]')
    priority = getPriorityOrder()
    print('[7] Sorting issues as per the priority...')
    sorted_issues = sortIssues(priority, issues)
    print('[8] Converting back to Data Frame...')
    print('[9] Returning sorted issues...')
    return getDataFrame(sorted_issues)
