import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to the Rock-Paper-Scissors Game!")
while True:
    player_choice = input("Make your choice (rock, paper, scissors or exit): ").lower()
    if player_choice == "exit":
        print("Game over! See you next time!")
        break
    elif player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        continue

    computer_choice_result = computer_choice()
    print(f"Computer's choice: {computer_choice_result}")

    result = determine_winner(player_choice, computer_choice_result)
    print(result)
    print("-" * 30)
