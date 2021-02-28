# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:12:01 2021

@author: shambhunath gupta
"""

def len_last_word():
    str=input("Enter the string : ")
    #first spilit the string ,seprate them ' ' and then store into arr
    arr=str.split(' ')
    print(arr)

    #for find the length of last element
    last_word=arr[-1]
    print(len(last_word))

len_last_word()

