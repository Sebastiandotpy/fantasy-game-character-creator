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


# Task 4
# Define a dictionary mapping month names to the number of days
month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Prompt user to input the name of the month
month = input("Input the names of month: ")

# Retrieve the number of days from the dictionary and print it
days = month_days.get(month.capitalize(), None)
if days is not None:
    print(f"Number if days: {days} days")
else:
    print("Invalid month name!")



    # Task 5
    # Prompt user to input a number
    num = float(input("Enter a number: "))


    # Check if the number is even and divisible by 3 and print appropriate message
    if num % 2 == 0 and num % 3 == 0:
        print (f"{int(num)} is even and divisible by  3")
    else:
        print(f"{int(num)} is not even divisible by 3")    