import sys
import ngram

bigram_x = ngram.compute_char_n_gram(sys.argv[1],2)
bigram_y = ngram.compute_char_n_gram(sys.argv[2],2)
qualifier = sys.argv[3]

print "bigrams of \""+ sys.argv[1] +"\": ", bigram_x
print "bigrams of \""+ sys.argv[2] +"\": ", bigram_y
print "union of the bigrams:", bigram_x|bigram_y
print "intersection of the bigrams:", bigram_x&bigram_y
print "difference of bigrams:", bigram_x - bigram_y
print "bigram \"" + qualifier + "\" contained in first?=>", qualifier in bigram_x
print "bigram \"" + qualifier + "\" contained in second?=>", qualifier in bigram_y
