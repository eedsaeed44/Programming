# code for return only string lines
import re
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
    n = re.findall('[0-9]+' , line)
    print(n)