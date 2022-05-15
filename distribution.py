from answer import WordleAnswer
from math import log2

class Distribution:

    @staticmethod
    def buckets(word, universe):
        A = WordleAnswer()
        d = dict()
        for u in universe:
            ans = A.response(u, word)
            if ans in d:
                d[ans].append(u)
            else:
                d[ans] = [u]
        for v in d.values():
            v.sort()
        return d

    @staticmethod
    def expectedlog(word, universe):
        A = WordleAnswer()
        bucks = Distribution.buckets(word, universe)
        s = 0
        for code, b in bucks.items():
            l = len(b)
            s += l * log2(l)
        return s / len(universe)
