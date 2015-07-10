import os
import sys
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import grid_search
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings("ignore")

directory = os.getcwd()

X = []
y = []
tfidf_vectorizer = TfidfTransformer()
vectorizer = CountVectorizer()
with open(directory + "\\train_5500.label", "r") as f:
	fc = f.read().split('\n')
	questions = []
	for row in fc: 
		fc = row.split()
		label = fc[0]

		questions.append(" ".join(ele.lower() for ele in fc[1:]))
		y.append(label)

	# pipeline = Pipeline([('vect', CountVectorizer(ngram_range=(1,3))), ('tfidf', TfidfTransformer()), ('clf', KNeighborsClassifier())])
	# clf = pipeline.fit(questions, y)
	# print clf
	# print clf.predict(["capital"])
	# # sys.exit()

	# ##############
	# vectorizer = CountVectorizer()
	X = vectorizer.fit_transform(questions)
	# tfidf_vectorizer = TfidfTransformer()
	X = tfidf_vectorizer.fit_transform(X)
	# clf = MultinomialNB(

	clf = KNeighborsClassifier()
	clf = clf.fit(X, y)
	# print clf.predict(vectorizer.transform(["animal"]).toarray())
	with open(directory + "\\TREC_10.label", "r") as f:
		fc = f.read().split('\n')
		questions = []
		X = []
		y = []
		for row in fc: 
			fc = row.split()
			label = fc[0].split(':')[0]

			questions.append(" ".join(ele.lower() for ele in fc[1:]))
			y.append(label)

		X = vectorizer.transform(questions)
		# tfidf_vectorizer = TfidfTransformer()
		X = tfidf_vectorizer.transform(X)
		#######################
		scores = cross_validation.cross_val_score(clf, X, y, cv=5, scoring="accuracy")
		# scores = cross_validation.ShuffleSplit(5, n_iter=3, test_size=0.25, random_state=10)
		print scores
	sys.exit()
	##############

# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=1)

parameters = {'alpha':[0, 0.2, 0.5, 0.7, 0.9, 1], 'fit_prior':[True, False]}
clf = MultinomialNB()
clf = grid_search.GridSearchCV(clf, parameters)
clf.fit(X, y)
print clf.predict(["capital"])
# scores = cross_validation.cross_val_score(clf, X_test, y_test, cv=5, scoring="accuracy")

##############################
with open(directory + "\\TREC_10.label", "r") as f:
	fc = f.read().split('\n')
	questions = []
	X = []
	y = []
	for row in fc: 
		fc = row.split()
		label = fc[0].split(':')[0]

		questions.append(" ".join(ele.lower() for ele in fc[1:]))
		y.append(label)

	tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True, analyzer='word', lowercase=True,
       stop_words='english')
	X = tfidf_vectorizer.fit_transform(questions)
#######################
scores = cross_validation.cross_val_score(clf, X, y, cv=5, scoring="accuracy")

####################
#F1 scores for the 5 cross validation runs
#[ 0.24981061  0.27227002  0.28381432  0.19513575  0.30918367]
####################
print scores