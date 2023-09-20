#!/usr/bin/env python3

import string
import sys
import os
import argparse

#
# vigenere.py
#
# last update:
#    aug 2019: bjr- 
#    31 aug 2013: bjr- new style command line interface
#

# usage: cat text | ./vigenere _key_

# In this version, the case of the first letter streamed into 
# vignere decides whether vignere will encrypt or decrypt. 
# the convention is plaintext is lower case, ciphertext is upper case.
# If the first letter is lower case, the text is assumed plain and
# vigenere will encrypt and leave the output in upper case.
# If the first letter is upper case, the text is assumed enciphered and
# vigenere will decrypt and lave the out in lower case.

# The key is lowercase with numbering beginning at 0 for "a". This 
# somewhat defies convention, as rot13 is associated with the shift
# of 13 and with the letter "m" for middle, Or the Ceasar cipher is a
# shift of 3 associated with the letter "C" for Ceasar. 


is_debug = 0 
word_group = 5
line_group = 5

def vigenere_encipher(p,k):
	c = ""
	i = 0
	for pi in p:
		ki = ord(k[i]) - ord('a')
		pi = ord(pi) - ord('a')
		pi = (ki+pi)%26
		c += chr(ord('A')+pi)
		i += 1
		if i>=len(k):
			i = 0
	return c ;

def vigenere_decipher(c,k):
	p = ""
	i = 0
	for ci in c:
		ki = ord(k[i]) - ord('a')
		ci = ord(ci) - ord('A')
		ci = (ci-ki+26)%26
		p += chr(ord('a')+ci)
		i += 1
		if i>=len(k):
			i = 0
	return p ;


def main(argv):

	encode = -1

	## gather plain text and format
	## automatically determine if we are encoding or decoding
	t_in = ""
	for line in sys.stdin:
		for c in line:
			if c.isalpha():
				if encode==-1:
					if c.isupper():
						encode = 0
					else:
						encode = 1 
				if encode==1:
					c = c.lower()
				else:
					c = c.upper()
				t_in += c

	key = sys.argv[1]
	if encode==0:
		t_out = vigenere_decipher(t_in,key)
	else:
		t_out = vigenere_encipher(t_in,key)

	## pretty print ct
	i = 0
	s = ""
	r = word_group * line_group

	for c in t_out:
		s += c
		i += 1
		if i%word_group==0:
			s += ' '
		if i%r==0:
			s += '\n'
	print (s)

main(sys.argv)
