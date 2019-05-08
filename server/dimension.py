# coding=utf-8
class Dimension(dict):
    def __init__(self, lim_i, lim_s, k):
        self.lim_i = 0
        self.lim_s = lim_s
        self.k = k

    def __str__(self):
        return str(self.__dict__)