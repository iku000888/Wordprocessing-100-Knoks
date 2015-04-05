import sys
from random import shuffle
#separate input string into words.
words = open(sys.argv[1]).readline().split(" ")

newwords=""
#iterate each words.
for word in words:
   #if there are enough characters, shuffle the word.
   if len(word)>4:
      charlist=list(word[1:len(word)-1])
      shuffle(charlist)
      result = word[0]+''.join(charlist)+word[len(word)-1]
      newwords+=result+" "
   else:
      #other wise do not modify.
      newwords+=word+" "

#print "output:"
print newwords
