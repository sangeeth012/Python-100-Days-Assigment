print("Welcome to Treasure Island. Your mission is to find the treasure.")

option = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if option == "left":
    option = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if option == "wait":
        option = input(
            "You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which colour do you choose? ").lower()

        if option == "blue":
            print("Eaten by beasts. Game Over.")
        elif option == "yellow":
            print("You found the treasure! You win! 🏆")
        elif option == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
