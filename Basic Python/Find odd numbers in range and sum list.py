# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:41:06 2023

@author: Danielle
"""

a = int(input("What is the 1st number?: "))
b = int(input("What is the 2nd number?: "))+1

oddnum = []

for i in range (a,b,1):
    if i % 2 != 0:
        oddnum.append(i)

c = sum(oddnum)

print ("The sum of all odd numbers between " + str(a) + " and " + str(b) + " is " + str(c))