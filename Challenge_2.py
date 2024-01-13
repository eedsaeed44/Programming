#Take two int values from user and print greatest among them.

two_digets = input("Enter two digets: ")
diget_one = two_digets[0]
diget_two = two_digets[1]

if diget_one > diget_two :
    print(f"the great diget among them is {diget_one}")
elif diget_two > diget_one : 
    print(f"the great diget among them is {diget_two}")
else:
    print("the digets are equal")