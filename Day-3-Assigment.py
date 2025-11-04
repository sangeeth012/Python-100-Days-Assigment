import random

game = ["stone", "paper", "scissor"]

computer_choice = random.choice(game)
user_choice = input("Enter your choice (stone, paper, scissor): ").lower()

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("Match draw!")
elif ((user_choice == "stone" and computer_choice == "scissor") or
      (user_choice == "paper" and computer_choice == "stone") or
      (user_choice == "scissor" and computer_choice == "paper")):
    print("You won!")
else:
    print("Computer won!")
