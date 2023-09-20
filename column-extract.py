#!/usr/bin/env python3

import string
import sys
import os
import argparse
import math

#
# index-of-coincidence
# last-update:
#    31 aug 2023: bjr- modified from breaking-tools.py

#
# usage: cat file | column-extract.py _offset_ _skip_
#
# with the characters c_i in the file numbered c_0 c_1 c_2 ... 
# from stdin writes c_offset c_(offset+skip) c_(offset+2*skip) ... 
# to stdout
#
def extract(text, offset, skip):
    return text[offset::skip]

def main(argv):
	
	## gather test text 
	tt = ""
	for line in sys.stdin:
		for c in line:
			if c.isalpha():
				tt += c.lower()

	offset = int(sys.argv[1])
	skip = int(sys.argv[2])
	extracted = extract(tt,offset,skip)
	print(extracted)
		
main(sys.argv)

