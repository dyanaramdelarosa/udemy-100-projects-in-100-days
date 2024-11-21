import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def print_choice(game_images: list, choice: int):
    if choice < len(game_images) and choice >= 0:
        print(game_images[choice])
    else:
        print("undefined")


def print_winner(player_choice: int, computer_choice: int):
    if player_choice < 0 or player_choice > 2:
        print("You typed an invalid number, you lose!")
    elif player_choice == computer_choice:
        print("It's a draw")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose")
    elif player_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > player_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win")


if __name__ == "__main__":
    game_images = [rock, paper, scissors]
    choices = [0, 1, 2]
    try:
        player_choice = int(
            input(
                "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
            )
        )
    except ValueError:
        player_choice = -1

    computer_choice = random.choice(choices)
    print_choice(game_images, player_choice)
    print("Computer chose:")
    print_choice(game_images, computer_choice)
    print_winner(player_choice, computer_choice)
