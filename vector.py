#/usr/bin/env python
#coding=utf8

import math


class Vector():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __div__(self, other):
        return Vector(self.x / other, self.y / other)

    def __idiv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __getitem__(self, other):
        return other

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def magnitude(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def normalize(self):
        try:
            self.x /= self.length()
            self.y /= self.length()
        except ZeroDivisionError:
            self.x = 0
            self.y = 0

    def normalized(self):
        try:
            return self / self.length()
        except ZeroDivisionError:
            return Vector(0, 0)

    def distance(self, other):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
