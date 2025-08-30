import random
import os
from art import logo, vs
from game_data import data

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess and the follower count and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def format_data(account):
    """Takes the account data and returns printable format"""
    account_name = account["name"]
    account_descr = account["description"] 
    account_country = account["country"]
    return f"{account_name}, {account_descr}, from {account_country}"

def play_game():
    """Main game function"""
    clear_screen()
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        # Make sure we don't compare the same character
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        print()  # Add line gap
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Validate input
        while guess not in ['a', 'b']:
            guess = input("Please enter 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        
        clear_screen()
        print(logo)
        
        if is_correct:
            score += 1
            print(f"✅ You're right! Current score: {score}")
            print(f"A had {a_follower_count:,} followers")
            print(f"B had {b_follower_count:,} followers")
            print("-" * 40)
        else:
            print(f"❌ Sorry, that's wrong. Final score: {score}")
            print(f"A: {account_a['name']} had {a_follower_count:,} followers")
            print(f"B: {account_b['name']} had {b_follower_count:,} followers")
            game_should_continue = False

# Run the game
if __name__ == "__main__":
    play_again = True
    while play_again:
        play_game()
        play = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play != 'y':
            play_again = False
            clear_screen()
            print("Thanks for playing! 🎌")