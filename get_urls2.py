import sys

file = input("Enter file name : ")

try:
    handle = open(file)
except:
    print("name error ")
    quit()
before = 0
after = 0
for line in handle :
    line = line.rstrip()
    before += 1
    if 'https://' not in line:
        continue
    print(line)
    after += 1
    with open('on.txt', 'a') as f:
        sys.stdout = f
        print(line)
        sys.stdout = sys.__stdout__

print(f"before : {before}")
print(f"after : {after}")