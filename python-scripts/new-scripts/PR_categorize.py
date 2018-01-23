import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
os.chdir("E:\\6th sem pse lab\pull-the-work\python-scripts\\new-scripts")
tag = pd.read_csv("tensorflow.csv", encoding= "latin-1")
X=tag.title
y=tag.priority
X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=1)
vect = CountVectorizer(ngram_range=(1,3))
vect.fit(X_train)
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)
nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)
y_pred_class=nb.predict(X-test_dtm)
print(metrics.accuracy_score(y_test, y_pred_class))
y_pred_prob=nb.predict_proba(X_test_dtm)
print(y_pred_prob)

