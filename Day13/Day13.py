# Debugging Challenge

# In this challenge, you'll debug a Python program designed to implement a simple bubble sort algorithm. 
# Bubble sort is a basic sorting method that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. The process repeats until no more swaps are needed, indicating the list is sorted.

# The provided code aims to sort a list of integers in ascending order but contains several bugs:
# - It has a logical error in the loop conditions, potentially causing incomplete sorting or infinite loops.
# - There's an issue with how swaps are performed, which might not correctly exchange values.
# - Input validation is missing, so non-integer inputs could crash the program.
# - A syntax error exists in one of the statements.
# - The output printing has a formatting problem.

# Your task: Run the code, use `pdb` or an IDE debugger to step through it, identify the bugs, and correct them. Test with sample inputs like [5, 3, 8, 4, 2] (expected: [2, 3, 4, 5, 8]) and an empty list (expected: []).

# Instructions to Debug
# 1. Read ReadMe.md First To understand theory
# 2. Run this programm with debugger: `python -m pdb Day13.py`.
# 3. Insert breakpoints (e.g., `breakpoint()`) in the sort function if needed.
# 4. Input numbers like "5 3 8 4 2" and observe where it fails (e.g., incomplete sort or errors).
# 5. Fix bugs iteratively, re-testing each time.
# 6. Ensure it handles edge cases like empty input or single element.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i):  
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]  
    return arr

# Main program
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers] 
sorted_numbers = bubble_sort(numbers)
print("Sorted list:" sorted_numbers)  

# Corrected Solution (Commented Out)
# Please Dont see this untill you try debugging yourself

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):  # Fixed: Changed to n-i-1 to prevent index out of range in comparison
#             if arr[j] > arr[j+1]:
#                 # Fixed: Proper swap using temporary variable
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#     return arr

# Main program
# numbers_input = input("Enter numbers separated by spaces: ").split()
# try:
#     numbers = [int(num) for num in numbers_input]  # Fixed: Added try-except for input validation
# except ValueError:
#     print("Invalid input: Please enter integers only.")
#     exit(1)
# sorted_numbers = bubble_sort(numbers)
# print("Sorted list:", sorted_numbers)  # Fixed: Added comma for proper print formatting
