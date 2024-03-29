# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
from isWordGuessed import isWordGuessed
from getGuessedWord import getGuessedWord
from getAvailableLetters import getAvailableLetters

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

    lettersGuessed = ""
    numberOfGuesses = 8
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")

    while numberOfGuesses > 0:
        
        print("You have " + str(numberOfGuesses) + " guesses left.")
        print("Available Letters: " + str(getAvailableLetters(lettersGuessed)))
        
        guess = input("Please guess a letter: ")
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print("-----------")
        else:
            if guess not in secretWord:
                lettersGuessed = lettersGuessed + guess
                print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                print("-----------")
                numberOfGuesses -= 1
            else:
                lettersGuessed = lettersGuessed + guess
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))) 
                print("-----------")
                
                
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            return None
        
        

    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
    return None

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = "left"
hangman(secretWord)
