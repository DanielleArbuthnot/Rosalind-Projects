# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:00:28 2023

@author: Danielle
"""

#https://rosalind.info/problems/gc/
#Task - testing GC content of ANY NUMBER of DNA strings in FASTA format and
#outputting which has the highest GC content.

#Stage 1
#1. collect data for first sequence
#2. calculate GC content and print to screen

#Stage 2
# in a loop:
#1. ask if there is another sequence to analyse
#       if yes - 
#           input data and output GC content
#           compare new sequence to old
#           store data of highest sequence
#       if no - 
#           print GC content of highest sequence

seq_name = input("What is the name of the first sequence?: ")
seq = input("What is the sequence of "+ seq_name + "?: ")

seq = seq.replace("\n", "")

seq_len = len(seq)

seq_GC_count = (seq.count('C') + seq.count('G'))


seq_GC = ((seq_GC_count / seq_len) * 100)
print ("seq_GC is: " + str(seq_GC))

highest_GC = seq_GC
highest_GC_name = seq_name

while input("Do you want to add another sequence? y/n : ") == 'y':
#   data collection for next sequence
    seq_name = input("What is the name of the next sequence?: ")
    seq = input("What is the sequence of "+ seq_name + "?: ")

    seq = seq.replace("\n", "")

    seq_len = len(seq)

    seq_GC_count = (seq.count('C') + seq.count('G'))


    seq_GC = ((seq_GC_count / seq_len) * 100)
    print ("The GC percentage is: " + str(seq_GC))
    
#   compare new sequence to old and store the highest
    if seq_GC > highest_GC:
        highest_GC = seq_GC
        highest_name = seq_name
    else:
        continue

print ("/n/nThe sequence with the highest GC is: \n" + highest_name + "\n" + str(highest_GC))

