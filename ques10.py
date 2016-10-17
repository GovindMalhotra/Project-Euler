
#Question - 10

from math import ceil

def prime_number_sum(i):
    c=5
    for t in range(5,i,2):
        d=[]
        r = ceil(0.5*t)
        s=int(r)
        for j in range(2,s):
            k=t%j
            d.append(k)
        if min(d) != 0:
            c = c + t
    return c

print prime_number_sum(10)
    
    
