import os
from data import MENU
from art import logo

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_resources(drinks):
    """Check if there is enough resources to make a coffee"""
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredients in drink_ingredients:
        if resources["ingredients"] < drink_ingredients["ingredients"]:
            print("Sorry there is not enough {ingredients}.")
            return False
        return True

def print_report():
    """Print the report of resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money']}")

def process_coints():
    """Process coints as input and calculate total value"""
    print("Please input value.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_transaction(drink, money_inserted):
    """Check if transaction is successful"""
    drink_cost = MENU[drink]["cost"]
    if money_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_inserted > drink_cost:
        change = money_inserted - drink_cost
        print(f"Here is ${change:.2f} in change.")

    # Add profit to Machine
    resources["money"] += drink_cost
    return True

def make_coffee(drink):
    """Deduct resources and make the coffee"""
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredients in drink_ingredients:
        resources[ingredients] -= resources[drink_ingredients]
    print(f"Here is your {drink}. Enjoy!")

def start_machine():
    """Start The Main Coffee Machine"""
    machine_on = True

    while machine_on:
        clear_screen()
        print(logo)

        take_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if take_order == "off":
            print("Turning off Machine")
            machine_on = False
        elif take_order == "report":
            print_report()
            input("\nPress Enter to continue...")
        elif take_order in MENU:
            # Check if resources are sufficient
            if check_resources(take_order):
                payment = process_coints()
                # Check if transaction is successful
                if check_resources(take_order, payment):
                    # Make Coffee
                    make_coffee(take_order)
                    input("\nPress Enter to continue...")
        else:
            print("Invalid selection. Please try again.")
            input("Press Enter to continue...")

# Start the machine
if __name__ == "__main__":
    start_machine()