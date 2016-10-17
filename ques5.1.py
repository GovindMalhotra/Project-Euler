
"""
Project Euler question 5
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""
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
"""

def factorial(x):
    if x==0:
        y=1
    elif x==1:
        y=1
    else :
        y=x*factorial(x-1)
    return y

l=[]
def div_check1(y):
    i=2
    while i <= y:
        if y%i ==0:
            l.append(i)
            y = y/i
            div_check1(y)
            break
        i=i+1
    return l

print factorial(10), div_check1(factorial(10))


