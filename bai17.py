# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:40:55 2024

@author: Asus
"""
# Nhập ba số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

# Tìm số lớn nhất và số nhỏ nhất
max_so = max(a, b, c)
min_so = min(a, b, c)

print("là số lớn nhất: ",max_so)
print("là số nhỏ nhất: ",min_so)