# ------------------------------------------------------
# 📚 Today class based on: Python Control Flow, Loops & Data Structures
# 🏫 Class: Three
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: April 2025
# 📘 Lessons Covered:
#     - Lesson 05: Control Flow & Loops
#     - Lesson 06: Lists, Tuples & Dictionary
#     - Lesson 07: The Set & Frozenset
# ------------------------------------------------------

# -------------------------------------
# 🧵 String Basics
# -------------------------------------

# Single Quotes
str = 'Muhammad , Hammad!'
print(str)

# Double Quotes
str1 = "General Knowledge"
print(str1)

# Triple Quotes (Multiline String)
str2 = '''Python is a high-level 
general purpose programming language.'''
print(str2)

# String as an Array
text = "Hammad"
print(text[0])   # Output: H
print(text[3])   # Output: m

# String Concatenation
first = "Muhammad"
second = "Hammad"
result = first + " " + second
print(result)  # Output: Muhammad Hammad

# String Length
text = "Programming"
print(len(text))  # Output: 11

# Escape Sequence Characters
print("Ham,\b Mad!")   # \b = backspace
print("Ham,\tMad!")    # \t = tab
print("Ham, \"Mad!\"") # Quotes inside string
print("Ham,\\ Mad!")   # Backslash

# -------------------------------------
# 🔁 Control Flow
# -------------------------------------

# If-Else
num = 10
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# -------------------------------------
# 🔄 Loops
# -------------------------------------

# For Loop
for a in range(7):
    print("Iteration:", a)

# While Loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Nested Loops
for a in range(1, 4):
    for b in range(1, 4):
        print(f"a={a}, b={b}")

# Loop with else
for c in range(3):
    print(c)
else:
    print("Loop finished")

# Break Statement
for j in range(5):
    if j == 3:
        break
    print(j)

# -------------------------------------
# 📋 Data Structures
# -------------------------------------

# List
names = ["usama", "hammad", "zayan"]
names.append("aiman")  # Adding an item
print(names)

# Tuple
colors = ("yellow", "purple", "grey")
print(colors[1])  # Output: purple

# Dictionary
student = {
    "name": "Muhammad Hammad Zubair",
    "age": 22,
    "course": "Python"
}
student["age"] = 23  # Updating value
print(student["name"])  # Output: Muhammad Hammad Zubair
print(student["age"])   # Output: 23

# Set (Mutable & Unique Items)
my_set = {4, 5, 6}
print(my_set)

# Add number
my_set.add(7)
print(my_set)

# Remove number
my_set.remove(5)
print(my_set)

# -------------------------------------
# ✅ End of class
# ------------------------------------------------------
