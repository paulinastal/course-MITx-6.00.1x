# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:24:39 2020

@author: Paulina
"""

s = 'zyxwvutsrqponmlkjihgfedcba'
count = 1
max = 0
last = 0

for i in range(len(s)-1):
    
    if ord(s[i+1]) >= ord(s[i]):
        count += 1 
    
    if ord(s[i+1]) < ord(s[i]):
        count = 1
        
    if max < count:
        max = count
        last = i
        
        
if (max == 1):   
    print("Longest substring in alphabetical order is:", s[0])

else:
    print("Longest substring in alphabetical order is:" ,s[last-max+2:last+2])
  

    
    