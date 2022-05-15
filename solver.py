from setreduction import SetReducer
from collections import Counter
from bestguess import Best
from distribution import Distribution


def main():
    with open('acceptedwords.txt') as f:
        universe = set(f.read().splitlines())

    with open('acceptedwords.txt') as f:
        complete = set(f.read().splitlines())

    print(f'Loaded in {len(universe)} words')
    print('Use the following commands:')
    print("\tEnter a five letter string that you have guessed..")
    print("\tEnter 'd' to see a distribution of a possible guess.")
    print("\tEnter 'q' to quit.")
    print("\tEnter 's' to see all possible words remaining.")
    print("\tEnter 'r' to reset to the initial wordlist.")
    print("\tEnter 'g' to see the best guesses.")
    print("\tEnter 'w' to see the worst guesses.")
    S = SetReducer()

    while True:
        print(f'{len(universe)} words remain.')
        g = input('Enter a Five Letter Guess or a Command:').lower()
        if g == 's':
            seeset(universe)
            continue
        if g == 'r':
            with open('acceptedwords.txt') as f:
                universe = set(f.read().splitlines())
            print(f'Loaded in {len(universe)} words')
            continue
        if g == 'q':
            print('Quitting...')
            break
        if g == 'g':
            bestguesses(universe, complete, worst=False)
            continue
        if g == 'w':
            bestguesses(universe, complete, worst=True)
            continue
        if g == 'd':
            distribution(universe)
            continue
        if len(g) != 5:
            print('Did not Enter a 5 Letter Word or Command Character.')
            continue
        p = input("What was the result of this guess?").lower()
        c = Counter(p)
        if len(p) != 5 and ((c['g'] + c['y'] + c['b']) != 5):
            print("Must guess a string of five 'g', 'y', 'b'.")
        universe = S.setfilter(universe, g, p)


def seeset(universe):
    print(sorted(universe))


def bestguesses(universe, complete, worst=False):
    inp = input('How many guesses do you want to see?').lower()
    B = Best()
    d = {}
    if inp.isnumeric():
        num=int(inp)
    else:
        print('Did not enter a number. Showing top 10.')
        num = 10
    print(f'Calculating {"worst" if worst else "top"} {num} guesses...')
    d = B.topnguesses(universe, complete, num, worst=worst)
    print("Guess | Expected Guesses Remaining after Guess")
    print("----------------------------------------------")
    for it in d.items():
        print(f'{it[0]} | {it[1]}')


def distribution(universe):
    inp = input("Distribution of what word?").lower()
    if len(inp) != 5:
        print('Did not enter a five letter word.')
        return
    B = Best()
    expguess = B.expectedguessesremaining(inp, universe)
    print(f'On average, you will have {expguess} guesses remaining after guessing {inp}.')
    D = Distribution()
    dist = D.buckets(inp, universe)
    dist = dict(sorted(dist.items(), key=lambda x: len(x[1]), reverse=True))
    for key, value in dist.items():
        if len(value) > 10:
            print(f'{patterntoemoji(key)} ({len(value)}):{value[0:10]} ...')
        else:
            print(f'{patterntoemoji(key)} ({len(value)}):{value}')


def patterntoemoji(pattern):
    e = ''
    for c in pattern:
        if c == 'g':
            e += '\U0001f7e9'
        if c == 'y':
            e += '\U0001f7e8'
        if c == 'b':
            e += '\U00002b1b'
    return e


if __name__ == "__main__":
    print('1')
    main()
