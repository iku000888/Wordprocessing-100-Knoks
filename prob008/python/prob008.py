import sys

#http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
def cipher(sometext):
   newstr=""
   for c in sometext:
      if c.islower():
         newstr+= chr(219 - ord(c))
      else:
         newstr+= c
   #print newstr      
   return newstr

def decipher(sometext):
   newstr=""
   for c in sometext:
      if c.islower():
         newstr+= chr(219 - ord(c))
      else:
         newstr+= c
   #print newstr      
   return newstr


cipher(sys.argv[1])
