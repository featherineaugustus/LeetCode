# -*- coding: utf-8 -*-
"""
A square root function that always round down.
"""

def Sqrt(x):
    lower = 0
    upper = x
    while int(lower) < int(upper):
        mid = (lower + upper)/2
        if mid*mid > x:
            upper = mid
        else:
            lower = mid
    print(int(lower))

Sqrt(0)
Sqrt(1)
Sqrt(2)
Sqrt(4)
Sqrt(8)
Sqrt(9)
Sqrt(400)