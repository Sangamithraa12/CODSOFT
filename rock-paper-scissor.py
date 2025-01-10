import random

user_score = 0
computer_score = 0

def print_welcome_message():
    """Display the welcome message and instructions."""
    print("\n=== Welcome to the Rock-Paper-Scissors Game ===")
    print("Instructions:")
    print("1. Choose 'rock', 'paper', or 'scissors' to play.")
    print("2. The computer will also make its choice.")
    print("3. Rock beats scissors, scissors beat paper, paper beats rock.")
    print("4. Type 'exit' to quit the game at any time.")
    print("=" * 50)

def get_user_choice():
    """Prompt the user to make a choice."""
    while True:
        user_choice = input("\nYour choice (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors", "exit"]:
            return user_choice
        else:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and the computer."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def display_round_result(result):
    """Display the result of the current round."""
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win this round!")
    else:
        print("Result: Computer wins this round!")

def update_scores(result):
    """Update the scores based on the round's result."""
    global user_score, computer_score
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

def display_scores():
    """Display the current scores."""
    print("\nCurrent Scores:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

def ask_to_play_again():
    """Ask the user if they want to play another round."""
    while True:
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def play_game():
    """Main game loop."""
    print_welcome_message()
    
    while True:
        user_choice = get_user_choice()
        if user_choice == "exit":
            print("\nExiting the game. Thanks for playing!")
            break
        
        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        display_round_result(result)
        
        update_scores(result)
        display_scores()
        
        if not ask_to_play_again():
            print("\nThank you for playing! Final Scores:")
            display_scores()
            print("Goodbye!")
            break

play_game()
