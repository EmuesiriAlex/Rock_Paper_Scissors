import random
import json
import os
from datetime import datetime

ASCII_ART = {
    "Rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "Paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    "Scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,
    "Lizard": """
        ()_()
       (_ . _)>
        /  |
       /   |___/|
      (_________/
    """,
    "Spock": """
       ____
      /___ \\
     //   \\ \\
    ||     || |
    ||     || |
     \\\\___// /
      \\____//
    """
}

CLASSIC_CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors"}
EXTENDED_CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

CLASSIC_WINS = {
    ("Rock", "Scissors"): "Rock crushes Scissors",
    ("Paper", "Rock"): "Paper covers Rock",
    ("Scissors", "Paper"): "Scissors cuts Paper"
}

EXTENDED_WINS = {
    ("Rock", "Scissors"): "Rock crushes Scissors",
    ("Rock", "Lizard"): "Rock crushes Lizard",
    ("Paper", "Rock"): "Paper covers Rock",
    ("Paper", "Spock"): "Paper disproves Spock",
    ("Scissors", "Paper"): "Scissors cuts Paper",
    ("Scissors", "Lizard"): "Scissors decapitates Lizard",
    ("Lizard", "Paper"): "Lizard eats Paper",
    ("Lizard", "Spock"): "Lizard poisons Spock",
    ("Spock", "Rock"): "Spock vaporizes Rock",
    ("Spock", "Scissors"): "Spock smashes Scissors"
}

HIGH_SCORES_FILE = "high_scores.json"


class GameStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.current_win_streak = 0
        self.current_loss_streak = 0
        self.best_win_streak = 0
        self.worst_loss_streak = 0
        self.history = []
        self.round_number = 1

    def record_win(self):
        self.wins += 1
        self.current_win_streak += 1
        self.current_loss_streak = 0
        if self.current_win_streak > self.best_win_streak:
            self.best_win_streak = self.current_win_streak

    def record_loss(self):
        self.losses += 1
        self.current_loss_streak += 1
        self.current_win_streak = 0
        if self.current_loss_streak > self.worst_loss_streak:
            self.worst_loss_streak = self.current_loss_streak

    def record_draw(self):
        self.draws += 1
        self.current_win_streak = 0
        self.current_loss_streak = 0

    def get_win_rate(self):
        total = self.wins + self.losses
        if total == 0:
            return 0.0
        return (self.wins / total) * 100

    def get_total_games(self):
        return self.wins + self.losses + self.draws

    def reset(self):
        self.__init__()

    def display_stats(self):
        print("\n========== STATISTICS ==========")
        print(f"Total Games: {self.get_total_games()}")
        print(f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}")
        print(f"Win Rate: {self.get_win_rate():.1f}%")
        print(f"Current Win Streak: {self.current_win_streak}")
        print(f"Current Loss Streak: {self.current_loss_streak}")
        print(f"Best Win Streak: {self.best_win_streak}")
        print(f"Worst Loss Streak: {self.worst_loss_streak}")
        print("================================\n")


