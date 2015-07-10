import os
import sys
from collections import defaultdict
dic = {}
dic = defaultdict(int)
def counter(q):
	dic[q]= dic[q] + 1

directory = os.getcwd()
with open(directory + "\\" + "train_5500.label", "r") as f:
	fc = f.read().split('\n')
	questions = []
	for row in fc: 
		fc = row.split()
		print type(fc)
		# print row.split()[1]
		# sys.exit()
		# print row
		# row = fc[1:].split()[0]
		# row = row.split()
		# print row[0:].split()
		# sys.exit()
		questions.append(ele for ele in fc[1:])
		# questions.append()
		# print type(questions)
		print questions
		sys.exit()

	for q in questions:
		print q
		sys.exit()

	
	# a = list(set(questions))
	# print len(a)

