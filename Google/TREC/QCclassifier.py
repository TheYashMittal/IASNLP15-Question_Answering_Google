import os
import sys
import sklearn
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import grid_search
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn import svm
import pickle
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")

directory = os.getcwd()

if not os.path.isfile(directory + '\\' + 'X'):
	X = []
	y = []
	i = 1
	with open(directory + "\\train_1000.label", "r") as f:
		fc = f.read().split('\n')
		questions = []
		for row in fc: 
			print str(i) + '/5500'
			i += 1
			fc = row.split()
			label = fc[0]

			questions.append(" ".join(ele.lower() for ele in fc[1:]))
			y.append(label)

		tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
           stop_words='english')
		tfidf_matrix = tfidf_vectorizer.fit_transform(questions)
		X = tfidf_matrix

		with open(directory + '\\' + "X", "wb") as f:
			pickle.dump(X, f)
		with open(directory + '\\' + "y", "wb") as f:
			pickle.dump(y, f)
else:
	with open(directory + '\\' + "X", "rb") as f:
		X = pickle.load(f)
	with open(directory + '\\' + "y", "rb") as f:
		y = pickle.load(f)

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=1)

	parameters = {'kernel':('linear', 'rbf', 'poly', 'sigmoid'), 'degree': [1,2,3,4,5], 'C':[0.001, 0.01, 0.1, 1, 10, 100], \
								'coef0':[0.001,0.01,0.1,1,10,100], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100]}
								
	svr = svm.SVC()
	clf = grid_search.GridSearchCV(svr, parameters)
	clf.fit(X_train, y_train)
	# predicted = clf.predict(X_test)
	# print accuracy_score(y_test, predicted)
	scores = cross_validation.cross_val_score(clf, X_test, y_test, cv=5, scoring='f1')

	####################
	#F1 scores for the 5 cross validation runs
	#[ 0.24981061  0.27227002  0.28381432  0.19513575  0.30918367]
	####################
	print scores