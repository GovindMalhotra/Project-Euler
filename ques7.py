
#Question - 7

from math import ceil

def prime_number_identifier(i):
    l=[2,3]
    for t in range(5,i,2):
        d=[]
        r = ceil(0.5*t)
        s=int(r)
        for j in range(2,s):
            k=t%j
            d.append(k)
        if min(d) != 0:
            l.append(t)
    return l

print prime_number_identifier(120000)[10000]
    
    
