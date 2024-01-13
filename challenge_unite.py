import random
import string

print("Welcome to the Password Generator!")

total_numbers = int(input("Enter the total number of characters in the password: "))
letters_number = int(input("Enter the number of letters in the password: "))
numbers_number = int(input("Enter the number of numbers in the password: "))
symbols_number = int(input("Enter the number of symbols in the password: "))
pass_list = []
if total_numbers != (letters_number + numbers_number + symbols_number):
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length.")

else:
    letters = random.choices(string.ascii_letters, k=letters_number)
    numbers = random.choices(string.digits, k=numbers_number)
    symbols = random.choices(string.punctuation, k=symbols_number)
    pass_list.extend(letters)
    pass_list.extend(numbers)
    pass_list.extend(symbols)
    random.shuffle(pass_list)
    pass_shuffel = ("".join(pass_list))
    print(f"Generated Password:    {pass_shuffel}")
