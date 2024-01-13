import random
words = ['panana', 'Strong', 'assembly', 'done']
random_word = random.choice(words)
gussed = input("please guess a letter : ").lower()
for letter in random_word:
    if letter == gussed:
        print("right")
    else:
        print("wronge")