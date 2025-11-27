from random import choice
import argparse as ap 

parser = ap.ArgumentParser()
tuple_type = lambda s: tuple(map(int, filter(lambda ch: ch not in '(, )', s)))
parser.add_argument('--word_len', type=tuple_type, default=(3,7), help='Word length (min, max). Ex. (4,8), (4,4). Default = (3,7)')
parser.add_argument('--num_words', type=int, default=1, help='Number of words in a line. Default = 1')
parser.add_argument('--num_tries', type=int, default=15, help='Number of lines to generate. Default = 15')
args = parser.parse_args()

word_len_min, word_len_max = args.word_len
word_lens  = list(range(word_len_min, word_len_max+1))
num_words, num_tries = args.num_words, args.num_tries 

letters = {chr(i) for i in range(97, 97+25+1)}
vows = {'a', 'e', 'i', 'o', 'u'}
cons = letters - vows
cons, vows = list(cons), list(vows)

for i in range(num_tries):
    words = ['' for _ in range(num_words)]
    for i, word in enumerate(words):
        word_len = choice(word_lens)
        for _ in range(word_len // 2):
            if (choice([0,1])): word += choice(cons) + choice(vows)
            else:              word += choice(vows) + choice(cons)
        if (word_len % 2):
            if (choice([0,1])): word += choice(cons)
            else:              word += choice(vows)
        words[i] = word
    for word in words: print(word, end=' ')
    print()