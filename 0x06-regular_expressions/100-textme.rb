#!/usr/bin/env ruby
puts ARGV[0].scan(/from.{1}([(\+\w{3})(\w+)]+).+to.{1}([(\+\w{3})(\w+)]+).+flags.{1}([-?\d:]+)/).join(",")