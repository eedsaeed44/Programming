import sys

file = input("Enter the file name : ")

try:
    handle = open(file)
except:
    print("File Name Error")
    quit()
count = 0

domans = []
for line in handle:
    line = line.split()
    if line[0] in domans:
        continue
    domans.append(line[0])
for n in domans:
    print(n)
    count += 1
    with open('output.txt', 'a') as f:
        sys.stdout = f
        print(n)
        sys.stdout = sys.__stdout__
        
print(f"Count Lines: {count}")




#==========================================================================================================


