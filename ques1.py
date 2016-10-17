"""
Project Euler question 1
Author : Govind Malhotra
Date : 7th July 2016
Objective : Find sum of all natural numbers less than a certain number x
which are divisible are either 3 or 5
"""

def ques1(x):
    l=[]
    for i in range(1,x):
        if i%3==0 or i%5==0:
            l.append(i)
    return sum(l)

print ques1(10)
print ques1(1000)
        
