# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:16:49 2023

@author: Danielle
"""
#https://rosalind.info/problems/iprb/
#Calculate the probablility of the dominant phenotype 
#being displayed when 2 organisms mate when:
#   HD = homozygous dominant
#   Het = heterozygous
#   HR = homozygous recessive

HD = int(input("How many organisms are homozygous dominant?: "))
Het = int(input("How many organisms are heterozygous?: "))
HR = int(input("How many organisms are homozygous recessive?: "))

total = HD + Het + HR

#probability of each pairing

if HD > 1:
    HD_HD = ((HD / total) * ((HD -1) / (total -1)))
else:
    HD_HD = 0

if HD >=1 and Het >=1:
    HD_Het = (((HD / total) * (Het / (total-1))) + ((HD / (total -1)) * (Het / total)))
else:
    HD_Het = 0

if HD >=1 and HR >=1:
    HD_HR = (((HD / total) * (HR / (total -1))) + ((HD / (total -1)) * (HR / total)))
else:
    HD_HR = 0

if Het >1:
    Het_Het = ((Het / total) * ((Het -1) / (total -1)))
else:
    Het_Het = 0

if Het>=1 and HR >=1:
    Het_HR = (((Het / total) * (HR / (total -1))) + ((Het / (total -1)) * (HR / total)))
else:
    Het_HR = 0


dom = (HD_HD + HD_Het + HD_HR + (Het_Het * 0.75) + (Het_HR * 0.5))

print ("The probability of the dominant phenotype being expressed is: \n" + str(dom))