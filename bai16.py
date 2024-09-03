# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:55:58 2024

@author: Asus
"""

# Nhập chuỗi giờ/phút/giây 
thoi_gian = input("Nhập hour/minute/second: ")
tongsogiay = 0
# Tìm số giờ 
if 'hour' in thoi_gian:
    hour = int(thoi_gian.split('hour')[0])
    tongsogiay += hour * 3600
# Tìm số phút 
if 'minute' in thoi_gian:
    minute= int(thoi_gian.split('minute')[0].split('hour')[-1])
    tongsogiay += minute * 60
# Tìm số giây 
if 'second' in thoi_gian:
    second = int(thoi_gian.split('hour')[0].split('minute')[-1])
    tongsogiay += second 
print("số giây là: ", tongsogiay) 