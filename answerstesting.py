import unittest

from answer import WordleAnswer


class MyTestCase(unittest.TestCase):

    def test_something(self):
        A = WordleAnswer()
        # (target, guess)
        self.assertEqual(A.response("light", "fired"), 'bgbbb')
        self.assertEqual(A.response("light", "speed"), 'bbbbb')
        self.assertEqual(A.response("fetch", "waste"), 'bbbyy')
        self.assertEqual(A.response("mumps", "mummy"), 'gggbb')
        self.assertEqual(A.response("speed", "evade"), 'ybbyy')
        self.assertEqual(A.response("cared", "evade"), 'ybyyb')

if __name__ == '__main__':
    unittest.main()
