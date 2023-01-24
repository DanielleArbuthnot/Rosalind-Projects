# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:52:48 2023

@author: Danielle
"""

#https://rosalind.info/problems/rna/
#Task - transcribe DNA into RNA

DNA = input("What is the string?: ")

RNA = DNA.replace("T", "U")

print ("\n\nThe transcribed RNA is: \n" + RNA)