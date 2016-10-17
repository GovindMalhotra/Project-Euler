
"""
Project Euler question 3
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""
import time
l=[]
def div_check1(x):
    i=2
    while i <= x:
        if x%i ==0:
            l.append(i)
            x = x/i
            div_check1(x)
            break
        i=i+1
    return max(l)


start = time.time()
print div_check1(600851475143)
elapsed = (time.time() - start)
print elapsed


