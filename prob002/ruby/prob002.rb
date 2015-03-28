#!/usr/bin/env ruby
#a for each syntax in ruby that works after version 1.8.7 apparantly...
#took from->http://stackoverflow.com/questions/1484952/iterating-over-each-character-of-a-string-in-ruby-1-8-6-each-char
index = 0;
outstr = ""
ARGV[0].each_char do |c|
    outstr = outstr + c + ARGV[1][index]
    index = index + 1
end
puts outstr

