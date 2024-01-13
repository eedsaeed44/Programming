import random
list = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(list)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("\nWelcome to the Rock, Paper, Seissors game:")
press = input("Press Enter to continue or type (Help) for rules help..").lower()
if press == 'help':
    print(""""\n
                         ***************RULES**********
                        1) You choose and the computer chooses
                        2) Rock smashes Scissors -> Rock wins
                        3) Scissors cut Paper -> Scissors wins
                        4) Paper covers Rock -> Paper wins\n
           """)

choice = input("Enter your choice (rock, paper, scissors): ").capitalize()
if choice not in ['Rock', 'Paper', 'Scissors']:
    print("Invalid choice chose (rock, paper, scissors) only. Try again..\n")
else:
    if choice == 'Rock':
        print(f"\nYour choice:\n{rock}\n")
    elif choice == 'Paper':
        print(f"\nYour choice:\n{paper}\n")
    else:     
        print(f"\nYour choice:\n{scissor}\n")
    if computer_choice == "Rock":
        print(f"\nComputer choice:\n{rock}")
    elif computer_choice == "Paper":
        print(f"\nComputer choice:\n{paper}")
    else:
        print(f"\nComputer choice:\n{scissor}")
    if choice == computer_choice:
        print("It is a tie!")
    elif(
        (choice == "Rock" and computer_choice == "Scissors")
        or
        (choice == "Paper" and computer_choice == "Rock")
        or
        (choice == "Scissors" and computer_choice == "Paper")
):
        print(f"You wine! {choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {choice}.")
