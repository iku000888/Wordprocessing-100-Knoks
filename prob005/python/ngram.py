#assumes that input string contains no special characters.
#sequence must be contained in words.
def compute_word_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"

   #initialize empty set. This time ignoring frequency
   #https://docs.python.org/2/tutorial/datastructures.html
   ngram = set()

   #split into words. Easy for English.
   words = str.split(" ")

   for word in words:
      if len(word)>=n:#ignore words shorter than n
         #iteratively add the n grams of each word.
         #reusing is justice!
         ngram |= compute_char_n_gram(word,n) 
   return ngram;

#n gram that allows sequence to be formed across words.
def compute_char_n_gram( str,n ):
   "This returns the n-gram of the input string as a dictionary of n-gram"
   ngram = set()

   str = str.replace(" ","")
   for idx, val in enumerate(str):
      #if guard for end of the string
      if idx+n > len(str):
         break 
      ngram.add(str[idx:idx+n])
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
#unit test code below can be uncommented to see some test code.
#unittest()
