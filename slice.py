import sys

file = input("Enter file name : ")

try:
    handle = open(file)
except:
    print("name error ")
    quit()
subdomans = []
uniqe = []
for line in handle:
    line = line.split(' ')
    subdomans.append(line[0])

    subdomans.append(line[-2])

    # with open('on.txt', 'a') as f:
    #     sys.stdout = f
    #     print(line)
    #     sys.stdout = sys.__stdout__
for w in subdomans:
    if w in uniqe:
        continue
    else:
        uniqe.append(w)
print()

for m in uniqe:
    print(m)