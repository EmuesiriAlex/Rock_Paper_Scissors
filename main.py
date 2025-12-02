import random

# mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

# initialize scores
darw_score = 0
player_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"--- Round {round_number} ---")
    try:
        player_choice = int(input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors, 0 = Quit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if player_choice == 0:
        print("Thanks for playing!")
        print(f"Final Score -> You: {player_score}, Computer: {computer_score}, Draws: {darw_score}")
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
        darw_score += 1
    elif (player_choice == 1 and computer_choice == 3) or \
            (player_choice == 2 and computer_choice == 1) or \
            (player_choice == 3 and computer_choice == 2):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {player_score}, Computer: {computer_score}, Draw: {darw_score}")
    print()  # blank line between rounds
    round_number += 1
