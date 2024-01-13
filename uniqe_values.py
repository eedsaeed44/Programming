#*** Code For just return uniqe values ***#
import sys
file_name = input("Enter the file name: ")
count = 0
uniqe_values = []

before = 0
after = 0

try:
    handle = open(file_name)
except:
    print("file name error ")
    quit()

for line in handle:
    line = line.rstrip()
    before += 1
    if line in uniqe_values:
        continue
    uniqe_values.append(line)
    after += 1 


for n in uniqe_values:
    print(n)
    with open('un.txt', 'a') as f:
        sys.stdout = f
        print(n)
        sys.stdout = sys.__stdout__
        

print(f"lines before: {before}")
print(f"lines aftere: {after}")

