file_name = input("Enter File Name: ")
if len(file_name) < 1:
    print("enter right name")
hand = open(file_name)
count = 0
for line in hand:
    line = line.replace('*.', '')
    line = line.rstrip()
    count = count + 1
    print(f"{count} => {line}")

print(f"The Total numbers of lines are : {count}\n")
