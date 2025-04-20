# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 🏫 Class: Four
# 📅 Date: April 2025
# 📘 Lessons:
    # ✅ Lesson 08: Control Modules & Function Views
    # ✅ Lesson 09: Exception Handling
    # ✅ Lesson 10: File Handling
    # ✅ Lesson 11: Math, DateTime & Calendar Modules
# ------------------------------------------------------

# -------------------------------------
# 🧠 1. Function - Defining & Calling
# -------------------------------------
def greet_user(name):
    """
    This function takes a name as an argument and prints a greeting message.
    """
    print(f"👋 Welcome, {name}!")

greet_user("Hammad")


# -------------------------------------
# 🧾 2. Using Modules - Math, DateTime, Calendar
# -------------------------------------
import math  # For mathematical operations
import datetime  # For working with dates
import calendar  # For working with calendars

# 🔢 Math Module Example
radius = 5
circle_area = math.pi * (radius ** 2)  # Calculate area of a circle
print("📐 Circle Area:", round(circle_area, 2))

# 🕒 DateTime Module Example
today = datetime.date.today()  # Get today's date
print("📅 Today's Date:", today)

# 🗓️ Calendar Module Example
print("🗓️ April 2025 Calendar:\n")
print(calendar.month(2025, 4))


# -------------------------------------
# ⚠️ 3. Exception Handling - Try/Except
# -------------------------------------
try:
    num = int(input("🔢 Enter a number: "))  # Taking user input
    division = 100 / num  # Division operation
    print("✅ Result:", division)
except ValueError:
    print("❌ Please enter a valid number.")  # Handle invalid input
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")  # Handle division by zero error
finally:
    print("📌 Done with exception handling.")


# -------------------------------------
# 📂 4. File Handling - Write & Read
# -------------------------------------
# Writing to a file
with open("output_class4.txt", "w") as f:
    f.write("This is Class 4 by Muhammad Hammad Zubair\n")
    f.write("Learning File Handling in Python\n")

# Reading from a file
with open("output_class4.txt", "r") as f:
    file_content = f.read()  # Read content from the file
    print("📄 File Content:\n", file_content)


# -------------------------------------
# 🛠️ 5. Custom Functions (Optional Practice)
# -------------------------------------
def add(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract two numbers.
    """
    return a - b

# Example calls to functions
print("➕ 5 + 3 =", add(5, 3))
print("➖ 10 - 4 =", subtract(10, 4))

# -------------------------------------
# ✅ End of class
# ------------------------------------------------------
