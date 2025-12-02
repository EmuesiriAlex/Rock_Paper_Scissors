import random

# mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

player_choice = int(input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors): "))
player_choice_name = choices.get(player_choice, "Invalid choice")

if player_choice == "Invalid choice":
    print("Select from 1, 2 or 3.")
    exit()

computer_choice = random.randint(1, 3)
computer_choice_name = choices.get(computer_choice)

# display the choices
print(f"The computer choose: {computer_choice_name}.")
print(f"You choose: {player_choice_name}.")

if player_choice == computer_choice:
    print("It's a draw!")

elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (
        player_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("Computer wins!")
