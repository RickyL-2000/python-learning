#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def puts(msg):
    print("\n%s%s%s\n" % ('\033[93m', "➜ ", msg))

if len(sys.argv) < 2:
    print("Usage: %s <filename>" %  ( sys.argv[0]))
    sys.exit(0)

input_file = sys.argv[1]
output_file = "%s%s" % (input_file[:-4], ".png")

with open(input_file, "rb") as f:
    binary = f.read(89773)[47:]

puts('Exports %s from %s' % ( output_file, input_file ))

for i in range(0, len(binary)):
    if (i % 2) == 0:
	with open(output_file,'ab') as f:
            f.write(binary[i])
