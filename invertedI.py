import glob   
from collections import defaultdict
from string import punctuation
special = list(set(punctuation)) # special characters which we need to remove
path = r"C:\Users\Tvarita Jain\Inverted-index\*.txt" #change it to your path!
files=glob.glob(path)
inverted= defaultdict(lambda: defaultdict(set))
freq = defaultdict(int) # dicitonary with the frequency of each word
fileNames = []
#print(defaultdict(set))
#print(len(files))
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
def searchsubseq(string):
	y = string.split()
	o=[]
	final=[]
	for each in y:
		for key in inverted[each]:
			o.append(key)
	for doc in o:
		if(o.count(doc)<=1):
			o.remove(doc)
	o=list(set(o))
	ctr=len(y)
	if(ctr==3):
		for key in o:
			s=inverted[y[0]][key]
			t=inverted[y[1]][key]
			u=inverted[y[2]][key]
			for pos in s:
				for pos2 in t:
					if(pos2==pos+1):
						for pos3 in u:
							if(pos3==pos2+1):
								final.append(key)
		return(list(set(final)))
	if(ctr==2):
		for key in o:
			s=inverted[y[0]][key]
			t=inverted[y[1]][key]
			for pos in s:
				for pos2 in t:
					if(pos2==pos+1):
						final.append(key)
		return(list(set(final)))

def subseqnsubseq(string):
	sub = string.split('AND')
	y=[]
	for each in sub:
		y.append(searchsubseq(each))
	a=Set(y[0])
	b=Set(y[1])
	final = a.intersection(b)
	for i in final:
		print(i,":",fileNames[i-1])

def distcount(string):
	sub = string.split(' ')
	
	a=list(sub[1])
	x=int(a[-1])
	

	sub.remove(sub[1])

	o=[]
	final=[]
	for each in sub:
		for key in inverted[each]:
			o.append(key)
	for doc in o:
		if(o.count(doc)<=1):
			o.remove(doc)
	o=list(set(o))
	
	for key in o:
			s=inverted[sub[0]][key]

			t=inverted[sub[1]][key]
			for pos in s:
				for pos2 in t:
					if(abs(pos2-pos)<=x+1):
						final.append(key)
	final=list(Set(final))
	for i in final:
		print(i,":",fileNames[i-1])




	
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

#for key1 in inverted['frog']:
	#print(inverted['frog'][key1])
	#break
#print(inverted)
#y=Set(inverted[0]['There'])
#print(y)

print("Query for any AND any type : snake AND frog")
intersectQ("snake AND frog")
print()
print("Query for any OR any type: snake OR frog")
unionQ("snake OR frog")
print()
print("Query for a string: snake")
search("snake")
print()
print("Query for a subsequence: There was a")
x=searchsubseq("there was a")
for i in x:
		print(i,":", fileNames[i-1])
print()
print("Query for a subsequence AND a subsequence: There was a AND One day")
subseqnsubseq("there was a AND one day")
print()
print("Query for a distance count between two words:why /2 you")
distcount("why /2 you")
print()
print("Query for a distance count between two words:proved /2 entertainer")
distcount("proved /3 entertainer")
print()


    
