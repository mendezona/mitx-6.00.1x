#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:49:09 2020

@author: josephmendezona
"""

#iterates over string s and prints the longest substring of s in which the letters occur in alphabetical order

previousLetter = 'a' #initialise letter

positionInS = 0 #initialise position in string s
currentLength = 0 #initialise counter of length

highscoreLength = 0 #record length of substring
highscorePos = 0 #record position of substring


for letter in s: #iterate over string in s and take one letter
    if letter >= previousLetter: #if letter is greater than previous letter
           
        currentLength += 1 #+1 to current length count            
        if currentLength > highscoreLength: #if current substring length is higher than current highscore substring
            highscoreLength = currentLength #replace length
            highscorePos = positionInS #record position of new substring
        
    else: #if letter is less than previous letter
        currentLength = 1 #reset current length count
        
    previousLetter = letter #reset letters
    positionInS += 1 #record position as a number
    
if highscorePos-highscoreLength > 0:
    print('Longest substring in alphabetical order is:', s[highscorePos-(highscoreLength-1):highscorePos+1])
    
if highscorePos-highscoreLength == 0:
    print('Longest substring in alphabetical order is:', s[1:highscorePos+1])
    
if highscorePos-highscoreLength < 0:
    print('Longest substring in alphabetical order is:', s[:highscorePos+1])

    
