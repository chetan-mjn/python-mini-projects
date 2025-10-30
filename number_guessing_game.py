import random

random_num = random.randint(1,100)
count = 0
chances = 6


print("-----WELCOME TO NUMBER GUESSING GAME-----")
print("Guess the number between 1-100. You only have 5 tries.")



while count < chances:
    count += 1
    num = int(input("Guess a number: "))

    if num == random_num:
            print(f"WOW! YOU GUESSED THAT RIGHT IN {count} TRIES.")
            break

    elif chances <= count and num != random_num:
         print("SORRY! YOUR ARE OUT OF MOVES. PLEASE TRY AGAIN.")

    elif num > random_num:
        print("too high")
        
    elif num < random_num:
        print("too low")
    
