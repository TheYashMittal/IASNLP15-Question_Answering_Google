import os
import sys
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import grid_search
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
import warnings
from sklearn import svm
from sklearn.svm import SVC

warnings.filterwarnings("ignore")

vectorizer = CountVectorizer(ngram_range = (1,2))
tfidf_vectorizer = TfidfTransformer()
directory = os.getcwd()

def preProcessing(path, num=0):	# use num = 1 for coarse-grain classifier
	X = []
	y = []

	with open(directory + "\\" + path, "r") as f:
		for row in f.read().split('\n'): 
			fc = row.split()
			if num == 0:
				label = fc[0]
			else:
				label = fc[0].split(':')[0]
			X.append(" ".join(ele.lower() for ele in fc[1:]))
			y.append(label)
			
	return X, y

def evaluateClassifier(questions, labels, clf):
	X_new_tfidf = vectorizer.transform(questions)
	X_new_tfidf = tfidf_vectorizer.transform(X_new_tfidf)
	scores = cross_validation.cross_val_score(clf, X_new_tfidf, labels, cv= 5, scoring="accuracy")
	print scores

def buildClassifier(questions, labels, classifierName):
	X_old = vectorizer.fit_transform(questions)
	X_old = tfidf_vectorizer.fit_transform(X_old)
	# print type(X_old)
	# sys.exit()
	# clf = KNeighborsClassifier()
	if classifierName == "KNN":
		parameters = {'weights': ['uniform', 'distance'], 'n_neighbors': [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
		clf = KNeighborsClassifier()
		clf = grid_search.GridSearchCV(clf, parameters)
		return clf.fit(X_old, labels)
	elif classifierName == "MNB":
		parameters = {'alpha':[0, 0.2, 0.5, 0.7, 0.9, 1], 'fit_prior':[True, False]}
		clf = MultinomialNB()
		clf = grid_search.GridSearchCV(clf, parameters)
		return clf.fit(X_old, labels)
	elif classifierName == "SVM":
		parameters = {'kernel':(['linear']), 'C':[0.01, 0.1, 1, 10], 'gamma':[0.01, 0.1, 1]}
		clf = svm.SVC()
		clf = grid_search.GridSearchCV(clf, parameters)
		return clf.fit(X_old, labels)
	# clf = clf.fit(X_old, labels)
	# return clf

def customQuestionScorer(question, clf):
	X_new_tfidf = tfidf_vectorizer.transform(vectorizer.transform([question]))
	print clf.predict(X_new_tfidf)
	
def main():
	X_train = X_test = y_train = y_test = []

	classifierName = "SVM"
	
	X_train, y_train = preProcessing("train_5500.label")
	X_test, y_test = preProcessing("TREC_10.label")
	
	print "Training"
	clf = buildClassifier(X_train, y_train, classifierName)
	
	print "Testing"
	evaluateClassifier(X_test, y_test, clf)
	
	q = "Who is the  director of IIIT?"
	customQuestionScorer(q, clf)
	

if __name__ == '__main__' :
	main()