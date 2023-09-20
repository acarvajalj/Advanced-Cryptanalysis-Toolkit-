#!/usr/bin/env python3

import string
import sys
import os
import argparse
import math

#
# index-of-coincidence
# last-update:
#    31 aug 2023: -bjr modified from breaking-tools.py
#     2 sep 2023: -bjr

#
# usage: cat file | index-of-coincidence.py _n_
#
# the index of coincidence of the file at stdin is computed for
# circulations of the input string 0, 1, etc up to n-1. 
# the outputs are normalized to 0.0 to 1.0.
#
# if s_i is the character sequence of stdin, and t_i is that sequence
# shifted by some amount, wrapping around at the end of the sequence, 
# then the index of coincidence is roughly the sum_i of s_i*t_i.
#

def run_ioc(tt, mo):
    total_chars = len(tt)
    print("off.\tcoincidence\n------------")
    for i in range(mo):
        coincidences = sum([1 for j, char in enumerate(tt) if char == tt[(j+i)%total_chars]])
        x = coincidences / total_chars
        print(f'{i}\t{x:4f}')

def main(argv):
	
	## gather test text 
	tt = ""
	for line in sys.stdin:
		for c in line:
			if c.isalpha():
				tt += c.lower()
	max_offset = int(sys.argv[1])
	run_ioc(tt, max_offset)
	
main(sys.argv)

