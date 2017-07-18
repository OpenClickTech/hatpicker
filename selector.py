from random import SystemRandom
import argparse
import sys

parser = argparse.ArgumentParser(description='Draw N ids at random from an input file.')
parser.add_argument('-n', type=int, help='the number of ids to draw', required=True)
args = parser.parse_args()

ids = set()

# Collect all the ids, from standard input, ignoring duplicates that appear more
# than once in the input file.
for line in sys.stdin:
    ids.add(line.strip())

print('Drawing {} ids from a set of {}'.format(args.n, len(ids)))

# Initialize random number generator
rng = SystemRandom()

# Choose n values at random from the list
chosen = rng.sample(ids, args.n)

# Print the choices out in order
for idx, c in enumerate(chosen):
    print('Pick {}: {}'.format(idx+1, c))

