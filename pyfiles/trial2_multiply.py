# -*- coding: utf-8 -*-

class Multiply:
    def __init__(self, conf):
        self.a = conf["a"]
        self.b = conf["b"]

    def plus(self, a, b):
        return a + b

    def multiply(self, c, d):
        return c * d

    def plus_multiply(self, c, d):
        return self.plus(c,d) * self.multiply(c, d)

    def execute(self):
        return self.plus_multiply(self.a, self.b)

