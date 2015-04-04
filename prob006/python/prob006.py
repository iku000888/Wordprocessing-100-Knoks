#This program simply leverages the function ngram
#written for the previous problem, with the built 
#in set operation that python provides.

import sys
import ngram

#obtain the bigram of param 1 and 2
bigram_x = ngram.compute_char_n_gram(sys.argv[1],2)
bigram_y = ngram.compute_char_n_gram(sys.argv[2],2)

#string that will be checked its presence in the bi gram
qualifier = sys.argv[3]

print "bigrams of \""+ sys.argv[1] +"\": ", bigram_x
print "bigrams of \""+ sys.argv[2] +"\": ", bigram_y
print "union of the bigrams:", bigram_x|bigram_y
print "intersection of the bigrams:", bigram_x&bigram_y
print "difference of bigrams:", bigram_x - bigram_y
print "bigram \"" + qualifier + "\" contained in first?=>", qualifier in bigram_x
print "bigram \"" + qualifier + "\" contained in second?=>", qualifier in bigram_y
