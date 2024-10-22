# -*- coding: utf-8 -*-
"""rock paper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q3NmUcq5bY_Vw3OhaHwCcqgDQEDIjP7U
"""

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    options = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore -> You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"\nFinal Score -> You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()