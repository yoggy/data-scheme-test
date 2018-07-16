#!/usr/bin/ruby

require 'json'
require 'base64'
require 'pp'

def usage
 puts "usage : "
 puts "    $ ./serialize.rb nike.jpg | #{$0} test.jpg"
 exit(0)
end

usage if ARGV.size == 0 
filename = ARGV[0]

json_str = $stdin.read

h = JSON.parse(json_str)
img_data_scheme = h["image"]

if img_data_scheme.index(",")
  img_base64 = img_data_scheme.split(",")[1]
else
  img_base64 = img_data_scheme.split(":")[1]
end

img = Base64.decode64(img_base64)

open(filename, "wb").write(img)

