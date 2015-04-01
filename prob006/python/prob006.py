import sys
import ngram

bigram_x = ngram.compute_char_n_gram(sys.argv[1],2)
bigram_y = ngram.compute_char_n_gram(sys.argv[2],2)

print bigram_x
print bigram_y

