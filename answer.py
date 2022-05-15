from collections import Counter

class WordleAnswer:

    @staticmethod
    def response(target, guess):
        assert len(target) == 5
        assert len(guess) == 5

        targetl = list(target)
        guessl = list(guess)

        responsel = [None] * 5
        tcounts = Counter(target)
        gcounts = {letter: 0 for letter in guess}

        for i in range(5):
            if guessl[i] == targetl[i]:
                responsel[i] = 'g'
                letter = guessl[i]
                gcounts[letter] += 1
            if guessl[i] not in targetl:
                responsel[i] = 'b'

        for i in range(5):
            if not responsel[i]:
                letter = guessl[i]
                assert letter in targetl
                if gcounts[letter] < tcounts[letter]:
                    responsel[i] = 'y'
                    gcounts[letter] += 1
                else:
                    responsel[i] = 'b'

        return ''.join(responsel)