import random
print("what do you choose? rock, paper or scissor?")
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
system_choice = random.randint(0, 2)

while True:      
    # User input
    user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

    if user_choice == 0:
        print("You chose Rock")
        print(rock)
    elif user_choice == 1:
        print("You chose Paper")
        print(paper)
    elif user_choice == 2:
        print("You chose Scissors")
        print(scissors)
    else:
        print("Invalid choice. Please choose 0, 1, or 2.")
        exit()  # Exit the game if an invalid choice is made

    print("Computer chose:")        
    if system_choice == 0:
        print(rock)
    elif system_choice == 1:
        print(paper)
    else:
        print(scissors)

    # Determine the winner
    if system_choice == user_choice:
        print("It's a tie!")
    elif (user_choice == 0 and system_choice == 2) or (user_choice == 1 and system_choice == 0) or (user_choice == 2 and system_choice == 1):
        print("You win!")
    else:
        print("You lose!")