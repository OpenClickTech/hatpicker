# hatpicker

## Description & Usage

Picks n random ids out of a hat.

Usage:

```bash
$ python selector.py -n 3 < data/sampleids.txt
```

This will choose 3 MD5s at random from the sample data file included in this repo.

If you want to allow duplicate ids, given each id that is duplicated a greater chance of winning, use the `-d` flag:

```bash
$ python selector.py -n 3 -d < data/sampledupes.txt
```

This will chose 3 MD5s at random from the sample data that includes one of the 10 ids duplicated 11 times (i.e. one entrant gets 11 entries, and the remaining nine entrants each get 1 entry).

## Notes

This script uses the python `random.SystemRandom` class, which should use /dev/urandom on Linux. This makes the random selection process as cryptographically secure as possible without getting a hardware random number generator.

## Real-world MCR usage

To use this to draw MCR winners, you can follow these steps:

1. Generate a list of MD5s (or other unique identifier) of people who have entered the drawing. Save this in text format, with one MD5 per line. Do not include a newline at the end of the file.
1. Run the script as above, making sure to pass `-n` for the number of entries you'd like to draw, and `-d` if you want to allow multiple entries per user.
1. The script will output `n` MD5s for you, who are your potential winners. Starting with the first user, begin the eligibility verification process.
1. Award the prize to the first user who is verified to be eligible to win.
