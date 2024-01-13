colors = []
color_1 = input("Add the first color you like: ")
colors.append(color_1)
more = input("Do you want to add more colors? Yes or No? ").lower()
if more == "yes":
    color_2 = input("Add another color to the list: ")
    colors.append(color_2)
    print("The colors you like are: ")
    print(colors)


elif more == "no":
    print("The color you like is:")
    print(colors)

else:
    print("enter yes or no only")

