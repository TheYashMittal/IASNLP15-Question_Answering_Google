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
from sklearn.neighbors import KNeighborsClassifier
import nltk
from sklearn.feature_extraction import DictVectorizer

# vec = DictVectorizer()
warnings.filterwarnings("ignore")

vectorizer = CountVectorizer()
tfidf_vectorizer = TfidfTransformer()
directory = os.getcwd()

def preProcessing(path, num=0):	# use num = 1 for coarse-grain classifier
	
	y = []
	X = []

	with open(directory + "\\" + path, "r") as f:
		print "In pre processing"
		fc = f.read().split('\n')
		for row in fc:
			pos_tags = []
			fc = row.split()
			if num == 0:
				label = fc[0]
			else:
				label = fc[0].split(':')[0]
			y.append(label)
			question = ""
			question += " ".join(ele.lower() for ele in fc[1:])
			tokens = nltk.tokenize.word_tokenize(question)
			pos = nltk.pos_tag(tokens) 
			for ele in pos:
			 	pos_tags.append("_".join([ele[0],ele[1]]))
			X.append(" ".join(ele for ele in pos_tags))

		print "preProcessing over"
	return X, y

def evaluateClassifier(questions, labels, clf):
	X_new_tfidf = tfidf_vectorizer.transform(vectorizer.transform(questions))
	scores = cross_validation.cross_val_score(clf, X_new_tfidf, labels, cv= 5, scoring="accuracy")
	print scores

def buildClassifier(questions, labels, classifierName):
	X = tfidf_vectorizer.fit_transform(vectorizer.fit_transform(questions))
	if classifierName == "KNN":
		clf = KNeighborsClassifier()
	elif classifierName == "MulNB":
		clf = MultinomialNB()
	clf = clf.fit(X,labels)
	return clf

def customQuestionScorer(question, clf):
	pos=nltk.pos_tag(nltk.tokenize.word_tokenize(question)) 
	qes = []
	X_f = []
	for ele in pos:
 		qes.append("_".join([ele[0],ele[1]]))
 	X_f.append(" ".join(ele for ele in qes))
	X_new_tfidf = tfidf_vectorizer.transform(vectorizer.transform(X_f))
	print clf.predict(X_new_tfidf)
	
def main():
	X_train = X_test = y_train = y_test = []

	classifierName = "KNN"
	print "Training"
	X_train, y_train = preProcessing("train_5500.label")
	print "Testing"
	X_test, y_test = preProcessing("TREC_10.label")
	
	print "Training"
	clf = buildClassifier(X_train, y_train, classifierName)
	
	print "Testing"
	evaluateClassifier(X_test, y_test, clf)
	
	q = "Who is the  director of IIIT?"
	customQuestionScorer(q, clf)
	

if __name__ == '__main__' :
	main()