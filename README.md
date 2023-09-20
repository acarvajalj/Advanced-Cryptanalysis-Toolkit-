## Breaking Vigenere

Finish these three python functions according to the program descriptions.
Then use the programs to discover the keys for the two challenge ciphertexts.

### A few notes

Helen Fouche Gaines' book
Cryptanalysis: A Study of Ciphers and Their Solution adopts
the convention of blocks of five letters, where lower case is 
the plain text, and upper case is the cipher text. All 
punctuation and spacing is suppressed, except to format the
5 letter blocks, typically 5 blocks per line.

This seems to be how it was done, as also William F. Friedman's Military Cryptanalysis Part 1
uses this convention (Aegean Park Press is now out of business, so this book is hard to get.)

### Breaking a Caesar Cipher

The Caesar cipher is a simple substitution cipher whose rule is, for each letter
shift it forward by i steps in the alphabet, wrapping over from z to a. The key is 
the number i.

It is broken by matching the frequency distribution of the cipher text with a 
reference distribution, to determine an i that makes the distributions overlap 
most completely. The program frequency-correlation.py does the math, trying
all 26 possible shifts and reports the quality of the overlap.

### Breaking a Vigenere Cipher

Noting the simplicity of breaking a Caesar, Vigenere augments the process
by having a sequence of Ceasars, used for successive letters in the text. 
The sequence, being finite, will repeat in a cyclic fashion when reaching 
the of the sequence. If the shift
amounts are identified with letters, then the key can be a word or a phrase.

To the code breaker, the length of the key is unknown. If the key length was known, 
the cipher text is disassembled into columns a distance apart equal to the key length, 
and each part broken as a Ceasar. The program column-extract.py helps with this.

To find the key length, the text is slid past itself looking for peaks in the 
number of coincidences of letters in the same place between the two texts. 
These peaks will be at the rhythm of the key length. The program index-of-coincidence.py 
does the math and prints out the coincidence frequency.

