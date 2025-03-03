# **Python Beginner Course (Day 1 - Day 9) 🚀**

Welcome to the **Python Beginner Course**, a structured guide to mastering Python fundamentals in just 9 days! This course covers essential concepts with hands-on examples to help you solidify your Python skills. 🐍✨

---

## 📌 **Day 1 - Working with Variables in Python**
### **Definition**
A **variable** in Python is a memory location used to store data. Variables can hold different data types, and Python dynamically assigns types based on values.

### **Use Cases**
- Storing user input
- Keeping track of scores in games
- Managing temporary values in calculations

### **Concepts**
- String, Integer, Float, and Boolean Variables
- Assigning values using `=`
- Printing values using `print()`
- Taking user input with `input()`
- String concatenation using `+`
- Naming conventions: `snake_case`

### **Example**
```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```
---

## 📌 **Day 2 - Understanding Data Types & Type Conversion**
### **Definition**
Data types define the kind of values stored in variables.

### **Use Cases**
- Ensuring correct calculations
- Converting user input formats

### **Concepts**
- **Basic Data Types**: `int`, `float`, `str`, `bool`
- **Type Checking**: `type(variable)`
- **Type Conversion**: `int()`, `str()`, `float()`
- **Mathematical Operations**: `+`, `-`, `*`, `/`, `**`, `//`, `%`

### **Example**
```python
age = int(input("Enter your age: "))
future_age = age + 5
print("In 5 years, you will be " + str(future_age) + " years old.")
```
---

## 📌 **Day 3 - Control Flow & Logical Operators**
### **Definition**
Control flow determines how a program executes statements based on conditions.

### **Use Cases**
- Implementing login authentication
- Game win/loss conditions

### **Concepts**
- `if`, `elif`, `else`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`
- **Nested Conditions**

### **Example**
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

## 📌 **Day 4 - Randomisation & Python Lists**
### **Definition**
- **Randomisation**: Generating unpredictable values using `random`
- **Lists**: Storing multiple items in a structured way

### **Concepts**
- Creating a list: `[]`
- Accessing elements: `list[0]`, `list[-1]`
- Modifying lists: `.append()`, `.remove()`, `.pop()`
- Random choices with `random.choice()`

### **Example**
```python
import random
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print("Random fruit: " + random_fruit)
```
---

## 📌 **Day 5 - Python Loops**
### **Definition**
Loops allow repetitive execution of a code block.

### **Concepts**
- **For Loops**: Iterating over lists, strings, and ranges
- **While Loops**: Repeating until a condition is `False`
- **Break & Continue**: Exiting or skipping iterations

### **Example**
```python
for i in range(1, 6):
    print("Iteration", i)

number = 1
while number < 5:
    print("Number is", number)
    number += 1
```
---

## 📌 **Day 6 - Functions & Karel**
### **Definition**
A **function** is a reusable block of code that performs a task.

### **Use Cases**
- Reducing redundancy
- Organizing large programs

### **Concepts**
- **Defining Functions**: `def function_name():`
- **Using Parameters & Return Values**
- **Calling Functions** to execute code

### **Example**
```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```
---

## 📌 **Day 7 - Hangman Game 🎮**
### **Definition**
A classic word-guessing game where players guess letters of a hidden word.

### **Concepts**
- **String Manipulation & Lists**
- **User Input Handling**
- **Looping Until Condition is Met**

### **Example**
```python
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

    if all(char in guessed_letters for char in word):
        print("You guessed the word! It was", word)
        break
else:
    print("You ran out of attempts! The word was", word)
```
---

## 📌 **Day 8 - Function Parameters & Caesar Cipher 🔐**
### **Definition**
The **Caesar Cipher** is a simple encryption technique that shifts letters.

### **Concepts**
- **Function Parameters & Return Values**
- **String Manipulation using ASCII**
- **Modular Arithmetic for Letter Wrapping**

### **Example**
```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            offset = ord(char) - ord(base)
            shifted = (offset + shift) % 26
            result += chr(ord(base) + shifted)
        else:
            result += char
    return result

encrypted = caesar_cipher("Hello World!", 3)
print(encrypted)  # Khoor Zruog!
```
---

## 📌 **Day 9 - Dictionaries, Nesting, & The Secret Auction 🏆**
### **Definition**
A **dictionary** stores data in key-value pairs, useful for structured information.

### **Concepts**
- **Dictionaries**: `{key: value}`
- **Nesting**: Storing lists inside dictionaries & vice versa
- **Iterating Through Dictionaries**

### **Example: Secret Auction**
```python
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True

highest_bid = max(bids.values())
winner = max(bids, key=bids.get)

print(f"The winner is {winner} with a bid of ${highest_bid}!")
```
---

## 🎯 **Conclusion**
By completing this **9-day Python beginner course**, you’ve learned:
✔️ Variables, data types, and type conversion  
✔️ Control flow with `if` statements  
✔️ Loops, functions, and logical operations  
✔️ Lists, dictionaries, and nested data structures  
✔️ Randomisation, encryption, and simple games  

🚀 Keep practicing and **happy coding!** 🐍💡  

