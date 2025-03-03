**# Python Beginner Course (Day 1 - Day 9) Theory & Examples**

## **Day 1 - Working with Variables in Python to Manage Data**

### **Definition:**

A variable in Python is a reserved memory location to store values. It acts as a placeholder for data.

### **Use Cases:**

- Storing user input
- Keeping track of scores in games
- Managing temporary values in calculations

### **Concepts:**

Variables are used to store data that can be referenced and manipulated later in a program. In Python, variables do not require explicit declaration; they are dynamically typed, meaning their type is inferred based on the value assigned.

- **String Variables**: Store sequences of characters (text).
- **Integer Variables**: Store whole numbers.
- **Float Variables**: Store decimal numbers.
- **Boolean Variables**: Store `True` or `False` values.
- **Assigning values**: Done using `=`.
- **Printing values**: Use `print()`.
- **Taking user input**: Use `input()`.
- **String concatenation**: Joining strings together using `+`.
- **Comments**: Use `#` for single-line comments and triple quotes `'''` or `"""` for multi-line comments.
- **Naming Conventions**: Variable names should be descriptive and follow the snake\_case naming convention.

### **Example:**

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

---

## **Day 2 - Understanding Data Types and Type Conversion**

### **Definition:**

Data types define the kind of value a variable can hold.

### **Use Cases:**

- Ensuring calculations are performed correctly
- Converting data formats when taking user input

### **Concepts:**

Python has several built-in data types that are automatically assigned based on the value stored in a variable. Understanding data types is crucial because different types interact in unique ways.

- **Basic Data Types:**
  - `int`: Whole numbers (e.g., 10, -3, 42)
  - `float`: Decimal numbers (e.g., 3.14, -0.99)
  - `str`: Text or sequence of characters (e.g., "Hello")
  - `bool`: Boolean values (`True` or `False`)
- **Type Checking:** Use `type()` to determine the data type of a variable.
- **Type Conversion:** Convert one data type into another using `str()`, `int()`, `float()`.
- **Mathematical Operations:**
  - `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division)
  - `**` (exponentiation), `//` (floor division), `%` (modulus)

### **Example:**

```python
age = int(input("Enter your age: "))
future_age = age + 5
print("In 5 years, you will be " + str(future_age) + " years old.")
```

---

## **Day 3 - Control Flow and Logical Operators**

### **Definition:**

Control flow determines the execution order of program statements.

### **Use Cases:**

- Making decisions in applications (e.g., login authentication)
- Implementing game logic (e.g., win/loss conditions)

### **Concepts:**

Control flow dictates how a program executes different statements based on conditions.

- **Conditional Statements:**
  - `if`: Executes code block if the condition is true.
  - `elif`: Specifies an additional condition if the first one is false.
  - `else`: Executes if none of the previous conditions are met.
- **Comparison Operators:** (`==`, `!=`, `>`, `<`, `>=`, `<=`) are used to compare values.
- **Logical Operators:**
  - `and`: Both conditions must be true.
  - `or`: At least one condition must be true.
  - `not`: Reverses the condition.
- **Nested Conditions:** Placing one `if` statement inside another.

### **Example:**

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

---

## **Day 4 - Randomisation and Python Lists**

### **Definition:**

Randomisation allows generating unpredictable outcomes. Lists store multiple values.

### **Use Cases:**

- Creating random events in games
- Storing multiple elements in structured data

### **Concepts:**

- **Randomisation:** `import random` to generate random values.
- **Lists:** Ordered collections of items.
  - Create with square brackets `[]`.
  - Access elements using index (`list[0]` for the first item, `list[-1]` for the last item).
  - Modify with `list.append()`, `list.remove()`, `list.pop()`.
- **Shuffling & Choosing Elements Randomly:** Use `random.choice()` to pick a random element.

### **Example:**

```python
import random
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print("Random fruit: " + random_fruit)
```

---

## **Day 5 - Python Loops**

### **Definition:**

Loops allow executing a block of code multiple times.

### **Use Cases:**

- Iterating over lists of data
- Repeating tasks without manual intervention

### **Concepts:**

Loops allow repeating a block of code multiple times.

