# ------------------------------------------------------
# 📚 Today class based on: Python Operators
# 🏫 Class: Two
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: April 2025
# 📘 Topic: All Types of Operators in Python
# ------------------------------------------------------

# ------------------------------
# 🧮 Arithmetic Operators
# ------------------------------
num1 = 5
num2 = 2
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# ------------------------------
# 📝 Assignment Operators
# ------------------------------
x = 7
print("\nInitial value of x:", x)

x += 3
print("After += 3:", x)

x -= 2
print("After -= 2:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

x //= 1
print("After //= 1:", x)

x %= 3
print("After %= 3:", x)

x **= 2
print("After **= 2:", x)

# ------------------------------
# 🔍 Comparison Operators
# ------------------------------
a = 5
b = 5
print("\na == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ------------------------------
# 🤖 Logical Operators
# ------------------------------
age = 20
has_ID = True
print("\nEligible to vote (age >= 18 and has ID):", age >= 18 and has_ID)

rainy = True
umbrella = False
print("Will stay dry (rainy or umbrella):", rainy or umbrella)

is_day = False
print("Is night (not is_day):", not is_day)

# ------------------------------
# 🆔 Identity Operators
# ------------------------------
list1 = [1, 2, 3]
list2 = list1
print("\nlist1 is list2:", list1 is list2)

x = [10, 20]
y = [10, 20]
print("x is not y:", x is not y)

# ------------------------------
# 📦 Membership Operators
# ------------------------------
fruits = ["apple", "banana", "mango"]
print("\n'mango' in fruits:", "mango" in fruits)

colors = ["red", "blue", "green"]
print("'yellow' not in colors:", "yellow" not in colors)

# ------------------------------
# 🧠 Bitwise Operators
# ------------------------------
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("\nBitwise AND (a & b):", a & b)
print("Bitwise OR (a | b):", a | b)
print("Bitwise XOR (a ^ b):", a ^ b)
print("Bitwise NOT (~a):", ~a)
print("Left Shift (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)

# ------------------------------------------------------
# ✅ End of class
# ------------------------------------------------------
