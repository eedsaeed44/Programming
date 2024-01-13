from string import ascii_letters, digits, punctuation
from itertools import product
import sys
count_lines = 0
for passcode in product(ascii_letters + digits + punctuation, repeat=4):
    # print("".join(passcode))
    count_lines += 1
    with open('all_pass.txt', 'a') as f:
        sys.stdout = f
        print("".join(passcode))
        sys.stdout = sys.__stdout__



print(f"Count Of Lines Is: {count_lines}")

# if repeat=1 : 94
# if repeat=2 : 8836
# if repeat=3 : 830584
# if repeat=4 : 

