from collections import Counter
from answer import WordleAnswer
from math import log

class Best:

    @staticmethod
    def expectedguessesremaining(word, universe):
        A = WordleAnswer()
        dist = dict()
        for u in universe:
            resp = A.response(u, word)
            if resp in dist:
                dist[resp] += 1
            else:
                dist[resp] = 1
        unisize = len(universe)
        expectedguesses = 0
        # s = len(universe)*len(universe)
        for k, v in dist.items():
            if k != 'ggggg':
                expectedguesses += (log(v, 5.28453709477981) + 1) * (v/unisize)
        return expectedguesses

    @staticmethod
    def topnguesses(possible, guesses, n, worst=False):
        scores = dict()
        for g in guesses:
            scores[g] = Best.expectedguessesremaining(g, possible)
        return dict(sorted(scores.items(), key=lambda x:x[1], reverse=worst)[:n])