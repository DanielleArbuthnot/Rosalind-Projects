# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:58:27 2023

@author: Danielle
"""
import math

a = int(input ("What is a?: "))
b = int(input ("what is b? :"))

csq = (a**2 + b**2)

c = math.sqrt(csq)

print ("\nThe square of the hypotenuse of a triangle with sides of length " + str(a) + " and " + str(b) + " is " + str(csq))

print ("\nThe hypotenuse is " + str(c))