- **For Loop:** Iterates over sequences like lists, strings, or `range()`.
- **While Loop:** Continues running while a condition is `True`.
- **Break & Continue:**
  - `break`: Exits the loop.
  - `continue`: Skips the rest of the current iteration and moves to the next.

### **Example:**

```python
for i in range(1, 6):
    print("Iteration", i)
```

```python
number = 1
while number < 5:
    print("Number is", number)
    number += 1
```

---

## **Day 6 - Python Functions & Karel**

### **Definition:**

A function is a reusable block of code that performs a specific task.

### **Use Cases:**

- Reducing redundancy in code
- Organizing large programs into smaller, manageable parts

### **Concepts:**

- Defining functions with `def function_name():`
- Using parameters and return values
- Calling functions to execute their code

### **Example:**

```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```

Day 6 - Python Functions & Karel
Definition:
A function is a reusable block of code that performs a specific task.
In some courses, “Karel” is a small educational environment used to teach basic programming logic.

Use Cases:
Reducing redundancy in code by encapsulating repetitive tasks
Organizing large programs into smaller, more manageable parts
Teaching fundamental concepts of commands and procedures (in Karel)
Concepts:
Defining functions with def function_name():
Using parameters and return values
Calling functions to execute their code
Basic Karel commands (if applicable), such as moving, turning, and placing markers
Example:
python
Copy
Edit
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
Day 7 - Hangman Game
Definition:
Hangman is a classic word-guessing game where the player tries to guess the hidden word one letter at a time.

Use Cases:
Practicing strings, loops, and conditional logic
Building interactive command-line games
Introducing basic game logic and user input handling
Concepts:
String Manipulation & Lists: Splitting words into letters, comparing guessed letters
User Input & Conditions: Checking if the guess is in the hidden word
Looping Until Condition is Met: Repeating until the word is guessed or attempts run out
Example (Basic Hangman Concept):
python
Copy
Edit
word = "python"
guessed_letters = []
attempts = 6

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    # Check if all letters are guessed
    all_guessed = True
    for char in word:
        if char not in guessed_letters:
            all_guessed = False
            break

    if all_guessed:
        print("You guessed the word! It was", word)
        break
else:
    print("You ran out of attempts! The word was", word)
Day 8 - Function Parameters & Caesar Cipher
Definition:
The Caesar Cipher is a simple encryption technique that shifts each letter of the plaintext by a certain number of positions in the alphabet.

Use Cases:
Demonstrating how functions can take parameters
Understanding basic encryption and decryption logic
Learning about string manipulation and ASCII values
Concepts:
Function Parameters & Return Values: Passing the text and shift values
String Manipulation: Converting characters based on their ASCII code
Modular Arithmetic: Ensuring letters wrap around from Z back to A
Example (Basic Caesar Cipher):
python
Copy
Edit
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # Only shift alphabetic characters
        if char.isalpha():
            # Determine if it's uppercase (A-Z) or lowercase (a-z)
            base = 'A' if char.isupper() else 'a'
            # Convert char to 0-25 range
            offset = ord(char) - ord(base)
            # Shift within 0-25
            shifted = (offset + shift) % 26
            # Convert back to ASCII
            new_char = chr(ord(base) + shifted)
            result += new_char
        else:
            # Leave non-alphabetic characters as they are
            result += char
    return result

encrypted = caesar_cipher("Hello World!", 3)
print(encrypted)  # Khoor Zruog!
Day 9 - Dictionaries, Nesting, and the Secret Auction
Definition:
A dictionary is a Python data structure that stores data in key-value pairs.
Nesting refers to placing one data structure inside another, such as a list inside a dictionary or a dictionary inside a list.

Use Cases:
Storing and retrieving data by keys instead of indices
Organizing data into nested structures for complex applications
Creating auctions or leaderboards (where keys are participants and values are bids or scores)
Concepts:
Dictionaries: Defined with curly braces {}, containing key-value pairs.
Nesting: Combining lists and dictionaries for hierarchical data.
Iterating through Dictionaries: Accessing keys and values.
Secret Auction: Example use case where participants place bids stored in a dictionary.
Example:
python
Copy
Edit
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True

highest_bid = 0
winner = ""

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}!")
