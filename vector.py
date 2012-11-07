#/usr/bin/env python
#coding=utf8

import math as _math


class Vector():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        self.x += other.x
        self.x += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.x -= other.y
        return self

    def __mul__(self, other):
        self.x *= other
        self.x *= other
        return self

    def __div__(self, other):
        self.x /= other
        self.x /= other
        return self

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        return self

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def distance(self, other):
        return _math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return _math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalized(self):
        try:
            return self / self.magnitude()
        except ZeroDivisionError:
            return self
