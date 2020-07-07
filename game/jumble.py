#!/usr/bin/env python

__author__ = "mis_takes"
__license__ = "GPL-3"
__version__ = "1.0.1"
__maintainer__ = "mis_takes"
__email__ = "hidden_perspectives@protonmail.com"

"""
  simple script to find the correct word from jumbled order,
  just give the jumbled string it will show all the possible word list
  using itertools (inbuilt) & enchant(to find the dictonary words)
"""


import enchant
from itertools import permutations
s = input ("Enter the string :")
perms = [''.join(p) for p in permutations(s)]
print(len(perms))
perms = list(set(perms)) 
print(len(perms))
d = enchant.Dict("en_US")
for i in perms:
    if(d.check(i)):
        print(i)
