"""
Joining consonants and vowels in python

"""

import re

def vowels_constants(word):
    return [g for g in re.split(r'([aeiou]+?[^aeiou]+?)', word, flags=re.I) if g]

if __name__ == '__main__':
	word = 'house'
	print vowels_constants(word)
