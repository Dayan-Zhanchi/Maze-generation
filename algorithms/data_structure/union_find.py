"""
    Implemented as described by Antii Laaksonen in Competitive programmer's handbook 2018
    can be found on page 146
"""


class union_find:

    def __init__(self, n):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        while x != self.link[x]:
            x = self.link[x]
        return x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = self.__swap(a, b)
        self.size[a] += self.size[b]
        self.link[b] = a

    @staticmethod
    def __swap(a, b):
        c = a
        a = b
        b = c
        return a, b
