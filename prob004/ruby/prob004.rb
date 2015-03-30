#problem answer shows up in different prder from python implementation
#because the data structures used were different.

f = File.open(ARGV[0],"r")#sys call to read file
line = f.gets().gsub('.','')#trim .
wordList = line.split(" ")

#initialize an empty hashtable.
#http://ruby-doc.org/core-1.9.3/Hash.html
pdcTbl = Hash.new()

index = 1

#classical for each loop
wordList.each do |word|
   #http://stackoverflow.com/questions/1986386/check-if-value-exists-in-array-in-ruby
   if [1, 5, 6, 7, 8, 9, 15, 16, 19].include? index
      pdcTbl[word[0]]=index
   else
      #http://stackoverflow.com/questions/3525351/how-to-select-array-elements-in-a-given-range-in-ruby
      pdcTbl[word[0..1]]=index 
   end
   index+=1
   #puts word
end

pdcTbl.each_key do |key|
   puts key +" "+ pdcTbl[key].to_s
end
f.close()
