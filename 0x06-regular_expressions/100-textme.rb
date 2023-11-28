#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([(\+\w{3})(\w+)]+).+to:([(\+\w{3})(\w+)]+).+flags:([-?\d:]+)/).join(",")