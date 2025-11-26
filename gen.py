from random import choice

word_len_min, word_len_max = 3, 7
word_lens  = list(range(word_len_min, word_len_max+1))
num_words, num_tries = 2, 25

letters = {chr(i) for i in range(97, 97+25+1)}
vows = {'a', 'e', 'i', 'j', 'o', 'u'}
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