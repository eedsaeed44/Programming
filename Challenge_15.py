print("Welcone to place the rabbit ....\n")
list_1 = ['🌲', '🌲', '🌲', '🌲']
list_2 = ['🌲', '🌲', '🌲', '🌲']
list_3 = ['🌲', '🌲', '🌲', '🌲']
print(list_1)
print(list_1)
print(list_1)

print("\nWhere should the rabbit go? 🐇")
input_str = input("Please choose a row and a column: ")
number_one = input_str[0]
number_two = input_str[1]

if number_one == '1' :
    if number_two == '1':
        list_1[0] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '2':
        list_1[1] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '3':
        list_1[2] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '4':
        list_1[3] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    else:
        print("Invalid number!2")
elif number_one == '2' :
    if number_two == '1':
        list_2[0] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '2':
        list_2[1] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '3':
        list_2[2] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '4':
        list_2[3] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    else:
        print("Invalid number!2")
elif number_one == '3' :
    if number_two == '1':
        list_3[0] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '2':
        list_3[1] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '3':
        list_3[2] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    elif number_two == '4':
        list_3[3] = '🐇'
        print("\nSuccess .....\n")
        print(list_1)
        print(list_2)
        print(list_3)
        print("")
    else:
        print("Invalid number!2")
else:
    print("\nInvalid number!1\n")



