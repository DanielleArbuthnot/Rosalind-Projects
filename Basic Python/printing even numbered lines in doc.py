# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:58:52 2023

@author: Danielle
"""

#https://rosalind.info/problems/ini5/

docname = input("what is the document name? ")
file = docname + ".txt"

newfile = docname + "_new.txt"

doc = open(file, 'r')
doc2 = open (newfile, 'w')  

for lines in doc:
    line = doc.readline()
    print (line)
    doc2.write(line)
