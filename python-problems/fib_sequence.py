"""
In math, it's given in a recursive form:
     | 0           if n = 0;
Fn = | 1           if n = 1;
     | Fn-1 + Fn-2 if n > 1.

Wolfram:
      
       (1+sqrt(5))exp(n) - (1-sqrt(5))exp(n)
  Fn=  --------------------------------------
                2exp(n)sqrt(5)
"""

from math import sqrt

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(10)


def F(n):
    return ((1+ sqrt(5)))**n-((1-sqrt(5))**n)/(2**n*sqrt(5))

print F(10)
