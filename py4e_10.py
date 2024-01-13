file = input("Enter the file name : ")

try:
    handle = open(file)
except:
    print("File Name Error")
    quit()

for line in handle:
    line = line.split()
    print(line)