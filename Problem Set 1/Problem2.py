#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 01:28:50 2020

@author: josephmendezona
"""

#finds number of times 'bob' occurs in string s

count = 0 #initialise count

for letter in range(len(s)): # #iterate over string s for length of bob
    if s[letter:letter+3] == 'bob': #if iteration = bob
        count += 1 #increase count
                
print('Number of times bob occurs is: ' + str(count))