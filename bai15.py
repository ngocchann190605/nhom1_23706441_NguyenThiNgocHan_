# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:14:13 2024

@author: Asus
"""
import math
#nhap hai so a,b 
a = float(input("nhap vao gia tri a: "))
b = float(input("nhap vao gia tri b: "))
ab = a*b

#tinh tung gia tri 
can3a = math.pow(a,1/3)
can3b = math.pow(b,1/3)
can3ab = math.pow(ab,1/3)
m =(a + b) / can3a + can3b 

#tinh tung thanh phan 
A = m - can3ab 
B = (can3a - can3b)**2

#ket qua
dapan = A / B
print("dap an la: ", dapan)
dapan = round(dapan, 3)
print("Số sau khi làm tròn 3 chữ số: ", dapan)
