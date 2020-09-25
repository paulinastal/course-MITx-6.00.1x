# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:18:44 2020

@author: Paulina
"""

balance = 3329
annualInterestRate = 0.2
lowestPayment = 10

updatedBalance = balance
monthlyInterestRate = (annualInterestRate) / 12.0
numberOfMonths = 12
unpaidBalance = 0
paid = False

while not paid:
    
    for i in range(numberOfMonths):
        unpaidBalance = updatedBalance - lowestPayment
        updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    
    if unpaidBalance < 0:
        paid = True
    else:
        lowestPayment += 10
        updatedBalance = balance
        
print("Lowest Payment: " + str(lowestPayment))
