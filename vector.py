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
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Return the result of the subtraction of two vectors.
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        # Return the vector scaled with the factor.
        return Vector(self.x * factor, self.y * factor)

    def __div__(self, divisor):
        # Return the vector scaled with the divisor.
        return Vector(self.x / divisor, self.y / divisor)

    def __neg__(self):
        # Return the inverse of the vector.
        return Vector(-self.x, -self.y)

    def __eq__(self, other):
        # Return True if the two vectors are equal, otherwise return False.
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        # Return True if the two vectors are inequal, otherwise return False.
        return self.x != other.x or self.y != other.y

    def __repr__(self):
        # Return a string representation of the vector for debugging.
        return 'Vector(%s, %s)' % (self.x, self.y)

    def normalized(self):
        '''Return the vector normalized.'''
        try:
            return Vector(self.x, self.y) / self.magnitude()
        except ZeroDivisionError:
            return Vector(self.x, self.y)

    def rounded(self):
        '''Return the vector with rounded widths and heights.'''
        return Vector(round(self.x), round(self.y))

    def direction(self):
        '''Return the direction of the vector in radians.'''
        try:
            return _math.atan(self.y / self.x)
        except ZeroDivisionError:
            if self.y != 0:
                return _math.radians(90 if self.y > 0 else -90)
            else:
                # The null vector has arbitrary direction.
                return None

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
