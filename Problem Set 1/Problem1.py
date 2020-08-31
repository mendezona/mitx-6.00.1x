#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 01:27:01 2020

@author: josephmendezona
"""

#finds number of lowercase vowels for string input S

numVowels = 0 #initialise vowel count

for letter in s: #iterate over letters in string s
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u': #if vowel found
        numVowels += 1 #increase vowel count
        
print('Number of vowels: ' + str(numVowels))