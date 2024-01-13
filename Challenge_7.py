import random
user_input = input("Enter a 4-digit PIN code: ")
PIN_code = random.randint(1000,9999)
if  len(user_input) == 4:
    if user_input.isdigit():
        if user_input == PIN_code:
            print("Great! the PIN did match!!")
        else:
            print("Failure PIN code did not match.")
            print(f"The Computer generated this PIN: {PIN_code}")
    else:
        print("Enter only digits not string")     
else:
    print("Please Enter 4 digits only ")
