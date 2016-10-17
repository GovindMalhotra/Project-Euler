
"""
Project Euler question 3
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""

from operator import mul
import math

def prime(x):
    l=[2]
    for i in range(3,x):
        t=[]
        for j in range(2,i):
            b=i%j
            t.append(b)
        if min(t)!=0:
            l.append(i)
    return l


d=[]
def div_check1(x):
    i=2
    while i <= x:
        if x%i ==0:
            d.append(i)
            x = x/i
            div_check1(x)
            break
        i=i+1
    return d


dict={}
t=[]
def printxy(y):
    for i in range(2,y):
        m = div_check1(i)
        if min(m)==max(m) and len(m)>1:
            p={min(m):len(m)}
            dict.update(p)
        d[:]=[]
    for i in dict:
        x=i
        n=dict[i]
        p=math.pow(x,n)
        t.append(p)
    return dict,t

def multip(y):
    o=prime(y)
    p,q=printxy(y)
    r=dict.keys()
    s=[x for x in o if x not in r]
    print o,p,r,s
    v=reduce(mul,s)
    u=reduce(mul,q)
    g=int(u*v)
    print u,v,g
    return g


    
    
#print multip(10)
print multip(20)

    


"""

for i in dict:
    x=i
    n=dict[i]
    p=math.pow(x,n)
    l.append(p)    
print reduce(mul,l)*prime(20)
"""




    
