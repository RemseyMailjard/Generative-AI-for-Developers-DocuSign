import random

def play_game():
    user_score = 0
    computer_score = 0
    print("Rock Paper Scissors Game")

    while True:
        user_input = input("Enter rock, paper, or scissors (or quit to stop playing): ").lower()
        if user_input == "quit":
            break

        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif (user_input == "rock" and computer_choice == "scissors") or \
             (user_input == "paper" and computer_choice == "rock") or \
             (user_input == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    print("Final Score")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("Computer won the game!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    play_game()
