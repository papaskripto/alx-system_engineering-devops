#!/usr/bin/env ruby
# puts ARGV[0].scan(/\[SENDER:(.*?)\]\[RECEIVER:(.*?)\]\[FLAGS:(..?[0-9]..?[0-9]..?[0-9]..?[0-9])\]/).join(",")
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
