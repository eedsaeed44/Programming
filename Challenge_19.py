indut = input("Enter the names of attendes seperated by commas: ").split(",")
list = []
list.extend(indut)
for i in list:
    print(f"\n{i}\n")
    confirm = input("Is this person attending? (yes/no): ").lower()
    if confirm == "yes":
        print("Attendance confirmed")
    else:
        print("Attendance not confirmed")
    print("----------------------------------------------")