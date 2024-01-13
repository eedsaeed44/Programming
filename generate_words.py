from string import ascii_letters, digits, punctuation
from itertools import product
import sys
count_lines = 0
for passcode in product(ascii_letters , repeat=4):
    print("".join(passcode))
    count_lines += 1
    with open('all_words.txt', 'a') as f:
        sys.stdout = f
        print("".join(passcode))
        sys.stdout = sys.__stdout__


print(f"Count Of Lines Is: {count_lines}")

# if repeat=1 : 52
# if repeat=2 : 2700
# if repeat=3 : 140654
# if repeat=4 :
# if repeat=5 :
