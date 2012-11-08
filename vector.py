#/usr/bin/env python
#coding=utf8

import math as _math


class Vector():
    '''A simple 2D vector class.'''

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        # Return the sum of two vectors.
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        # Return the result of the subtraction of two vectors.
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, factor):
        # Return the vector scaled with the factor.
        self.x *= factor
        self.y *= factor
        return self

    def __div__(self, divisor):
        # Return the vector scaled with the divisor.
        self.x /= divisor
        self.y /= divisor
        return self

    def __neg__(self):
        # Return the inverse of the vector.
        self.x = -self.x
        self.y = -self.y
        return self

    def __eq__(self, other):
        # Return True if the two vectors are equal, otherwise return False.
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        # Return True if the two vectors are inequal, otherwise return False.
        return self.x != other.x or self.y != other.y

    def __repr__(self):
        # Return a string representation of the vector for debugging.'''
        return 'Vector(%s, %s)' % (self.x, self.y)

    def normalized(self):
        '''Return the vector normalized.'''
        try:
            return self / self.magnitude()
        except ZeroDivisionError:
            return self

    def rounded(self):
        '''Return the vector with rounded widths and heights.'''
        self.x = round(self.x)
        self.y = round(self.y)
        return self

    def direction(self):
        '''Return the direction of the vector (in radians).'''
        return _math.atan(self.y / self.x)

    def magnitude(self):
        '''Return the magnitude of the vector.'''
        return _math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def distance(self, other):
        '''Return the distance between the terminal points of two vectors.'''
        return _math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def dot(self, other):
        '''Return the dot product of two vectors.'''
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        '''Return the cross product of two vectors.'''
        return self.x * other.y - self.y * other.x
