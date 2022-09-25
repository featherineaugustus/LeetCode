# -*- coding: utf-8 -*-
"""
Check if a string is a palindrome
"""

import time

def isPalindrome(x):
    return str(x)==str(x)[::-1]

print('\nUsing str')
start = time.time()
for i in range(-1000,1000):
    isPalindrome(i)
print(time.time() - start)



def isPalindrome(x):
    
    if x < 0:
        return False
    
    l = []
    while x > 0:
        l.append(x % 10)
        x = x // 10

    return l == l[::-1]

print('\nWithout string str')
start = time.time()
for i in range(-1000,1000):
    isPalindrome(i)
print(time.time() - start)