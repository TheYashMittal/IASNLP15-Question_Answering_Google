import os
import operator
from collections import defaultdict

directory = os.getcwd()
labels = defaultdict(int)

def c(token):
	labels[token] += 1

with open(directory + "\\train_5500.label", "r") as f:
			fc = f.read().split('\n')
			for row in fc: 
				vector = []
				fc = row.split()
				try:
					c(fc[0])
				except:
					continue

print sorted(labels.items(), key=operator.itemgetter(1))
