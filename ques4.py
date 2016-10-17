"""
Project Euler question 3
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""
l={}
for i in range(90,100):
    for j in range(98,100):
        k=i*j
        l=str(k)
        m=len(l)
        n=int(m*0.5)
        if m==4 and (l[0:n]==l[::-1][0:n]):
            print i,j,k
