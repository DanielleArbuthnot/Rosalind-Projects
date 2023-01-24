# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:27:08 2023

@author: Danielle
"""

letters = input("What is the string?: ")

number1 = int(input("what is the 1st number?: "))
number2 = int(input("what is the 2nd number?: ")) +1
number3 = int(input("what is the 3rd number?: "))
number4 = int(input("what is the 4th number?: ")) +1

a = letters[number1:number2]

b = letters[number3:number4]

print (a + " " + b)