def load_high_scores():
    if os.path.exists(HIGH_SCORES_FILE):
        try:
            with open(HIGH_SCORES_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []


def save_high_scores(scores):
    with open(HIGH_SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)


def add_high_score(player_name, wins, losses, win_rate, mode):
    scores = load_high_scores()
    scores.append({
        "player": player_name,
        "wins": wins,
        "losses": losses,
        "win_rate": round(win_rate, 1),
        "mode": mode,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    scores = sorted(scores, key=lambda x: (-x["win_rate"], -x["wins"]))[:10]
    save_high_scores(scores)


def display_high_scores():
    scores = load_high_scores()
    print("\n========== HIGH SCORES ==========")
    if not scores:
        print("No high scores yet!")
    else:
        print(f"{'Rank':<5} {'Player':<15} {'Wins':<6} {'Losses':<7} {'Win %':<8} {'Mode':<10} {'Date'}")
        print("-" * 70)
        for i, score in enumerate(scores, 1):
            print(
                f"{i:<5} {score['player']:<15} {score['wins']:<6} {score['losses']:<7} {score['win_rate']:<8.1f} {score['mode']:<10} {score['date']}")
    print("=================================\n")


def show_ascii_art(choice_name):
    if choice_name in ASCII_ART:
        print(ASCII_ART[choice_name])


def get_computer_choice(choices, difficulty="medium", player_history=None):
    if difficulty == "easy":
        return random.choice(list(choices.keys()))
    elif difficulty == "hard" and player_history and len(player_history) >= 3:
        from collections import Counter
        recent = [h[0] for h in player_history[-5:]]
        most_common = Counter(recent).most_common(1)[0][0]
        if len(choices) == 3:
            counter_moves = {"Rock": 2, "Paper": 3, "Scissors": 1}
        else:
            counter_moves = {"Rock": 2, "Paper": 3, "Scissors": 1, "Lizard": 1, "Spock": 4}
        return counter_moves.get(most_common, random.choice(list(choices.keys())))
    else:
        return random.choice(list(choices.keys()))


def determine_winner(player_choice, computer_choice, wins_dict):
    if player_choice == computer_choice:
        return "draw", None
    if (player_choice, computer_choice) in wins_dict:
        return "win", wins_dict[(player_choice, computer_choice)]
    return "loss", wins_dict.get((computer_choice, player_choice), "")


def show_rules(extended=False):
    print("\n========== RULES ==========")
    if extended:
        print("Rock-Paper-Scissors-Lizard-Spock!")
        print("\nWinning combinations:")
        print("  Rock crushes Scissors and Lizard")
        print("  Paper covers Rock and disproves Spock")
        print("  Scissors cuts Paper and decapitates Lizard")
        print("  Lizard eats Paper and poisons Spock")
        print("  Spock vaporizes Rock and smashes Scissors")
    else:
        print("Classic Rock-Paper-Scissors!")
        print("\nWinning combinations:")
        print("  Rock crushes Scissors")
        print("  Paper covers Rock")
        print("  Scissors cuts Paper")
    print("===========================\n")


def show_main_menu():
    print("\n========== MAIN MENU ==========")
    print("1. Single Player (vs Computer)")
    print("2. Two Player Mode")
    print("3. View High Scores")
    print("4. View Rules")
    print("0. Quit")
    print("================================")


def show_game_options():
    print("\n========== GAME OPTIONS ==========")
    print("1. Classic (Rock-Paper-Scissors)")
    print("2. Extended (Rock-Paper-Scissors-Lizard-Spock)")
    print("0. Back to Main Menu")
    print("==================================")


def show_difficulty_menu():
    print("\n========== DIFFICULTY ==========")
    print("1. Easy (Random)")
    print("2. Medium (Slightly Smart)")
    print("3. Hard (Analyzes Your Patterns)")
    print("================================")


def show_mode_menu():
    print("\n========== GAME MODE ==========")
    print("1. Free Play (Unlimited Rounds)")
    print("2. Best of 3")
    print("3. Best of 5")
    print("4. Best of 7")
    print("5. Custom (Choose number of wins)")
    print("================================")


def get_valid_input(prompt, valid_options):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            print(f"Please enter one of: {valid_options}")
        except ValueError:
            print("Please enter a valid number.")


def play_round(player_name, choices, wins_dict, stats, difficulty, show_art=True):
    choice_list = ", ".join([f"{k} = {v}" for k, v in choices.items()])
    print(f"\n--- Round {stats.round_number} ---")
    print(f"Choose: {choice_list}")
    print("(7 = Stats, 8 = Rules, 9 = Reset, 0 = Quit)")

    player_input = get_valid_input("Your choice: ", list(choices.keys()) + [0, 7, 8, 9])

    if player_input == 0:
        return "quit"
    elif player_input == 7:
        stats.display_stats()
        return "continue"
    elif player_input == 8:
        show_rules(len(choices) > 3)
        return "continue"
    elif player_input == 9:
        stats.reset()
        print("Game reset! All scores cleared.\n")
        return "continue"

    player_choice = choices[player_input]
    computer_choice_key = get_computer_choice(choices, difficulty,
                                              [(h[0], h[1]) for h in stats.history])
    computer_choice = choices[computer_choice_key]

    print(f"\n{player_name} chose: {player_choice}")
    if show_art:
        show_ascii_art(player_choice)
    print(f"Computer chose: {computer_choice}")
    if show_art:
        show_ascii_art(computer_choice)

    result, reason = determine_winner(player_choice, computer_choice, wins_dict)

    if result == "draw":
        stats.record_draw()
        print("It's a DRAW!")
    elif result == "win":
        stats.record_win()
        print(f"{reason}! {player_name} WINS!")
    else:
        stats.record_loss()
        print(f"{reason}! Computer WINS!")

    stats.history.append((player_choice, computer_choice, result))
    stats.round_number += 1

    print(f"\nScore: {player_name}: {stats.wins} | Computer: {stats.losses} | Draws: {stats.draws}")

    if stats.current_win_streak >= 3:
        print(f"*** {stats.current_win_streak} WIN STREAK! ***")
    elif stats.current_loss_streak >= 3:
        print(f"*** {stats.current_loss_streak} loss streak... ***")

    return result


def play_single_player(player_name):
    show_game_options()
    game_type = get_valid_input("Select game type: ", [0, 1, 2])
    if game_type == 0:
        return

    extended = (game_type == 2)
    choices = EXTENDED_CHOICES if extended else CLASSIC_CHOICES
    wins_dict = EXTENDED_WINS if extended else CLASSIC_WINS
    mode_name = "Extended" if extended else "Classic"

    show_difficulty_menu()
    diff_choice = get_valid_input("Select difficulty: ", [1, 2, 3])
    difficulty = {1: "easy", 2: "medium", 3: "hard"}[diff_choice]

    show_mode_menu()
    mode_choice = get_valid_input("Select game mode: ", [1, 2, 3, 4, 5])

    target_wins = None
    if mode_choice == 2:
        target_wins = 2
    elif mode_choice == 3:
        target_wins = 3
    elif mode_choice == 4:
        target_wins = 4
    elif mode_choice == 5:
        target_wins = get_valid_input("Enter number of wins needed: ", list(range(1, 100)))

    stats = GameStats()
    show_rules(extended)

    print(f"\nStarting {mode_name} mode on {difficulty.upper()} difficulty!")
    if target_wins:
        print(f"First to {target_wins} wins!")
    print("Let's play!\n")

    while True:
        result = play_round(player_name, choices, wins_dict, stats, difficulty)

        if result == "quit":
            break

        if target_wins and (stats.wins >= target_wins or stats.losses >= target_wins):
            print("\n========== GAME OVER ==========")
            if stats.wins >= target_wins:
                print(f"Congratulations {player_name}! You won the match!")
            else:
                print("Computer wins the match! Better luck next time!")
            stats.display_stats()
            break

    if stats.get_total_games() > 0:
        add_high_score(player_name, stats.wins, stats.losses, stats.get_win_rate(), mode_name)
        print("Your score has been saved to the leaderboard!")

    print("\n--- Game History ---")
    for i, (p, c, r) in enumerate(stats.history, 1):
        print(f"Round {i}: {player_name} ({p}) vs Computer ({c}) -> {r.upper()}")


def play_two_player():
    print("\n========== TWO PLAYER MODE ==========")
    player1_name = input("Player 1, enter your name: ").strip() or "Player 1"
    player2_name = input("Player 2, enter your name: ").strip() or "Player 2"

    show_game_options()
    game_type = get_valid_input("Select game type: ", [0, 1, 2])
    if game_type == 0:
        return

    extended = (game_type == 2)
    choices = EXTENDED_CHOICES if extended else CLASSIC_CHOICES
    wins_dict = EXTENDED_WINS if extended else CLASSIC_WINS

    show_mode_menu()
    mode_choice = get_valid_input("Select game mode: ", [1, 2, 3, 4, 5])

    target_wins = None
    if mode_choice == 2:
        target_wins = 2
    elif mode_choice == 3:
        target_wins = 3
    elif mode_choice == 4:
        target_wins = 4
    elif mode_choice == 5:
        target_wins = get_valid_input("Enter number of wins needed: ", list(range(1, 100)))

    p1_wins = 0
    p2_wins = 0
    draws = 0
    round_num = 1
    history = []

    show_rules(extended)
    print(f"\n{player1_name} vs {player2_name}!")
    if target_wins:
        print(f"First to {target_wins} wins!")
    print("Let's play!\n")

    while True:
        print(f"\n--- Round {round_num} ---")
        choice_list = ", ".join([f"{k} = {v}" for k, v in choices.items()])
        print(f"Choices: {choice_list} (0 = Quit)")

        print(f"\n{player1_name}'s turn (others look away!):")
        p1_input = get_valid_input("Your choice: ", list(choices.keys()) + [0])
        if p1_input == 0:
            break
        p1_choice = choices[p1_input]

        print("\n" * 20)

        print(f"{player2_name}'s turn (others look away!):")
        p2_input = get_valid_input("Your choice: ", list(choices.keys()) + [0])
        if p2_input == 0:
            break
        p2_choice = choices[p2_input]

        print("\n" * 5)
        print("========== REVEAL ==========")
        print(f"{player1_name} chose: {p1_choice}")
        show_ascii_art(p1_choice)
        print(f"{player2_name} chose: {p2_choice}")
        show_ascii_art(p2_choice)

        if p1_choice == p2_choice:
            draws += 1
            result = "Draw"
            print("It's a DRAW!")
        elif (p1_choice, p2_choice) in wins_dict:
            p1_wins += 1
            result = f"{player1_name} wins"
            print(f"{wins_dict[(p1_choice, p2_choice)]}! {player1_name} WINS!")
        else:
            p2_wins += 1
            result = f"{player2_name} wins"
            print(f"{wins_dict[(p2_choice, p1_choice)]}! {player2_name} WINS!")

        history.append((p1_choice, p2_choice, result))
        round_num += 1

        print(f"\nScore: {player1_name}: {p1_wins} | {player2_name}: {p2_wins} | Draws: {draws}")

        if target_wins and (p1_wins >= target_wins or p2_wins >= target_wins):
            print("\n========== GAME OVER ==========")
            if p1_wins >= target_wins:
                print(f"Congratulations {player1_name}! You won the match!")
            else:
                print(f"Congratulations {player2_name}! You won the match!")
            break

    print("\n--- Game History ---")
    for i, (p1, p2, r) in enumerate(history, 1):
        print(f"Round {i}: {player1_name} ({p1}) vs {player2_name} ({p2}) -> {r}")


def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║     ROCK - PAPER - SCISSORS - LIZARD - SPOCK              ║
    ║                    Ultimate Edition                        ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    player_name = input("Enter your name: ").strip() or "Player"
    print(f"\nWelcome, {player_name}!")

    while True:
        show_main_menu()
        choice = get_valid_input("Select option: ", [0, 1, 2, 3, 4])

        if choice == 0:
            print(f"\nThanks for playing, {player_name}! Goodbye!")
            break
        elif choice == 1:
            play_single_player(player_name)
        elif choice == 2:
            play_two_player()
        elif choice == 3:
            display_high_scores()
        elif choice == 4:
            print("\n1. Classic Rules")
            print("2. Extended Rules")
            rules_choice = get_valid_input("Select: ", [1, 2])
            show_rules(rules_choice == 2)


if __name__ == "__main__":
    main()
