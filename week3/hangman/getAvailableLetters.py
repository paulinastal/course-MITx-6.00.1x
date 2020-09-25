import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = string.ascii_lowercase
    
    for letter in lettersGuessed:
        if letter in availableLetters:
            availableLetters = availableLetters.replace(letter, "")
    
    return availableLetters