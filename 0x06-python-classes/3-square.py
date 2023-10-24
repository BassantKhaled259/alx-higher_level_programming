#!/usr/bin/python3
"""Defines a class square"""

class square:
"""Class that defines square by: (based on 2-square.py).
   Attribute:
        size: size of a square (1 side).
"""

def __init__(self, size=0):
"""Creates new instances of square.

Args:
    size: size of the square (1 side)
"""

self.__size = size

if not isinstance(size, int):
    raise TypeError("size must be an integer")
if size < 0:
    raise ValueError("size must be >= 0")
else
    self.__size = size

def area(self):
"""A public object method.
Returns: the current square area"""

return self.__size**2
