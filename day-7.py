# Task 1: Simple problem statements with logic + validation

print("=== TASK 1 ===")

# Problem 1: Even or Odd checker
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Problem 2: Simple login validation
username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# ---------------- TASK 2 ----------------

print("\n=== TASK 2 ===")

# Problem 3: Grade calculator with validation
marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# Problem 4: Simple number validation system
age = int(input("\nEnter age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")