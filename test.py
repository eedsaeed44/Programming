file_name = input("Enter File Name: ")
if len(file_name) < 1:
    print("enter right name")
hand = open(file_name)

for line in hand:
    line = line.replace('/', '$')
    line = line.rstrip()
    print(line)





