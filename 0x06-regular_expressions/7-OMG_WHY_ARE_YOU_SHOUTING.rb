#!/usr/bin/env ruby
# A regular expression it only  matches the capital letters
puts ARGV[0].scan(/[A-Z]/).join
