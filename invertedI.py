import glob   
from collections import defaultdict
from string import punctuation
special = list(set(punctuation)) # special characters which we need to remove
path = '/home/vishal97/IRtest/*.txt' #change it to your path!
files=glob.glob(path)
inverted= defaultdict(lambda: defaultdict(set))
freq = defaultdict(int) # dicitonary with the frequency of each word
fileNames = []
def Set(d):
	s = set()
	for i in d:
		s.add(i)
	return(s)
def removeSpecial(word): # to remove special characters, there could be a more optimal way to do it
	newWord = word
	for i in word:
		if(i in special):
			newWord = newWord.replace(i, "") #removing the special character if present in the string
	return(newWord)
def toLower(word): # making the words case insensitive
	newWord = word.lower()
	return(newWord)
def parse(string):
	i = string.rfind('/')
	return(string[i+1:])
def search(string):
	for i in inverted[string]:
		print(i,":", fileNames[i-1])
def intersectQ(string):
	l  = string.split()
	first = l[0]
	second = l[-1]
	a = Set(inverted[first])
	b = Set(inverted[second])
	interSet = a.intersection(b)
	for i in interSet:
		print(i,":", fileNames[i-1])
def unionQ(string):
	l = string.split()
	first = l[0]
	second = l[-1]
	a = Set(inverted[first])
	b = Set(inverted[second])
	interSet = a.union(b)
	for i in interSet:
		print(i,":", fileNames[i-1])
for i in range(len(files)):
	f=open(files[i], 'r')
	fileNames.append(parse(files[i]))
	j = 0
	for words in f.read().split(): #split by default splits it by space
		if(words in inverted):
			freq[words]+=1  # increase the value of the word which is a key by 1 when it's found
			inverted[words][i+1].add(j) # this adds the docid which is (i+1) and to it's set it adds the position
			j+=1
		else:
			words = removeSpecial(words)
			words = toLower(words)
			freq[words]+=1  # increase the value of the word which is a key by 1 when it's found
			inverted[words][i+1].add(j)
			j+=1
	f.close()

print("Query for any AND any type")
intersectQ("snake AND frog")
print()
print("Query for any OR any type")
unionQ("snake OR frog")
print()
print("Query for a string")
search("snake")
print()


    
