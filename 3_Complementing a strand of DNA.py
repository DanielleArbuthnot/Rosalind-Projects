# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:37:32 2023

@author: Danielle
"""

#https://rosalind.info/problems/revc/
#Task - Output the reverse complement of a DNA sequence

DNA = input("What is the forward sequence?: ")

reverse = DNA[::-1]

print ("\n\nThe reversed sequence is: \n\n" + reverse)

#replace nt with complementary nt

complement = reverse.replace ("A", "a")
complement = complement.replace ("T", "t")
complement = complement.replace ("G", "g")
complement = complement.replace ("C", "c")

complement = complement.replace ("t", "A")
complement = complement.replace ("a", "T")
complement = complement.replace ("c", "G")
complement = complement.replace ("g", "C")

print ("\n\nThe reversed complement sequence is: \n\n" + complement)