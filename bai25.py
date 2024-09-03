# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:47:39 2024

@author: Asus
"""

chucai = input("Nhap vao mot chu cai: ") 

if chucai.islower():
    chucai = chucai.upper()
else:
    chucai = chucai.lower()

print("Chu cai sau khi chuyen doi: ", chucai)