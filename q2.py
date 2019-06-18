# -*- coding: utf-8 -*-

#Write a function to find simple interest by taking inputs from user

def simple():
    time=float(input('Enter time in years'))
    rate=float(input('Enter rate'))
    prin=float(input('Enter principal amount'))
    si=(prin*rate*time)/100
    print('Simple Interest is',si)
    
simple()