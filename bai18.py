# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:01:04 2024

@author: Asus
"""

# Nhập vào thời gian theo định dạng hh:mm:ss

time_input1 = input("Nhập vào giờ, phút và giây (định dạng hh:mm:ss): ")
time_input2 = input("Nhập vào giờ, phút và giây (định dạng hh:mm:ss): ")
hh1 , mm1 , ss1 = map(int , time_input1.split(":"))
hh2 , mm2 , ss2 = map(int , time_input2.split(":"))
# Kiểm tra xem giờ, phút, giây có hợp lệ không
if 0 <= hh1  <= 23 and 0 <= mm1  < 60 and 0 <= ss1  < 60 and 0 <= hh2  <= 23 and 0 <= mm2  < 60 and 0 <= ss2  < 60:
    #cong gio
    giocong = hh1 + hh2 
    putcong = mm1 + mm2
    giaycong = ss1 + ss2
    print(f"thời gian sau khi cộng là: {giocong}:{putcong}:{giaycong}")
    #tru gio
    giotru = hh1 - hh2 
    puttru = mm1 - mm2 
    giaytru = ss1 - ss2 
    print(f"thời gian sau khi trừ là: {giotru}:{puttru}:{giaytru}")
else:
    print(" giờ phút hoặc giây không hợp lệ.")