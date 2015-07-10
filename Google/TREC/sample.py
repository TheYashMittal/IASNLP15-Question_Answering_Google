from sklearn.neighbors import KNeighborsClassifier
import nltk
import sys
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

clf = KNeighborsClassifier(n_neighbors=1)

vectorizer = CountVectorizer()
tfidf_vectorizer = TfidfTransformer()
sent = "What 's the second-most-used vowel in English ?"
pos=nltk.pos_tag(nltk.tokenize.word_tokenize(sent)) 
# print nltk.ne_chunk(pos, binary=True)
questions = []
X = []
XX = []
for ele in pos:
 	X.append("_".join([ele[0],ele[1]]))
for x in X:
	XX.append(" ".join(ele for ele in X[0:] ))
print XX[:2]
# print questions
# # sys.exit()
# X = tfidf_vectorizer.fit_transform(vectorizer.fit_transform(questions))
# clf.fit()
# print X

# print vec.get_feature_names()

# X = [[0,0,1], [1,0,0], [1,1,1], [0,0,0]]
# y = ['abc', 'caab', 'cab', 'a']
# clf.fit(X,y)

# print clf.predict([0, 0, 0])