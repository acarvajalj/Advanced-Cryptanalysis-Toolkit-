#
# makefile for proj2
# last update: 
#     30 aug 2021 -bjr
#      1 sep 2023 -bjr
#


CHALLENGE_1_KEY= dorothy
CHALLENGE_2_KEY= lotharwitzke

ST= standard-text.txt
CT= ciphertext.txt
REF_FILE= standard-text.txt

OFFSET ?= 0
SKIP ?= 12
IOC_LIMIT = 50

PY= python3

KEY= abc

all:
	@echo "Read the Makefile!"

encode:
	cat ${ST} | ${PY} vigenere.py ${KEY} > ${CT}
	
ioc: 
	cat ${CT} | ${PY} index-of-coincidence.py ${IOC_LIMIT}

cols:
	cat ${CT} | ${PY} column-extract.py ${OFFSET} ${SKIP} > temp.txt

freq:
	cat temp.txt | ${PY} frequency-correlate.py ${ST}

challenge-1: 
	cat challenge-1.txt | ${PY} vigenere.py ${CHALLENGE_1_KEY} > challenge-1-solved.txt
	echo "submit secret-message.txt as your solution"

challenge-2: 
	cat challenge-2.txt | ${PY} vigenere.py ${CHALLENGE_2_KEY} > challenge-2-solved.txt
	echo "submit secret-message.txt as your solution"

clean:
	-rm ${CT} temp.txt challenge-1-solved.txt challenge-2-solved.txt
	

