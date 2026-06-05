import random
#Initializing scores
player_score = 0
computer_score = 0
draws = 0

while True:
    print("\n=== Rock-Paper-Scissors Game ===")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    #Human Choice
    player = int(input("Enter your choice (1-3) : "))
    if player < 1 or player > 3:
        print("Invalid choice! Please choose between 1 and 3.")
        continue

    # Computer Choice
    computer = random.randint(1, 3)
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    # Displaying choices
    print("Player choose:", choices[player])
    print("Computer choose:", choices[computer])

    #Determining the winner
    if player == computer:
        print("It's a Draw!")
        draws += 1

    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You Win!")
        player_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    # Displaying scoreboard
    print("\nScoreboard")
    print("Player:", player_score)
    print("Computer:", computer_score)
    print("Draws:", draws)

    # Play again
    choice = input("\nPlay again? (y/n): ")

    if choice.lower() == 'n':
        break

# Final result
print("\nFinal Score")
print("Player:", player_score)
print("Computer:", computer_score)
print("Draws:", draws)