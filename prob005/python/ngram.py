def compute_word_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"

   #initialize empty dictionary
   #https://docs.python.org/2/tutorial/datastructures.html
   ngram = dict()

   #split into words. Easy for English.
   words = str.split(" ")

   for word in words:
      if len(word)>1:
         
         print len(word)
   print ngram
   print n
   return;

def compute_char_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"
   print str
   print n
   return;


def unittest():
   compute_word_n_gram("yolo I am a sitting duck",2)
   compute_char_n_gram("yolo I am a sitting duck",2)
   return;
#unit test code below.
unittest()
