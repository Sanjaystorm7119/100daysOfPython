import random

list1 = ["random", "mouse", "keyboard", "monitor", "computer", "laptop", "tablet", "smartphone", "headphones", "speaker"]
print("Welcome to the Hangman Game!")
word = random.choice(list1)
guesses = ""
turns = 6
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()
    
    if failed == 0:
        print("You won!")
        break
    
    guess = input("Guess a character: ").lower()
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print(f"Wrong! You have {turns} attempts left.")
        if turns == 0:
            print("You lost! The word was:", word)
    else:
        print("Good guess!")
        print("Current guesses:", guesses)
        print("Current word:", " ".join([char if char in guesses else "_" for char in word]))
        print()
        if all(char in guesses for char in word):
            print("Congratulations! You've guessed the word:", word)
        