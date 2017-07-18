# hatpicker

## Description & Usage

Picks n random ids out of a hat.

Usage:

```bash
$ python selector.py -n 3 < data/sampleids.txt
```

This will choose 3 MD5s at random from the sample data file included in this repo.

## Notes

This script uses the python `random.SystemRandom` class, which should use /dev/urandom on Linux. This makes the random selection process as cryptographically secure as possible without getting a hardware random number generator.
