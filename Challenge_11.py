import random
print("Welcome to 'whose wallet?' ")
print("You will give me a list of names, and I will pick a person to pay.")
names = input("If you're ready, enter names separated by a comma :  ").split(", ")
print(f"Please ask '{random.choice(names)}' to take his wallet out. Dinner is on him.'")