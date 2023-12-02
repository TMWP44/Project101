import random

response = "y"

while response.lower() == "y":
    dice_result = random.randint(1, 6)

    if dice_result == 1:
        print("---------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("---------")
    elif dice_result == 2:
        print("---------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("---------")
    elif dice_result == 3:
        print("---------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("---------")
    elif dice_result == 4:
        print("---------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("---------")
    elif dice_result == 5:
        print("---------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("---------")
    elif dice_result == 6:
        print("---------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("---------")

    response = input("Do you want to roll the dice again? (y/n): ")

print("Thanks for playing! Goodbye!")
