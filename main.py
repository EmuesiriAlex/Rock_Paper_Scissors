import random
from secrets import choice

#mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

player_choice = int(input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors): "))
player_choice = choices.get(player_choice, "Invalid choice")


if player_choice == "Invalid choice":
    print("Select from 1, 2 or 3.")
    exit()

computer_choice = random.randint(1, 3)
player_choice = choices.get(player_choice)

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

# print(f"Player choice: {player_choice}")
# print(f"Player choice: {player_choice_name}")
# print(f"Computer choice: {computer_choice}")
# print(f"Computer choice: {computer_choice_name}")