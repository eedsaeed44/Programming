import random
computer_guess = random.randint(0,20)
user_guess = int(input("Guess a number betwen 0 and 20 : "))
while computer_guess != user_guess:
    if user_guess > computer_guess:
        user_guess = int(input("too high! guess again: "))
    else:
        user_guess = int(input("too low! guess again: "))

print("congratulation! correct guess")