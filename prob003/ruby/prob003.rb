#http://stackoverflow.com/questions/7157207/how-can-i-read-a-file-with-ruby
contents = File.read(ARGV[0])

#http://stackoverflow.com/questions/17348539/how-to-strip-commas-from-float-input
contents = contents.gsub(',','').gsub('.','')

#http://stackoverflow.com/questions/13537920/ruby-split-by-whitespace
contents = contents.split(' ')

contents.each do |word|
   puts word.length
end

#http://www.rubylife.jp/ini/for/index5.html
#puts contents

