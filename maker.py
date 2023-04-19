# Task 1: Compute the sum of 3 user input numbers
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
num3 = float(input("Enter number: "))

total = num1 + num2 + num3

print("Sum of the numbers:", total)

# Task 2: Prompt the user to input two numbers and handle invalid inputs
while True:
    try:
        num1 = float(input("Enter number 1: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        num2 = float(input("Enter number 2: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Compute the product of the two valid inputs
product = num1 * num2
print("Product of the numbers:", product)

# Task 3: Compute the maximum of 5 user input numbers
max_val = float('-inf')

for i in range(5):
    while True:
        try:
            num = float(input("Enter number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if num > max_val:
        max_val = num

print("Maximum of the numbers:", max_val)
