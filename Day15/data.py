# Coffee Machine Program Data

# Menu - Drink recipes and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources in the coffee machine
resources = {
    "water": 300,    # ml
    "milk": 200,     # ml  
    "coffee": 100,   # g
    "money": 0       # dollars
}

# Coin values for payment processing
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Alternative coin input format (if you want to use this approach)
COIN_VALUES = [
    ("quarters", 0.25),
    ("dimes", 0.10), 
    ("nickles", 0.05),
    ("pennies", 0.01)
]