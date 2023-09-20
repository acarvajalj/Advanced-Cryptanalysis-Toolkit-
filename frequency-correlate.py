#!/usr/bin/env python3

import string
import sys
import os
import argparse
import math

#
# index-of-coincidence
# last-update:
#    31 aug 2023: bjr- modified from letter_utils.py

#
# usage: cat file | frequency_correlate.py _reference_
#
# the file is assumed to be a shift cipher, and the output gives
# information to solve for the shift amount.
#
# the letter frequencies of stdin v_i, as a normalized vector, is rotated
# by all j, v_(i+j mod 26) and the dot product of the rotated vector
# and a standard frequency count vector is printed. 
#
# the index of the put uses a==0, b==1, etc, to aid in key guessing
# 
#



def freq_count(text):
	# given a string text, all characters are in a-z, return
	# a vector of frequency counts.

	s = string.ascii_lowercase
	v = [0] * len(s)

# finish this function

	return v

def correlate_freqs(v1,v2,s):

	def shifted(i,s):
		return (i+s)%len(v1)

	assert len(v1)==len(v2)
	
	c = 0

# finish the this function

	return c
	
def main(argv):
	
	## gather test text 
	tt = ""
	for line in sys.stdin:
		for c in line:
			if c.isalpha():
				tt += c.lower()
				
	stf = open(sys.argv[1],'r')
	st = ""
	for line in stf.read():
		for c in line:
			if c.isalpha():
				st += c.lower()
	
	st_freq = freq_count(st)
	tt_freq = freq_count(tt)
	
	if is_debug:
		print("DEBUG")
		for i in range(len(st_freq)):
			print(f"{i}\t{st_freq[i]:.4f}\t{tt_freq[i]:.4f}")

	print(f'shift\tcorrelation\n---------------')
	for i in range(len(st_freq)):
		c = correlate_freqs(st_freq,tt_freq,i)
		print(f'{chr(ord("a")+i)}\t{c:.4f}')
		
main(sys.argv)

