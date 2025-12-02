import random

player_choice = int(input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors): "))

if player_choice == 1:
    player_choice_name = "Rock"
elif player_choice == 2:
    player_choice_name = "Paper"
else:
    player_choice_name = "Scissors"

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice_name = "Rock"
elif computer_choice == 2:
    computer_choice_name = "Paper"
else:
    computer_choice_name = "Scissors"

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

print(f"Player choice: {player_choice}")
print(f"Player choice: {player_choice_name}")
print(f"Computer choice: {computer_choice}")
print(f"Computer choice: {computer_choice_name}")