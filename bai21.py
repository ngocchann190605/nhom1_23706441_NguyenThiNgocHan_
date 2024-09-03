# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:46:13 2024

@author: Asus
"""
# Nhập số  từ người dùng
nun= int(input("Nhập vào một số nguyên: "))

# Kiểm tra và in kết quả
if 0 <= nun <= 9:
    number = ["không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
    print(number[nun])
else:
    print("Không đọc được")