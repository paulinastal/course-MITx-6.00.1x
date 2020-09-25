# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:45:09 2020

@author: Paulina
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

minimumPayment = 0
unpaidBalance = 0
interest = 0
numberOfMonths = 12


for i in range (numberOfMonths):
    
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = (annualInterestRate / 12) * unpaidBalance
    balance = unpaidBalance + interest
    
    #print("Month " + str(i+1) + ": " + str(round(balance, 2)))
    
print("Remaining balance: " + str(round(balance, 2)))