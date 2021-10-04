# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:15:00 2021

@author: Quina
"""

A = int(input("Masukkan Bilangan Pertama : "))
B = int(input("Masukkan Bilangan Kedua : "))
C = int(input("Masukkan Bilangan Ketiga : "))

if (A > B) and (A > C):
    print("Bilangan terbesarnya adalah : ",A)
elif (B > A) and (B > C):
    print ("Bilangan terbesarnya adalah : ",B)
else:
    print("Bilangan terbesarnya adalah : ",C)
    