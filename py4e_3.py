# code for count the number of words in the file 

file_name = input("Enter File Name ")
count = 0
# Handle the error of file name
try:
    file_handle = open(file_name)
except:
    print(f"File cannot be opened: {file_name}")
    quit()

for line in file_handle:
    line = line.rstrip()
    line = line.split(" ")
    for n in line:
        count  += 1
    
print(f"the total words is: {count} ")
