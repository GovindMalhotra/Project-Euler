"""
Project Euler question 3
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""
"""
def infinite_number_gen(x):
    i=1
    while i <= x:
        yield i
        i=i+1
"""
def smallest_multiple(x,y):
    t=[]
    r=[]
    for i in range(1,y):
        t.append(i)
    for j in range(y+1,x):
        l=[]
        for k in list(t):
            b=j%k
            l.append(b)
        if min(l)==max(l) and min(l)==0:
            r.append(j)
    return min(r)
                

print smallest_multiple(100000000,10)




