import random

player_choice = input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors): ")

computer_choice = random.randrange(2)

if player_choice == 1 and computer_choice == 2:
    print("Computer Wins")
elif player_choice == 2 and computer_choice == 3:
    print("Computer Wins")
elif player_choice == 3 and computer_choice == 1:
    print("Computer Wins")
elif player_choice == computer_choice:
    print("Draw")
else:
    print("You win!")