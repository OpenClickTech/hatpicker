from random import SystemRandom
import argparse
import sys

parser = argparse.ArgumentParser(description='Draw N ids at random from an input file.')
parser.add_argument('-n', type=int, help='the number of ids to draw', required=True)
args = parser.parse_args()

rng = SystemRandom()
ids = set()

for line in sys.stdin:
    ids.add(line.strip())

chosen = rng.sample(ids, args.n)

print('Drawing {} ids from a set of {}'.format(args.n, len(ids)))

for c in chosen:
    print('got {}'.format(c))

