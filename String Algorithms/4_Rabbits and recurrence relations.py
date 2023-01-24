# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:18:43 2023

@author: Danielle
"""

#https://rosalind.info/problems/fib/
#Task - Using the fibonacci sequence as a base, calculate the total number of rabbits 
#after n months when:
# + each adult pair prouces k kits per month
# + kits take 1 month to become adults and another month to produce offspring
# + no rabbits die

months = int(input("What is the number of months?: "))
kits = int(input("How many kit pairs per litter?: "))

newadults = 0
oldadults = 0
young = 1
total = 0

for i in range(1,months):
    newadults = oldadults + young
    young = oldadults * kits
    total = newadults + young
    oldadults = newadults
    print ("adults = " + str(oldadults) + ", young = " + str(young) + ", total = " + str(total))
    
print ("Total rabits = " + str(total))