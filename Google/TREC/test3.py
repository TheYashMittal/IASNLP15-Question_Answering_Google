import sys
import os
from collections import defaultdict
directory = os.getcwd()
word_counts = defaultdict(int)
for w in open(directory + "\\train_5500.label","r").read().split():
	if w.isalnum():
		word_counts[w.lower()] += 1

print len(word_counts.keys())
# print word_counts["hum:ind"]
# print word_counts["num:date"]


# for w,c in word_counts.iteritems():
 	# print w, "occurs", word_counts[w], "times"
# print sorted(word_counts.keys())