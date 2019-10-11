
def countWords(s):
	words = s.split(" ")
	wordsDone = list()
	retDict = dict()
	
	for word in words:
		if word in wordsDone:
			continue
		count = words.count(word)
		# print("%s comes %d times" % (word, count))
		retDict.update({word: count})
		wordsDone.append(word)
	return retDict


print(countWords("the the the the the"))
print(countWords(""))
print(countWords("the quick fox quick the"))