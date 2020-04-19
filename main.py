# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:55:19 2020

@author: Ayaz
"""


print("--------------------------")

print("\nPAN CARD OCR\n")

print("--------------------------")

print("PRESS 1 TO CLICK AN IMAGE FROM WEBCAM")
print("PRESS 2 TO EXTRACT INFO FROM SAVED IMAGE")

print("\nEnter your choice: ")

inp = int(input())

if inp == 2:
    import ocr_local
if inp == 1:
    import capture