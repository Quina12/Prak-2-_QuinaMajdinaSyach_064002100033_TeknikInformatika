# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:21:46 2021

@author: Quina
"""
from math import sqrt

fo=input('Panjang sisi mana yang kamu cari di antara sisi a, b, atau c? ')

if fo=="c":
    sa=int(input("Masukkan panjang sisi a : "))
    sb=int(input("Masukkan panjang sisi b : "))
    sc=sqrt(sa*sa + sb*sb)
    
    print("Panjang dari sisi c adalah ",sc)

elif fo=="a":
    sb=int(input("Masukkan panjang sisi b : "))
    sc=int(input("Masukkan panjang sisi c : "))
    
    if (sc<sb):
        print("Panjang sisi c tidak valid")
        sc=int(input("Masukkan panjang sisi c : "))
        
    sa=sqrt(sc*sc-sb*sb)
    print("Panjang dari sisi a adalah ",sa)

elif fo=="b":
    sa=int(input("Masukkan panjang sisi a : "))
    sc=int(input("Masukkan panjang sisi c : "))
    if (sc<sa):
        print("Panjang sisi c tidak valid")
        sc=int(input("Masukkan panjang sisi c : "))
        
    sb=sqrt(sc*sc-sa*sa)
    print("Panjang dari sisi b adalah ",sb)    
else:
    print("Tolong pilih di antara sisi a,b,c")
    