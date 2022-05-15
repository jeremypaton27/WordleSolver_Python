from answer import WordleAnswer


class SetReducer:

    @staticmethod
    def setfilter(universe, guess, pattern):
        A = WordleAnswer()
        resp = set()

        for u in universe:
            if A.response(u, guess) == pattern:
                resp.add(u)

        return resp