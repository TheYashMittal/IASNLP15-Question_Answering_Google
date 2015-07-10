import sys
import os
import nltk

directory = os.getcwd()
label = []
f = open(directory + "\\train_5500.label", "r")
for line in f.read().split("\n"):
	l = line.split()
	label.append(l[0])
	# print line
	# sys.exit()
label = set(label)
ll = []