"""
📘 Python Data Types - Easy Guide for Beginners
Author: Muhammad Hammad Zubair
Description:
    This program shows the most common data types in Python.
    It is written in a simple way, so beginners can understand easily.
"""

# -------------------------------------
# 🖨️ 1. Print a Message
# -------------------------------------
print("👋 Hello, World!")  # This shows a welcome message on the screen


# -------------------------------------
# 🔤 2. String (Text values)
# -------------------------------------
name = "Hammad"  # A string is any text written in quotes
print(" Name:", name)


# -------------------------------------
# 🔢 3. Integer (Whole numbers, no decimal)
# -------------------------------------
negative_number = -25
positive_number = 25
print("➖ Negative Number:", negative_number)
print("➕ Positive Number:", positive_number)


# -------------------------------------
# 🔣 4. Float (Numbers with decimal)
# -------------------------------------
pi = 3.14
print("🔸 Float Value:", pi)


# -------------------------------------
# ✅ 5. Boolean (True or False values)
# -------------------------------------
is_logged_in = True
has_access = False
print("🔓 Logged In:", is_logged_in)
print("🔒 Has Access:", has_access)


# -------------------------------------
# 📋 6. List (Group of items - can be changed)
# -------------------------------------
numbers = [1, 2, 3]
fruits = ["Apple", "Mango", "Cherry"]
print("🔢 Number List:", numbers)
print("🍎 Fruit List:", fruits)


# -------------------------------------
# 📦 7. Tuple (Group of items - cannot be changed)
# -------------------------------------
person = ("Umar", True, 4, 5)
print("👤 Person Info:", person)


# -------------------------------------
# 🧾 8. Dictionary (Key and value pairs)
# -------------------------------------
user = {
    "name": "Hammad",
    "city": "Karachi",
    "country": "Pakistan"
}
print("🗃️ User Information:")
print(" - Name:", user["name"])
print(" - City:", user["city"])
print(" - Country:", user["country"])


# -------------------------------------
# 🧮 9. Set (Group of unique items, no duplicates)
# -------------------------------------
unique_numbers = {1, 2, 3, 4}
unique_numbers.add(5)  # Add 5 to the set
print("🔁 Unique Numbers:", unique_numbers)


# -------------------------------------
# ❄️ 10. Frozen Set (Set that cannot be changed)
# -------------------------------------
frozen_values = frozenset({1, 2, 3})
frozen_map = {frozen_values: "Hammad"}
print("🧊 Frozen Set Map:", frozen_map)


# -------------------------------------
# 🚫 11. None (No value)
# -------------------------------------
result = None
if result is None:
    print("⚠️ Result has no value.")
else:
    print("✅ Result is:", result)
