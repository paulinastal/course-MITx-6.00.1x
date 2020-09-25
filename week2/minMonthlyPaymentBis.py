# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:39:58 2020

@author: Paulina
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

updatedBalance = balance
unpaidBalance = 0
numberOfMonths = 12
lowestPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
paid = False

while not paid:
    
    for i in range(numberOfMonths):
       unpaidBalance = updatedBalance - lowestPayment
       updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
        
    if  -0.01 < unpaidBalance < 0:
        paid = True
        
    elif unpaidBalance > 0:
        monthlyPaymentLowerBound = lowestPayment
        lowestPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
        updatedBalance = balance
        
    else:
        monthlyPaymentUpperBound = lowestPayment
        lowestPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
        updatedBalance = balance
        
print("Lowest Payment: " + str(round(lowestPayment, 2)))