import random

# mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

while True:
    try:
        player_choice = int(input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors, 0 = Quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if player_choice == 0:
        print("Thanks for playing!")
        break

    player_choice_name = choices.get(player_choice, "Invalid choice")
    if player_choice_name == "Invalid choice":
        print("Select from 1, 2, or 3.")
        continue

    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice]

    # display the choices
    print(f"You picked: {player_choice_name}.")
    print(f"The computer picked: {computer_choice_name}.")

    # determine winner
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 1 and computer_choice == 3) or \
            (player_choice == 2 and computer_choice == 1) or \
            (player_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

    print()  # blank line between rounds
