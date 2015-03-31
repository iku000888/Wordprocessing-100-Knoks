def compute_word_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"

   #initialize empty dictionary
   #https://docs.python.org/2/tutorial/datastructures.html
   ngram = set()

   #split into words. Easy for English.
   words = str.split(" ")

   for word in words:
      if len(word)>=n:#ignore words shorter than n
         #print word
         #print compute_char_n_gram(word,n)
         #print len(word)
         ngram |= compute_char_n_gram(word,n) 
   #print ngram
   #print n
   return ngram;

def compute_char_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"
   ngram = set()

   str = str.replace(" ","")
   for idx, val in enumerate(str):
      #if guard for end of the string
      if idx+n > len(str):
         break 
      ngram.add(str[idx:idx+n])
      #print idx, val
      #print str[idx:idx+n]
   #print str
   #print ngram
   return ngram;


def unittest():
   print "word test"
   print compute_word_n_gram("yolo I am a sitting duck",2)
   print compute_word_n_gram("yolo I am a sitting duck",3)
   print compute_word_n_gram("yolo I am a sitting duck",4)
   print compute_word_n_gram("yolo I am a sitting duck",5)
   print "char tests:"
   print compute_char_n_gram("yolo I am a sitting duck",2)
   print compute_char_n_gram("yolo I am a sitting duck",4)
   print compute_char_n_gram("yolo I am a sitting duck",7)
   return;
#unit test code below.
#unittest()
