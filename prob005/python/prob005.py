import sys

#How to deal with user defined modules
#https://docs.python.org/2/tutorial/modules.html
import ngram

f = open(sys.argv[1],'r')
ngram.computengram(f.readline,3)





#reference:http://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string
#remove new line,comma and period. rstrip does not work for commas.
#line = f.readline().rstrip('\n.').replace(',','')
#
#wordList = line.split(' ')
#pdcTable = {}
#for word in wordList:
#   if wordList.index(word)+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:#required by probstatement
#      pdcTable[word[0]]=wordList.index(word)+1
#   else:
#      pdcTable[word[0]+word[1]]=wordList.index(word)+1
#
##final output
#for key in pdcTable:
#   print key, pdcTable[key]

#very use ful tip below found:
#http://stackoverflow.com/questions/1676632/whats-a-quick-way-to-comment-uncomment-lines-in-vim
f.close()
