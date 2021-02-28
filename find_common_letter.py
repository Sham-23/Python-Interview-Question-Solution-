# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:53:38 2021

@author: shambhunath gupta
"""

def common_letter():
    str1 = input("Enter first String : ")
    str2 = input("Enter first String : ")
    #to remove the duplicates,we use set
    s1= set(str1)
    s2= set(str2)
    #now for common letters in both string
    lst = s1 & s2
    print(lst)

#call function
common_letter()