import sys

#How to deal with user defined modules
#https://docs.python.org/2/tutorial/modules.html
import ngram

f = open(sys.argv[1],'r')
line = f.readline().rstrip('\n.')
#print line

print "word n gram:"
print ngram.compute_word_n_gram(line,2)
print "character n gram:"
print ngram.compute_char_n_gram(line,2)

#very use ful tip below found:
#http://stackoverflow.com/questions/1676632/whats-a-quick-way-to-comment-uncomment-lines-in-vim
f.close()
