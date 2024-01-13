import random
print("welcome to the coin guessing game!")
print("choose a method to toss the coin:")
print("1. using random.random()\n2. using random.randint()")
user_choice = input("enter your choice (1 or 2): ")
computer_method_1 = random.random()
computer_method_2 = random.randint(0,1)
print(computer_method_1)
print(computer_method_2)

if user_choice == "1":
    user_guess = input("enter your guess (heads or tails): ").lower()
    if computer_method_1 >= 0.5 and user_guess == "heads":
        print("congratulation! you won!")
        print("the computer's coin toss result was: Heads")
    elif computer_method_1 < 0.5 and user_guess == "heads":
        print("sorry! you lose!")
        print("the computer's coin toss result was: Tails")
    elif computer_method_1 >= 0.5 and user_guess == "tails":
        print("sorry! you lose!")
        print("the computer's coin toss result was: Heads")
    elif computer_method_1 < 0.5 and user_guess == "tails":
        print("congratulation! you won!")
        print("the computer's coin toss result was: Tails")
    else:
        print("invalid choice. please select either Heads or Tails only")
elif user_choice == "2":
    user_guess = input("enter your guess (heads or tails): ").lower()
    if computer_method_2 == 1 and user_guess == "heads":
        print("congratulation! you won!")
        print("the computer's coin toss result was: Heads")
    elif computer_method_2 == 0 and user_guess == "heads":
        print("sorry! you lose!")
        print("the computer's coin toss result was: Tails")
    elif computer_method_2 == 1 and user_guess == "tails":
        print("sorry! you lose!")
        print("the computer's coin toss result was: Heads")
    elif computer_method_2 == 0 and user_guess == "tails":
        print("congratulation! you won!")
        print("the computer's coin toss result was: Tails")
    else:
        print("invalid choice. please select either Heads or Tails only")
else:
    print("invalid choice. please select either 1 or 2 only")