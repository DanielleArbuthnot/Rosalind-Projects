# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:29:41 2023

@author: Danielle
"""

#https://rosalind.info/problems/dna/

nt = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

string = str(input("what is the string?: "))

for letter in string:
    nt[letter] += 1

a = nt['A']
c = nt['C']
t = nt['T']
g = nt['G']

print (str(a) + " " + str(c) + " " + str(g) + " " + str(t))