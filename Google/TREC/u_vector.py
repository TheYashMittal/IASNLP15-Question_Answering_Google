#!/usr/bin/env python

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import SVC
import os
import sys
from sklearn import svm, grid_search, cross_validation, datasets
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
import sys, ast
from sklearn import neighbors
from sklearn.naive_bayes import MultinomialNB

'''
stopWords = stopwords.words('english')
vectorizer = CountVectorizer()
transformer = TfidfTransformer()


file1 = open("x_train.txt", 'r') 
s1 = file1.read().split("\n")
x_train_vector = vectorizer.fit_transform(s1)
file1.close()

file2 = open("x_test.txt", 'r') 
s2 = file2.read().split("\n")
x_test_vector = vectorizer.transform(s2)
file2.close()
	
X = transformer.fit_transform(x_train_vector)
x_test = transformer.transform(x_test_vector)
'''
directory = os.getcwd()
file1 = open(directory + "\\top_300_normal.txt","r+")
s1 = file1.read().split(" ")
#print len(s)

file2 = open(directory + "\\x_train.txt","r+")
s2 = file2.readline()

Matrix = [[0 for x in range(228)] for x in range(5452)] 

#print len(Matrix[555])
#print Matrix.shape[1]

i = -1
j = -1
while s2!='':
	s3 = s2.split(" ")
	i = i + 1
	for e in s3:
		j = j + 1
		if e in s1:
			Matrix[i][j] = 1
		else:
			Matrix[i][j] = 0
	
	j = -1
	s2 = file2.readline()
# print Matrix
Matrix = np.array(Matrix)
# print type(Matrix)
# sys.exit()

svm_parameters = {'kernel':(['linear']), 'C':[0.01, 0.1, 1, 10], 'gamma':[0.01, 0.1, 1]}
knn_parameters = {'weights': ['uniform', 'distance'], 'n_neighbors': [0, 0.2, 0.5, 1]}
mnb_parameters = {'alpha' : [0, 0.2, 0.5, 0.7, 0.9, 1], 'fit_prior':[True,False]}

file2 = open("y_train.txt", 'r') 
y = file2.read().split("\n")

clf = svm.SVC()
clf = grid_search.GridSearchCV(clf, svm_parameters)
# print len(y)
# sys.exit()
print "Built classifier"
# sys.exit()
clf = clf.fit(Matrix,y)
print "Finished"
'''
knn = neighbors.KNeighborsClassifier()
knn = grid_search.GridSearchCV(knn, knn_parameters)
knn.fit(X,y)

nb = MultinomialNB()
nb = grid_search.GridSearchCV(nb, mnb_parameters)
nb.fit(X,y)
'''
print "started"
scores = cross_validation.cross_val_score(clf, Matrix , y, cv=5, scoring = "accuracy")
print scores
print "Accuracy = ", scores.mean()

sys.exit()
clf.predict()


#classifier = Pipeline([
#    ('vectorizer', CountVectorizer(min_df=1,max_df=2)),
#    ('tfidf', TfidfTransformer()),
#    ('clf', OneVsRestClassifier(LinearSVC()))])
#classifier.fit(x_train_vector,y_train)
#predicted = classifier.predict(x_test_vector)

#predicted = clf.predict(x_test_vector)
#print accuracy_score(y_test, predicted)

#for item, labels in zip(x_test_vector, predicted):
#	print '%s => %s' % (item, ', '.join(distinct[x] for x in labels))
