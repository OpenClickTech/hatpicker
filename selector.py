from random import SystemRandom
import argparse
import sys

parser = argparse.ArgumentParser(description='Draw N ids at random from an input file.')
parser.add_argument('-n', type=int, help='the number of ids to draw', required=True)
parser.add_argument('-d', action='store_const', help='allow duplicate ids, giving them a greater chance of winning', const=True, default=False)
args = parser.parse_args()

if args.d:
    ids = []
else:
    ids = set()

# Collect all the ids from standard input.
# if -d was not passed, ignore duplicates that appear more than once in the input file.
for line in sys.stdin:
    if args.d:
        ids.append(line.strip())
    else:
        ids.add(line.strip())

print('Drawing {} ids from a set of {}'.format(args.n, len(ids)))

# Initialize random number generator
rng = SystemRandom()
chosen = []

# Choose n values at random from the list
for _ in xrange(args.n):
    pick = rng.sample(ids,1)[0]
    chosen.append(pick)
    if args.d:
        ids = [val for val in ids if val != pick]
    else:
        ids.remove(pick)

# Print the choices out in order
for idx, c in enumerate(chosen):
    print('Pick {}: {}'.format(idx+1, c))

