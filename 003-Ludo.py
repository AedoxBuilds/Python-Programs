import random

print("🎲 Welcome to Ludo Dice Game 🎲")

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")

input(f"\n{player1}, press Enter to roll the dice...")
dice1 = random.randint(1, 6)
print(f"{player1} rolled: {dice1}")

input(f"\n{player2}, press Enter to roll the dice...")
dice2 = random.randint(1, 6)
print(f"{player2} rolled: {dice2}")

print("\n🏆 Result 🏆")

if dice1 > dice2:
    print(f"{player1} wins!")
elif dice2 > dice1:
    print(f"{player2} wins!")
else:
    print("It's a tie! Roll again.")
