# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:29:16 2024

@author: Asus
"""
#nhập giờ phút giây từng người dùng
hour = int(input("Nhập hour: "))
minute = int(input("Nhập minute: "))
second = int(input("Nhập second: "))
if hour < 24 and hour >=0 and minute < 60 and minute >=0 and second < 60 and second >=0:
        print("hour,minute,second hợp lệ")
else:
        print("hour, minute, second hợp lệ")

