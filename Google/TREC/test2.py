import os
import sys
from collections import defaultdict
from collections import Counter
from nltk import word_tokenize
# a = {}
# a = defaultdict(int)

directory = os.getcwd()
questions = []
a = []
with open(directory + "\\" + "train_5500.label", "r") as f:
	fc = f.read().split("\n")
	for line in fc:
		# questions = []
		fc1 = line.split()
		for word in fc1[1:]:
			a.append(word.lower())
		# a.append(fc[1:])
		# print a
		# print a
		# sys.exit()
	# print a[]
	# print len(a)
	# sys.exit()
	b = []
	b = list(set(a))
	print len(b)
	# print type(questions)
	