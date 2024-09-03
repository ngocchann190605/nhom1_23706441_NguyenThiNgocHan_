# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:23:30 2024

@author: Asus
"""

import math

# Nhập loại hình
loại_hình = input("Nhập loại_hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if loại_hình == 'v':
    # Tính diện tích và chu vi của hình vuông
    cạnh = float(input("Nhập độ dài cạnh của hình vuông: "))
    chuvi = 4 * cạnh
    dientich = cạnh * cạnh
    print(f"P = {chuvi} S = {dientich}")

elif loại_hình == 'n':
    # Tính diện tích và chu vi của hình chữ nhật
    chieurong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    chieudai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chuvi = 2 * (chieurong + chieudai)
    dientich = chieurong * chieudai
    print(f"P = {chuvi} S = {dientich}")

elif loại_hình == 't':
    # Tính diện tích và chu vi của hình tròn
    bankinh = float(input("Nhập bán kính của hình tròn: "))
    chuvi = 2 * math.pi * bankinh
    dientich = math.pi * bankinh * bankinh
    print(f"P = {chuvi:.2f} S = {dientich:.2f}")

else:
    print("Loại_hình không hợp lệ. Vui lòng nhập v, n hoặc t.")
