#Rock paper scissors game

import random
options = ["rock", "paper", "scissor"]
bot_choice = random.choice(options)


print("---ROCK PAPER SCISSORS GAME---")
print("*press enter to start*")
start = input()

choice = input("Enter your choice: ")
choice = choice.lower()

while True:
    if choice == "paper" and bot_choice == "paper":
        print("Draw")
        break
    
    elif choice == "paper" and bot_choice == "rock":
        print("You won")
        break
    
    elif choice == "paper" and bot_choice == "scissor":
        print("Opps! Bot won.")
        break
    
    if choice == "rock" and bot_choice == "rock":
        print("Draw")
        break
    
    elif choice == "rock" and bot_choice == "scissor":
        print("You won")
        break
    
    elif choice == "rock" and bot_choice == "paper":
        print("Opps! Bot won.")
        break

    if choice == "scissor" and bot_choice == "scissor":
        print("Draw")
        break
    
    elif choice == "scissor" and bot_choice == "paper":
        print("You won")
        break
    
    elif choice == "scissor" and bot_choice == "rock":
        print("Opps! Bot won.")
        break
    
print(f"Bot chose : {bot_choice}")
