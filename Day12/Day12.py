import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer):
    """Compares guess with answer and provides feedback."""
    if user_guess > actual_answer:
        print("Too High.")
    elif user_guess < actual_answer:
        print("Too Low.")
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return True 

def set_difficulty():
    """Sets the number of attempts based on difficulty level."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Main game function."""
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    # Uncomment the next line for debugging
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = None  

    while turns > 0:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))

        if check_answer(guess, answer):  # If correct, exit the loop
            return
        
        turns -= 1  # Reduce attempts

    print(f"You've run out of attempts! The correct answer was {answer}.")

# Run the game
from art import logo
print(logo)
game()
