# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:01:04 2020

@author: Ayaz
"""

import csv
file = open('temp.txt', 'r')
lines  =file.readlines()

for i in range(4):
    string = lines[i]
    string = string[:-1]
    lines[i] = string

with open(r'pandata.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(lines)
    
    
print("--------------------------\n\n")
print("WRITTEN TO CSV FILE")
print("--------------------------\n\n")