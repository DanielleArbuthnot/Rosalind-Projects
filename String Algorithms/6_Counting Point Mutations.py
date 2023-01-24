# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:55:38 2023

@author: Danielle
"""

#https://rosalind.info/problems/hamm/
#Task - Calculate the Hamming distance between 2 strings
#(Hamming distance - number of differing nucleotides)


#1. input both sequences
#2. use for loop to compare each index of the sequences
#3. if indexes do not match, add 1 to the counter

seq1 = input("What is the first string?: ")
seq2 = input("what is the second string?: ")

count = 0

for nt in range(len(seq1)):
    if seq1[nt] != seq2[nt]:
        count += 1
       

print ("Hamming distance is: \n " + str(count))