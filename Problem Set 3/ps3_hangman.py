#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:04:20 2020

@author: josephmendezona


Hangman game vs computer
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    
    for letter in secretWord:
        for guessLetter in lettersGuessed:
            if letter == guessLetter:
                count += 1
                break
                
    if len(secretWord) == count:
        return True
    
    else:
        return False
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    tempSecretWord = []
    for letter in secretWord:
        tempSecretWord.append(' _ ')
    
    count = 0
    for letter in secretWord:
        for guessLetter in lettersGuessed:          
            if letter == guessLetter:
                tempSecretWord[count] = letter
                
        count += 1
        
    guessedWord = 'a'
    for finalOutput in tempSecretWord:
        guessedWord += finalOutput
    
    return guessedWord[1:]


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for guessLetter in lettersGuessed:
        if alphabet.count(guessLetter):
            alphabet.remove(guessLetter)
    
    alphabet.sort()
    alphabetString = 'a'
    for finalOutput in alphabet:
        alphabetString += finalOutput
           
    return alphabetString[1:]
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    mistakesMade = 8
    lettersGuessed = []
    tempListSecretWord = []
    
    for letter in secretWord:
        tempListSecretWord.append(letter)
        
    while mistakesMade > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have', mistakesMade, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        
        if lettersGuessed.count(guessInLowerCase) > 0:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            
        else:
            lettersGuessed.append(guessInLowerCase)
            if tempListSecretWord.count(guessInLowerCase) > 0:
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                mistakesMade -= 1  
            
    print('-------------')
    if mistakesMade > 0:
         print('Congratulations, you won!')
    else:        
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')

# secretWord = 'apple'
# print(hangman(secretWord))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))