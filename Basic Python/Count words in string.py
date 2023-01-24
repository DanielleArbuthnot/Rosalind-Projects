# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:02:38 2023

@author: Danielle
"""
import numpy


wordcount = {}

string = input("what is the string?: ")

punc = "£$%^&*()_+-={}[]:@~;'#|\<>?,./"
for char in string:
    if char in punc:
        string = string.replace(char, "")

stringsplit = string.split()

for word in stringsplit:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1

for key, value in wordcount.items():
    print (str(key) + "\t" + str(value))


#to put results in an array (requires numpy)
a = wordcount.items()   #returns all key value pairs in dictionary
b = list(a)             #turns all key value pairs into a list
c = numpy.array(b)      #turns the list into an array
print (c)