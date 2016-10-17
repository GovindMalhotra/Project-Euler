"""
Project Euler question 2
Author : Govind Malhotra
Date : 7th July 2016
Objective : Find sum of even valued terms in fibonacci series
less than the number x
"""


#Defining function for fibonacci series
def fibo_series(x):
    if x == 1:
        y = 1
    elif x == 2:
        y = 2
    else:
        y = (fibo_series(x-1) + fibo_series(x-2))
    return y
print fibo_series(10)


def iter(x):
    for i in range(1,x):
        y=fibo_series(i)
        if y > 4000000:
            return i

print iter(100)

def fibo_print(x):
    l=[]
    for i in range(1,x):
        y=fibo_series(i)
        if y%2 == 0:
            l.append(y)
    return sum(l),max(l)


print fibo_print(iter(100))

