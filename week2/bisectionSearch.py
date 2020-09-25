# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:40:52 2020

@author: Paulina
"""

start  = 0
end = 100
guess = int((start + end)/2)

print("Please think of a number between 0 and 100!")
print("Is your secret number "+ str(guess) + "?", end = '')
number = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." + "\n")

while True:
    
    if number == "h":
        end = guess
        guess = int((start + end)/2)
        
    elif number == "l":  
        start = guess
        guess = int((start + end)/2)
         
    elif number == "c":
        print("Game over. Your secret number was:", guess)
        break
    
    else:
        print("Sorry, I did not understand your input.")
      
    print("Is your secret number " + str(guess) + "?", end = ' ')
    number = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." + "\n")
 
   
        
   
    