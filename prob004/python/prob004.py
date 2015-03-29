import sys
f = open(sys.argv[1],'r')#sys call

#reference:http://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
#remove new line,comma and period. rstrip does not work for commas.
line = f.readline().rstrip('\n.').replace(',','')

wordList = line.split(' ')
pdcTable = {}
for word in wordList:
   if wordList.index(word)+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:#required by probstatement
      pdcTable[word[0]]=wordList.index(word)+1
   else:
      pdcTable[word[0]+word[1]]=wordList.index(word)+1

#final output
for key in pdcTable:
   print key, pdcTable[key]

f.close()
