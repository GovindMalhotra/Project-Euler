
from math import round
def number_generator(x):
    n=5
    while n < x:
        yield n
        n = n+2

           

def factors(x):
    l=[]
    for i in number_generator(round(x*0.5)):
        if x%i == 0 and i%3 != 0 and i%5 != 0:
            l.append(i)
    return l

print factors(600851475143)
