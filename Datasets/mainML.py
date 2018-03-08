import pandas as pd
import re
import copy
import numpy as np
import matplotlib.pyplot as plt


def dateToList(s):
    vals = re.findall(r'[\d]+', s)
    nums = [int(v) for v in vals]
    return copy.deepcopy(nums)


def subDates(s2,s1):
    l1=dateToList(s1)
    l2=dateToList(s2)
    days = (l2[0]- l1[0])*365 + (l2[1]- l1[1])*30 + (l2[2]- l1[2])
    return days

def auth_assoc(s):
    if(s=="OWNER"):
        return 4
    elif(s=="MEMBER"):
        return 3
    elif(s=="CONTRIBUTOR"):
        return 2
    elif(s=="NONE"):
        return 1
    else:
        return 0

def classify_closeTime(i):
    cat0=[i for i in range(0,3)]
    cat1=[i for i in range(3,8)]
    cat2=[i for i in range(8,15)]
    cat3=[i for i in range(15,28)]
    if (i in cat0):
        return 0
    elif(i in cat1):
        return 1
    elif(i in cat2):
        return 2
    elif(i in cat3):
        return 3
    else:
        return 4

csv = pd.read_csv("test.csv",encoding="latin-1")
c = csv['closed_at']
o = csv["created_at"]
aa = csv['author_association']


# C_T=[subDates(cl,ol) for cl,ol in zip(c,o)]
# csv['Closing_time']= C_T
# aap =[auth_assoc(s) for s in aa]
# csv['Author_Priority']= aap
# ctc = [classify_closeTime(i) for i in csv["Closing_time"]]
# csv["Closetime_class"]=ctc
# csv.to_csv('test.csv',sep=",",encoding="latin-1")
# print("done!")


# l =[0]*80
# for i in csv["Closing_time"]:
#     l[i]+=1
# print(l)


# x = [i for i in range(0,80)]
# y=[l[i] for i in x]
# plt.plot(x,y,label = "number of points", color = 'r')
# plt.xlabel("days")
# plt.ylabel("number")
# plt.legend()
# plt.show()
# print(classify_closeTime(0))


ap = csv['Author_Priority']
a = csv['assignees']
co = csv['comments']
clo = csv['Closetime_class']
X_= [[api,ai,coi] for api,ai,coi in zip(ap,a,co)]
y_ =[cli for cli in clo]
X = np.array(X_)
y = np.array(y_)

from sklearn.neighbors import KNeighborsClassifier #max at n_neihbors = 5 mean =48.989%
# knn = KNeighborsClassifier(n_neighbors=1)
# from sklearn.model_selection import GridSearchCV
# k_range = [i for i in range(1,31)]
# param_grid = dict(n_neighbors = k_range)
# grid = GridSearchCV(knn,param_grid,cv=10,scoring="accuracy")
# grid.fit(X,y)
# print(grid.grid_scores_)



from sklearn.model_selection import train_test_split
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.9, random_state=1)

from sklearn.linear_model import LogisticRegression#52.8846%
# logreg = LogisticRegression()
# logreg.fit(X_train,y_train)
# y_pred = logreg.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))


from sklearn.tree import DecisionTreeClassifier #54.807%
#
# tree1 = DecisionTreeClassifier(max_depth=2)
# tree1.fit(X_train,y_train)
# y_pred = tree1.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))


from sklearn.ensemble import RandomForestClassifier#49- 51%
# rnd_forest = RandomForestClassifier()
# rnd_forest.fit(X_train,y_train)
# y_pred = rnd_forest.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))


from sklearn.svm import SVC #54.807%
# svmCls = SVC(probability=True)
# svmCls.fit(X_train,y_train)
# y_pred = svmCls.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))


from sklearn.ensemble import VotingClassifier#55.769%
rnd_forest = RandomForestClassifier()
logreg = LogisticRegression()
tree1 = DecisionTreeClassifier(max_depth=2)
svmCls = SVC(probability=True)
es =[("rf",rnd_forest),("lr", logreg),("dt",tree1),("svc",svmCls)]
voting_cls = VotingClassifier(estimators=es,voting="soft")
voting_cls.fit(X_train,y_train)
y_pred = voting_cls.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))





