import random

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def lrand(a, b):
    if 1 + a == b:
        return a
    else:
        return random.randrange(a, b)

def sample_with_replacement(n, m):
    indices = xrange(n)
    return [ random.choice(indices) for i in xrange(m) ]

def sample_with_replacement_from_list(lst, m):
    indices = xrange(len(lst))
    return [ lst[random.choice(indices)] for i in xrange(m) ]

def sample_without_replacement(n, m):
    return random.sample(range(n), m)

def sample_without_replacement_from_list(lst, m):
    return random.sample(lst, m)

def random_shuffle(lst):
    return random.sample(lst, k = len(lst))

