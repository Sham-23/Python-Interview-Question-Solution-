# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:14:21 2021

@author: shambhunath gupta
"""
n=int(input("Enter a number for print swastik pattern"))
def Swastik_pattern(n):
    row=n;
    col=n;
    for i in range(row): #i  in range of o to n
        for j in range(col): #j  in range of o to n
            #for first left section of swastik
            if (i<row//2):    #i for row
                if (j<col//2):
                    if(j==0):   #for first col print * for row and col less than 3
                        print("*",end="")
                    else:
                        print(" ",end="")
                elif(j==col//2): #for middle col eg n-7 then it's fot j=3
                    print("*",end="")
                else:
                    if(i==0): #for row 0 and col > 3
                        print("*",end="")
                    else:
                        print(" ",end="")
            #middle row of given number by user
            elif(i==row//2):
                print("*",end="")
            else:
                #for last row
                if (i==row-1):
                    if(j<=col//2 or j==col-1):
                        print("*",end="")
                    else:
                        print(" ",end="")
                elif(j==col//2 or j==col-1):
                    print("*",end="")

                else:
                    print(" ",end="")

        print()



Swastik_pattern(n)