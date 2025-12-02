import random

# mapping numbers to choices
choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}

# initialize scores
draw_score = 0
player_score = 0
computer_score = 0
round_number = 1
history = []

# welcome and get player name
player_name = input("Enter your name: ").strip()
print(f"Welcome, {player_name}! Let's play Rock-Paper-Scissors.")


def show_rules():
    print("\n--- Rules ---")
    print("Rock 🪨 beats Scissors ️✂️")
    print("Paper 📄 beats Rock 🪨")
    print("Scissors ✂️️ beats Paper 📄")
    print("Enter 0 to quit, 9 to reset the game, 8 to see rules.\n")


show_rules()

while True:
    print(f"--- Round {round_number} ---")
    try:
        player_choice = int(
            input("Select your option (1 = Rock, 2 = Paper, 3 = Scissors, 0 = Quit, 9 = Reset, 8 = Rules): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if player_choice == 0:
        print("Thanks for playing!")
        print(f"Final Score -> {player_name}: {player_score}, Computer: {computer_score}, Draws: {draw_score}")

        # overall winner
        if player_score > computer_score:
            print("Overall winner: You!")
        elif computer_score > player_score:
            print("Overall winner: Computer!")
        else:
            print("Overall result: It's a tie!")

        print("\nGame History:")
        for r in history:
            print(r)
        break

    elif player_choice == 9:
        # reset the game
        draw_score = 0
        player_score = 0
        computer_score = 0
        round_number = 1
        history.clear()
        print("Game reset. Scores cleared.\n")
        show_rules()
        continue

    elif player_choice == 8:
        show_rules()
        continue

    player_choice_name = choices.get(player_choice, "Invalid choice")
    if player_choice_name == "Invalid choice":
        print("Select from 1, 2, or 3.")
        continue

    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice]

    print(f"You picked: {player_choice_name}")
    print(f"The computer picked: {computer_choice_name}")

    # determine winner
    if player_choice == computer_choice:
        result = "Draw"
        draw_score += 1
        print("It's a draw!")
    elif (player_choice == 1 and computer_choice == 3) or \
            (player_choice == 2 and computer_choice == 1) or \
            (player_choice == 3 and computer_choice == 2):
        result = "Win"
        player_score += 1
        print("You win!")
    else:
        result = "Loss"
        computer_score += 1
        print("Computer wins!")

    # store round history
    history.append(
        f"Round {round_number}: {player_name} ({player_choice_name}) vs Computer ({computer_choice_name}) -> {result}")

    print(f"Score -> {player_name}: {player_score}, Computer: {computer_score}, Draw: {draw_score}\n")
    round_number += 1
