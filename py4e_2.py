# code for return only string lines

file_name = input("Enter File Name ")
count = 0
b = 0
# Handle the error of file name
try:
    file_handle = open(file_name)
except:
    print(f"File cannot be opened: {file_name}")
    quit()
for line in file_handle:
    line = line.rstrip()
    b += 1
    if line.isnumeric():
        continue
    
    print(line)
    count += 1

print(f"Total Lines Before: {b}")
print(f"Total Lines After: {count}")