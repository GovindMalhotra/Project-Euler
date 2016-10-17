"""
Project Euler question 3
Author : Govind Malhotra
Date : 8th July 2016
Objective : Largest prime factor of a number
"""

#First drive the prime numbers function

def number_generator(x):
    n=5
    while n < x:
        yield n
        n = n+2
        
        
def prime_func(x):
    l=[2,3]
    for i in number_generator(x):
        p=[]
        for j in xrange(3,i,2):
            t= i%j
            p.append(t)
        if min(p)!=0:
            l.append(i)
    return l

print prime_func(7000)


"""
def find_prime_factors(x):
    l = prime_func(x)
    t=[]
    for i in list(l):
        if x%i == 0:
            t.append(i)
    return max(t)

#print find_prime_factors(600851475143)
print find_prime_factors(60085147)
    """
                
