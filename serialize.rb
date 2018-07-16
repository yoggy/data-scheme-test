#!/usr/bin/ruby

require 'json'
require 'base64'
require 'pp'

def usage
 puts "usage : #{$0} filename"
 puts ""
 puts "exampe : "
 puts "    $ #{$0} filename > test.json"
 exit(0)
end

usage if ARGV.size == 0 

ext = File.extname(ARGV[0]).downcase

img = ARGF.read()
img_base64 = Base64.encode64(img)

if ext == ".jpeg" || ext == ".jpg"
  header = "data:image/jpeg;base64,"
elsif ext == ".png"
  header = "data:image/png;base64,"
elsif ext == ".gif"
  header = "data:image/gif;base64,"
else
  header = "data:"
end

img_data_sheme = header + img_base64

h = {}
h["image"] = img_data_sheme

puts h.to_json

