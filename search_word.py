#*** Code For Searching about a word in the all file ***#

file_name = input("Enter the file name: ")
count = 0

try:
    handle = open(file_name)
except:
    print("file name error ")
    quit()

word = input('What is the word you looking for: ').strip()

for line in handle:
    line = line.rstrip()
    if word not in line:
        continue
    count += 1
    print(line)
print(f"total is : {count}")