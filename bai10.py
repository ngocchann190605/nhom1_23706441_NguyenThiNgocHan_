# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:25:27 2024

@author: Asus
"""
so = int(input("Nhập vào biển số xe gồm 4 số: "))
ngan = so // 1000
tram = so // 100 % 10
chuc = so // 10 % 10
donvi = so % 10
nut = tram + ngan + chuc + donvi
a = nut // 10
b = nut % 10
c = a + b
d = c // 10
e = c % 10
f = d + e
print("Biển số xe của bạn được: (nút)", f)