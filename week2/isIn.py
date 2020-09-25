# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:45:40 2020

@author: Paulina
"""
#mistake 
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0 or len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    tChar = int(len(aStr)/2)
    
    if char == aStr[tChar]:
        return True
    else:
        if ord(char) > ord(aStr[tChar]):
            aStr = aStr[tChar+1:]
            return isIn(char, aStr)
        else:
            aStr = aStr[:tChar]
            return isIn(char, aStr)
            
print(isIn("f", "aifjbd"))
            
            