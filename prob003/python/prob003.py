import sys
f = open(sys.argv[1],'r')#sys call

#reference:http://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
#remove new line,comma and period. rstrip does not work for commas.
line = f.readline().rstrip('\n.').replace(',','')

wordList = line.split(' ')
for word in wordList:
   print len(word)

f.close()
