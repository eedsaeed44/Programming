attendes = ['Alice', 'Bob', 'Charlie']
for i in attendes:
    print(i)
    confirm = input("Is this person attending? (yes/no): ").lower()
    if confirm == 'yes':
        print("Attendance Confirmed!")
    else:
        print("Attendance Not Confirmed!")
    print("------------------------------------")